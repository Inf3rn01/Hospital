import sqlite3
import os
import settings


class DBManager:

    def __init__(self, db_path: str):
        self.db_path = db_path

    def check_base(self):
        return os.path.exists(self.db_path)

    def connect_db(self):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()

        return conn, cur

    def execute_sql_script(self, create_script: str, fill_script: str):
        conn, cur = self.connect_db()
        try:
            cur.executescript(open(create_script).read())
            cur.executescript(open(fill_script, encoding="utf-8").read())
            conn.commit()
            conn.close()
        except sqlite3.Error as error:
            print({'code': 500, 'msg': {error}})
            os.remove(self.db_path)

    def execute_query(self, query: str, fetchone: bool = True, args: tuple = None):
        conn, cur = self.connect_db()
        try:
            if fetchone:
                res = cur.execute(query, args).fetchone()
            else:
                res = cur.execute(query).fetchall()

            conn.commit()
            return {'code': 200, 'data': res}

        except sqlite3.IntegrityError:
            return {'code': 500, 'error': 'request contains unique error'}
        finally:
            conn.close()


db_manager = DBManager(db_path=settings.DB_PATH)
