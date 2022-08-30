import sqlite3

DATABASE = "data.db"


def create_schema() -> None:
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    # sqlite has no DATE, https://www.sqlite.org/datatype3.html
    cur.execute(
        """
    CREATE TABLE IF NOT EXISTS data (
        date TEXT(10),
        key VARCHAR(255),
        value INT,
        PRIMARY KEY (date, key)
    );
    """
    )
    con.commit()
    con.close()


def load_data(data: list[tuple[str, str, int]]) -> None:
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.executemany("INSERT INTO data (date, key, value) VALUES (?, ?, ?)", data)
    con.commit()
    con.close()


def insert_data(date: str, key: str, value: int) -> None:
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute(
        """
    INSERT INTO data (date, key, value)
    VALUES (:_date, :_key, :_value)
    ON CONFLICT (date, key) DO UPDATE SET value = excluded.value
    """,
        {"_date": date, "_key": key, "_value": value},
    )
    con.commit()
    con.close()


if __name__ == "__main__":
    create_schema()
    print("Schema created 🍰!")
