from tabulate import *
from Util.DBconn import DBConnection
from abc import ABC, abstractmethod
from MyExceptions.director_exception import DirectorNotFoundError


class IDirectorService(ABC):
    @abstractmethod
    def read_directors(self):
        pass

    @abstractmethod
    def create_director(self, director):
        pass

    @abstractmethod
    def update_director(self, director, Director_ID):
        pass

    @abstractmethod
    def delete_director(self, DirectorID):
        pass

    @abstractmethod
    def read_director_by_id(self, DirectorID):
        pass


class DirectorService(IDirectorService, DBConnection):
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

    def read_director_by_id(self, Director_ID):
        try:
            self.cursor.execute(
                "SELECT * FROM Directors where DirectorId=?", (Director_ID)
            )
            directors = self.cursor.fetchall()
            if len(directors) == 0:
                raise DirectorNotFoundError(Director_ID)
            else:
                print(directors)
        except Exception as e:
            print("OOPs Error happend: ", e)
