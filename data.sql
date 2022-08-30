PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE data (
        date TEXT(10),
        key VARCHAR(255),
        value INT,
        PRIMARY KEY (date, key)
    );
INSERT INTO data VALUES('2022-08-30','banana',42);
COMMIT;
