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


if __name__ == "__main__":
    reset_db()
    print_db()
    create_schema()
    print_db()
    print("🍰")
