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


def insert_data(data: list[tuple[str, str, int]]) -> None:
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.executemany("INSERT INTO data (date, key, value) VALUES (?, ?, ?)", data)
    con.commit()
    con.close()


if __name__ == "__main__":
    create_schema()
    print("Schema created 🍰!")
