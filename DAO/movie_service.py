from tabulate import *
from Util.DBconn import DBConnection


class MovieService(DBConnection):

    # def __init__(self, conn):
    #     self.conn = conn
    #     self.cursor = conn.cursor()

    def read_movies(self):
        try:
            self.cursor.execute("Select * from Movies")
            movies_data = [list(row) for row in self.cursor.fetchall()]
            headers = ["MovieId", "Title", "Year", "DirectorId"]
            print(tabulate(movies_data, headers=headers, tablefmt="grid"))
        except Exception as e:
            print(e)
        # finally:
        #     self.cursor.close()
        #     self.conn.close()

    def create_movie(self, movie):
        self.cursor.execute(
            "INSERT INTO Movies (Title, Year, DirectorId) VALUES (?, ?, ?)",
            (movie.title, movie.year, movie.director_id),
        )
        self.conn.commit()

    def update_movie(self, movie, movie_id):
        self.cursor.execute(
            """
            Update Movies
            Set Title = ?, Year = ?, DirectorId = ?
            where MovieId = ?
            """,
            (movie.title, movie.year, movie.director_id, movie_id),
        )
        self.conn.commit()

    def delete_movie(self, movie_id):
        self.cursor.execute("Delete from Movies Where MovieId = ?", movie_id)
        self.conn.commit()

    # def close(self):
    #     self.cursor.close()
    #     self.conn.close()


# class MovieService:
#     def __init__(self, conn):
#         self.conn = conn
#         self.cursor = conn.cursor()

#     def read_movies(self):
#         try:
#             self.cursor.execute("Select * from Movies")
#             # movies = cursor.fetchall() # Get all data
#             # for movie in movies:
#             #     print(movie)

#             # Get data one row at a time
#             for row in self.cursor:
#                 print(row)
#         except Exception as e:
#             print(e)
#         finally:
#             self.cursor.close()
#             self.conn.close()

#     # Task 1
#     # Get the data from the user
#     # Clue: Use arguments
#     def create_movie(self, movie):
#         try:
#             self.cursor.execute(
#                 "INSERT INTO Movies (Title, Year, DirectorId) VALUES (?, ?, ?)",
#                 (movie.title, movie.year, movie.director_id),
#             )
#             self.conn.commit()  # Permanent storing | If no commit then no data
#         except Exception as e:
#             print(e)
#         finally:
#             self.close()

#     def update_movie(self, movie, movie_id):
#         try:
#             self.cursor.execute(
#                 """
#             Update Movies
#             Set Title = ?, Year = ?, DirectorId = ?
#             where MovieId = ?
#             """,
#                 (movie.title, movie.year, movie.director_id, movie_id),
#             )
#             self.conn.commit()  # Permanent storing | If no commit then no data
#         except Exception as e:
#             print(e)
#         finally:
#             self.close()

#     # Task 2
#     # Delete a movie from the db by getting the id from user
#     def delete_movie(self, movie_id):
#         try:
#             self.cursor.execute("Delete from Movies Where MovieId = ?", movie_id)
#             self.conn.commit()
#         except Exception as e:
#             print(e)
#         finally:
#             self.close()

#     def close(self):
#         self.cursor.close()
#         self.conn.close()
