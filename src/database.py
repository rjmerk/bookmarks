from enum import Enum, unique
import datetime
import psycopg2
from typing import List, Dict, Optional


@unique
class TABLE(Enum):
    BOOKMARKS = 'bookmarks'


class Database:

    def __init__(self):
        self.conn = psycopg2.connect("dbname=bookmark_db user=bookmark_user")
        self.cursor = None

    def get_by_id(self, table: str, id_: int) -> Optional[Dict]:
        with self.conn.cursor() as cur:
            cur.execute(
                f"select * from {table} where id = %(id_)s;",
                dict(id_=id_)
            )
            result = cur.fetchone()
        return result

    def get_all(self, table: str, limit=10) -> List:
        with self.conn.cursor() as cur:
            cur.execute(
                f"select * from {table} limit %(limit)s",
                dict(limit=limit)
            )
            result = cur.fetchall()
        return result

    def create_bookmark(self, url, name):
        created = datetime.datetime.now()
        with self.conn.cursor() as cur:
            cur.execute(
                "INSERT INTO bookmarks (url, name, created) VALUES (%s, %s, %s)",
                (url, name, created)
            )
        self.conn.commit()


def main():
    db = Database()
    db.create_bookmark(
        url="https://joshreads.com/",
        name="The Comics Curmudgeon")
    x = db.get_by_id(TABLE.BOOKMARKS.name, 1)
    print(x)
    print(db.get_all(TABLE.BOOKMARKS.name))
    print([t.name for t in TABLE])


if __name__ == "__main__":
    main()
