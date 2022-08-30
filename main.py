import sqlite3
from subprocess import run


def load_db() -> None:
    run("sqlite3 data.db < data.sql", shell=True)


def save_db() -> None:
    run("sqlite3 data.db .dump > data.sql", shell=True)
    run("rm data.db", shell=True)


def create_schema() -> None:
    # NOTE this is not written to be idempotent if the schema already exists
    con = sqlite3.connect(f"data.db")
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


def insert_data(data: list[tuple[str, str, int]]) -> None:
    con = sqlite3.connect(f"data.db")
    cur = con.cursor()
    cur.executemany("INSERT INTO data VALUES (?, ?, ?)", data)
    con.commit()
    con.close()


if __name__ == "__main__":
    load_db()
    create_schema()
    # insert_data(...) TODO
    save_db()
    print("Done 🍰!")
