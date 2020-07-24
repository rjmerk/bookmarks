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

    def get_by_id(self, table: TABLE, id_: int) -> Optional[Dict]:
        with self.conn.cursor() as cur:
            cur.execute(
                f"select * from {table.name} where id = %(id_)s;",
                dict(id_=id_)
            )
            result = cur.fetchone()
        return result

    def get_all(self, table: TABLE, limit: int = 10) -> List:
        with self.conn.cursor() as cur:
            cur.execute(
                f"select * from {table.name} limit %(limit)s",
                dict(limit=limit)
            )
            result = cur.fetchall()
        return result

    def create_bookmark(self, url: str, name: str):
        created = datetime.datetime.now()
        with self.conn.cursor() as cur:
            cur.execute(
                "INSERT INTO bookmarks (url, name, created) VALUES (%s, %s, %s)",
                (url, name, created)
            )
        self.conn.commit()


db = Database()
