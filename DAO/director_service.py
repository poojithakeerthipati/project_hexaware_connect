from tabulate import *
from Util.DBconn import DBConnection


class DirectorService(DBConnection):
    def read_directors(self):
        try:
            self.cursor.execute("SELECT * FROM Directors")
            directors_data = [list(row) for row in self.cursor.fetchall()]
            headers = ["DirectorID", "Name"]
            print(tabulate(directors_data, headers=headers, tablefmt="grid"))
        except Exception as e:
            print(e)

    def create_director(self, Director):
        self.cursor.execute("insert into Directors(Name) values(?)", (Director.Name))
        self.conn.commit()

    def update_director(self, Director, Director_ID):
        self.cursor.execute(
            "update Directors set Name = ? where DirectorId = ?",
            (Director.Name, Director_ID),
        )
        self.conn.commit()

    def delete_director(self, DiretorID):
        self.cursor.execute("delete from directors where directorID=?", (DiretorID))
        self.conn.commit()
