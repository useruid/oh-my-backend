import os
import uuid
from typing import Optional

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, status
from fastapi_sqlalchemy import DBSessionMiddleware, db
from pydantic import BaseModel
from sqlalchemy import (
    BigInteger,
    CheckConstraint,
    Column,
    DateTime,
    ForeignKey,
    UniqueConstraint,
    create_engine,
    func,
)
from sqlalchemy.dialects import postgresql
from sqlalchemy.exc import DatabaseError
from sqlalchemy.ext.declarative import declarative_base

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

engine = create_engine(os.environ["DATABASE_URL"])

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])

Base = declarative_base()


# Models

class ModelWallet(Base):
    __tablename__ = "wallets"

    id = Column(
        postgresql.UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    amount = Column(BigInteger, nullable=False)


class ModelTransaction(Base):
    __tablename__ = "transactions"
    id = Column(
        postgresql.UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    created_on = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
    wallet_credit_id = Column(
        postgresql.UUID(as_uuid=True),
        ForeignKey("wallets.id"),
    )
    wallet_debit_id = Column(
        postgresql.UUID(as_uuid=True),
        ForeignKey("wallets.id"),
    )
    amount = Column(BigInteger, nullable=False)


# Schemas
class Wallet(BaseModel):
    id: Optional[uuid.UUID] = None
    amount: int = 0

    class Config:
        orm_mode = True


class WalletTransactionOut(BaseModel):
    wallet_credit: Wallet
    wallet_debit: Wallet


# Views
@app.put(
    "/wallets/make-transaction",
    response_model=WalletTransactionOut,
    status_code=status.HTTP_200_OK,
)
def update_wallet_transaction(
        wallet_id_debit: str, wallet_id_credit: str, amount: int
):
    db_wallet_debit = (
        db.session.query(ModelWallet).filter_by(id=wallet_id_debit).first()
    )
    db_wallet_credit = (
        db.session.query(ModelWallet).filter_by(id=wallet_id_credit).first()
    )

    db_wallet_debit.amount -= amount
    db.session.add(db_wallet_debit)
    db.session.commit()
    db_wallet_credit.amount += amount
    db.session.add(db_wallet_credit)
    db.session.commit()

    db_transaction = ModelTransaction(
        wallet_credit_id=db_wallet_credit.id,
        wallet_debit_id=db_wallet_debit.id,
        amount=amount,
    )
    db.session.add(db_transaction)
    db.session.commit()

    return WalletTransactionOut(
        wallet_credit=db_wallet_credit, wallet_debit=db_wallet_debit
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)