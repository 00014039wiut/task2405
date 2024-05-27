import psycopg2


class DBContextManager:

    def __enter__(self):
        db_name = "Volleyball"
        password = "Sql7575"
        user = 'postgres'
        port = 5432
        host = 'localhost'

        self.conn = psycopg2.connect(database=db_name, password=password, user=user, port=port, host=host)
        self.cur = self.conn.cursor()
        show_all = """select * from person"""
        self.cur.execute(show_all)

        data = self.cur.fetchall()
        for row in data:
            print(row)
        print("This is the end of enter part")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        show_all = """select * from person"""
        self.cur.execute(show_all)

        data = self.cur.fetchall()
        for row in data:
            print(row)
        self.cur.close()
        self.conn.close()
        print("exit is working")


with DBContextManager() as manager:
    changes_query = """update person set teamnumber = 5 where id in (1 , 3, 5)"""
    manager.cur.execute(changes_query)
    manager.conn.commit()
