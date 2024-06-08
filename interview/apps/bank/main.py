# poetry run uvicorn main:app --host 0.0.0.0 --reload
import os
import uuid
from typing import Optional
from loguru import logger

import time
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, status
from fastapi_sqlalchemy import DBSessionMiddleware, db
from pydantic import BaseModel
from sqlalchemy import (
    BigInteger,
    Column,
    DateTime,
    ForeignKey,
    create_engine,
    func,
)
from sqlalchemy.dialects import postgresql
from sqlalchemy.ext.declarative import declarative_base
from time import sleep

load_dotenv(override=True)

engine = create_engine(os.environ["PG_URI"])

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["PG_URI"])

Base = declarative_base()


def insert_data():
    initial_amounts = [0, 20, 30, 50]

    for amount in initial_amounts:
        with db():
            cnt_wallets = db.session.query(ModelWallet).count()
            if cnt_wallets != len(initial_amounts):
                db.session.add(
                    ModelWallet(
                        amount=amount
                    )
                )
                db.session.commit()


@app.on_event("startup")
async def create_tables():
    Base.metadata.create_all(bind=engine)
    insert_data()



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


@app.patch("/reload_db")
def reload_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    insert_data()


# Views
@app.put(
    "/wallets/make-transaction",
    response_model=WalletTransactionOut,
    status_code=status.HTTP_200_OK,
)
def update_wallet_transaction(
        wallet_id_debit: str, wallet_id_credit: str, amount: int, sleep_sec: int
):
    logger.info(
        f"Wallet debit id: {wallet_id_debit}, Wallet credit id: {wallet_id_credit}, Amount: {amount}"
    )

    with db.session.begin():
        db_wallet_debit = (
            db.session.query(ModelWallet).filter_by(id=wallet_id_debit).with_for_update().first()
        )

        sleep(sleep_sec)

        logger.info(f"Wallet debit: {db_wallet_debit.id}, {db_wallet_debit.amount}")

        if not db_wallet_debit:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Wallet debit not found",
            )

        if (db_wallet_debit.amount - amount) < 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Insufficient funds",
            )

        db_wallet_credit = (
            db.session.query(ModelWallet).filter_by(id=wallet_id_credit).with_for_update().first()
        )

        if not db_wallet_credit:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Wallet credit not found",
            )

        db_wallet_debit.amount -= amount
        db.session.add(db_wallet_debit)

        db_wallet_credit.amount += amount
        db.session.add(db_wallet_credit)

        db_transaction = ModelTransaction(
            wallet_credit_id=db_wallet_credit.id,
            wallet_debit_id=db_wallet_debit.id,
            amount=amount,
        )
        db.session.add(db_transaction)
        db.session.commit()

    return WalletTransactionOut(
        wallet_credit=Wallet(**db_wallet_credit.__dict__), wallet_debit=Wallet(**db_wallet_debit.__dict__)
    )

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)


# TODO: https://deadlockempire.github.io/#L2-deadlock
# TODO: select for update


# random
import random

elements = [1, 2, 3, 4, 5]
new_elements = []
counter = 0

while elements:
    counter += 1
    rnd = random.random()
    if rnd > 0.5:
        el = random.choice(elements)
        new_elements.append(el)
        elements.pop(elements.index(el))


def try_except_example(divider):
    try:
        result = 1 // divider
    except ZeroDivisionError as e:
        raise e
    else:
        print(result)
        return result
    finally:
        print('finished')


try_except_example(10)


my_gen = (i ** 2 for i in range(10))

list(my_gen)


def list_for_loop(n):
    lst = []
    for i in range(n):
        lst.append(i)
    return lst


def list_comprehension(n):
    return [i for i in range(n)]


import dis
dis.dis(list_for_loop)
dis.dis(list_comprehension)