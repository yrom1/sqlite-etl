PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE data (
        date TEXT(10),
        key VARCHAR(255),
        value INT,
        PRIMARY KEY (date, key)
    );
COMMIT;
