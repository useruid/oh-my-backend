## ACID

- Atomicity: атомарность - условно транзацкия выполнится полностью, либо не выполнится вообще)
- Consistency: это больше про набор constraint-ов, условно не должно быть два одинаковый человека с одним и тем же фио)
- Isolation: это нужно для того, чтобы не допустить race condition. есть следующие уровни изоляции транзакций
  - serializable (когда транзакции выполняются строко последовательно), чтобы не было проблем с доступом к данных
              главный минус - низкая производительнотсь
  - read uncommited (тут могут быть dirty reads)
  - read commited (транзакий могут работать параллельно, но при этом следующая транзация t2 увидит данные после commit t1, но есть и минусы:
  привести пример c письмами)
    - session 1:
      - ```
        SET SESSION CHARACTERISTICS AS TRANSACTION ISOLATION LEVEL READ COMMITTED; 1
        START TRANSACTION; 2
        INSERT INTO emails (body) values ('email 1'); 3
        select count(*) from emails; 4
        select * from emails; 9
        commit; 10
    - session 2:
      - ```
        SET SESSION CHARACTERISTICS AS TRANSACTION ISOLATION LEVEL READ COMMITTED; 5
        START TRANSACTION; 6
        INSERT INTO emails (body) values ('email 2'); 7
        COMMIT; 8
  - repeatable read or snapshot isolation (когда делается snapshot во время транзакции, поэтому на шаге 9 будет всего 3 письма)
    - session 1:
        - ```
          SET SESSION CHARACTERISTICS AS TRANSACTION ISOLATION LEVEL REPEATABLE READ; 1
          START TRANSACTION; 2
          INSERT INTO emails (body) values ('email 1'); 3
          select count(*) from emails; 4
          select * from emails; 9
          commit; 10
      - session 2:
        - ```
          SET SESSION CHARACTERISTICS AS TRANSACTION ISOLATION LEVEL REPEATABLE READ; 5
          START TRANSACTION; 6
          INSERT INTO emails (body) values ('email 2'); 7
          COMMIT; 8
База данных хранит в одно и то же время при snapshot isolation разные версии одного и того же объекта.
MVCC multiversion cincurrency control. 

- Durability (типо что после коммита данные хранятся на диске а не в оперативе)