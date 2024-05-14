import pyodbc
from tabulate import tabulate
from Entity.movie import *
from Entity.Director import *
from DAO.movie_service import *
from DAO.director_service import *

# server_name = "SAMAR\\MSSQLSERVER01"
# database_name = "MoviesDB"

# conn_str = (
#     f"Driver={{SQL Server}};"
#     f"Server={server_name};"
#     f"Database={database_name};"
#     f"Trusted_Connection=yes;"
# )

# print(conn_str)
# conn = pyodbc.connect(conn_str)
# cursor = conn.cursor()
# cursor.execute("Select 1")
# print("Database connection is successful 🎊")


class MainMenu:
    movie_service = MovieService()
    director_service = DirectorService()

    def movie_menu(self):

        while True:
            print(
                """      
            1. Add a Movie
            2. View all Movies
            3. Update a Movie  
            4. Delete a Movie
            5. Back to main menu
                    """
            )
            choice = int(input("Please choose from above options: "))

            if choice == 1:
                title = input("Please enter movie title: ")
                year = int(input("Please enter movie year: "))
                director_id = int(input("Please enter movie director's id: "))
                new_movie = Movie(title, year, director_id)
                self.movie_service.create_movie(new_movie)
            elif choice == 2:
                self.movie_service.read_movies()
            elif choice == 3:
                movie_id = int(input("Please enter movie's id: "))
                title = input("Please enter movie title: ")
                year = int(input("Please enter movie year: "))
                director_id = int(input("Please enter movie director's id: "))
                updated_movie = Movie(title, year, director_id)
                self.movie_service.update_movie(updated_movie, movie_id)
            elif choice == 4:
                movie_id = int(input("Please tell a movie id to delete: "))
                self.movie_service.delete_movie(movie_id)
            elif choice == 5:
                break

    def director_menu(self):
        while True:
            print(
                """
            1.Insert a new Director
            2.View All Directors
            3.update the Director
            4.Delete the Director
            5.Back to main menu"""
            )
            choice = int(input("Please choose from above options:"))
            if choice == 1:
                Name = input("Please Enter the Name of the director: ")
                new_director = Director(Name)
                self.director_service.create_director(new_director)
            elif choice == 2:
                self.director_service.read_directors()
            elif choice == 3:
                Name = input("Please Enter the Name of the director: ")
                Director_ID = int(input("Please Enter the Director Id to update: "))
                updated_director = Director(Name)
                self.director_service.update_director(updated_director, Director_ID)
            elif choice == 4:
                director_id = int(input("Please tell a director id to delete: "))
                self.director_service.delete_director(director_id)
            elif choice == 5:
                break

    def actor_menu():
        pass


def main():
    main_menu = MainMenu()

    while True:
        print(
            """      
                1. Movie Management
                2. Director Management
                3. Actor Management
                4. Exit
                    """
        )

        choice = int(input("Please choose from above options: "))

        if choice == 1:
            main_menu.movie_menu()
        elif choice == 2:
            main_menu.director_menu()
        elif choice == 3:
            main_menu.actor_menu()
        elif choice == 4:
            main_menu.movie_service.close()
            main_menu.director_service.close()
            break


if __name__ == "__main__":
    print("Welcome to the movies app")
    main()

    # cursor.close()
    # conn.close()
