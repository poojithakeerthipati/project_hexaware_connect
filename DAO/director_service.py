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

    def create_director(self, director):
        pass
