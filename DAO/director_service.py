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

    def update_director(self, Director):
        self.cursor.execute(
            """" update directors 
            set Name = ?
            where ID = ?""",
            (Director.Name, Director.ID),
        )
        self.conn.commit()

    def delete_director(self, Diretor):
        self.cursor.execute("delete from directors where ID=?", (Diretor.ID))
        self.conn.commit()
