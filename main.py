import sqlite3
from subprocess import run

DATABASE = "data.db"


def print_db():
    print(f"--- {DATABASE} ---")
    run(f"cat {DATABASE}", shell=True)


def reset_db():
    run(f"rm {DATABASE}", shell=True)
    run(f"touch {DATABASE}", shell=True)


def create_schema():
    con = sqlite3.connect(f"{DATABASE}")
    cur = con.cursor()
    # sqlite has no DATE, https://www.sqlite.org/datatype3.html
    cur.execute(
        """
    CREATE TABLE data (
        date TEXT(10),
        key VARCHAR(255),
        value INT,
        PRIMARY KEY (date, key)
    );
    """
    )
    con.commit()
    con.close()


def insert_data():
    con = sqlite3.connect(f"{DATABASE}")
    cur = con.cursor()
    cur.execute("INSERT INTO data VALUES (CURRENT_DATE, 'banana', 42)")
    con.commit()
    con.close()


if __name__ == "__main__":
    reset_db()
    print_db()
    create_schema()
    insert_data()
    print_db()
    print("🍰")
