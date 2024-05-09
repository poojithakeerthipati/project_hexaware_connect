import pyodbc

server_name = "DESKTOP-BJQV7BU\SQLEXPRESS"
database_name = "HexawareMovieDB"


conn_str = (
    f"Driver={{SQL Server}};"
    f"Server={server_name};"
    f"Database={database_name};"
    f"Trusted_Connection=yes;"
)
# print(conn_str)
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()
cursor.execute("SELECT 1")
print("Database connection is successful")


# class DirectorService:
#     def read_directors(self):
#         cursor.execute()
class MovieService:
    def read_movies(self):
        cursor.execute("SELECT * FROM Movies")
        # movies = cursor.fetchall()
        # for movie in movies:
        #     print(movie)

        # getting 1 row at a time
        for row in cursor:
            print(row)

    # def create_movie(n, y, d):
    #     cursor.execute(
    #         "INSERT INTO Movies (Title, Year, DirectorId) VALUES(?,?,?)",
    #         (n, y, d),
    #     )
    #     conn.commit()  # permanently inserts the value

    # def delete_movie():
    #     cursor.execute(
    #         "DELETE FROM Movies WHERE Title = ?",
    #         ("Guru"),
    #     )
    #     conn.commit()

    # Task 1: Get the data from the user [Clue: Use arguments]
    def create_movie(self, movie, year, directorId):
        cursor.execute(
            "INSERT INTO Movies (Title, Year, DirectorId) VALUES (?, ?, ?)",
            (movie, year, directorId),
        )
        conn.commit()  # Permanent storing | If no commit then no data

    # Task 2
    # Delete a movie from the db by getting the id from user
    def delete_movie(self, movie_id):
        cursor.execute("Delete from movies where MovieId=?", (movie_id))
        conn.commit()

    def update_movie(self, Movie_id, title, directorid, year):
        cursor.execute(
            "update Movies set title = ? ,year=?,directorid=? where MovieId=?",
            (title, year, directorid, Movie_id),
        )
        conn.commit()


# Task 3
# Choice
# Add a Movie
# Delete a Movie
def Movie_menu():
    movie_service = MovieService()
    while True:
        print(
            """
            Do you want to
            1. Create a Movie
            2. Display the movies
            3. Update the Movie
            4. Delete the Movie
            5. Exit
            """
        )

        choice = int(input("Please choose from above options: "))
        # print("1. Create a movie")
        # print("2.update the movie")
        # print("3. Delete a movie")
        # print("4. Read movies")
        # choice = input("Enter your choice: ")

        if choice == 1:
            name = input("Enter the movie name: ")
            year = int(input("Enter the year: "))
            director_id = int(input("Enter the director ID: "))
            movie_service.create_movie(name, year, director_id)
        elif choice == 2:
            movie_service.read_movies()
        elif choice == 3:
            MovieId = int(input("Enter the MovieId: "))
            title = input("Enter the movie name: ")
            year = int(input("Enter the year: "))
            director_id = int(input("Enter the director ID: "))
            movie_service.update_movie(MovieId, title, director_id, year)
        elif choice == 4:
            title = input("Enter the Title that you need to update: ")
            MovieId = int(input("Enter the MovieId: "))
            movie_service.delete_movie(MovieId)
        elif choice == 5:
            print("You have exited successfully")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


def director_menu():
    pass


def actors_menu():
    pass


if __name__ == "__main__":
    while True:
        print(
            """
            select one from below
            1.Movie Management
            2.Director Management
            3.Actors Management
            4.Exit to Main Menu"""
        )

        choice1 = int(input("Enter Your choice: "))

        if choice1 == 1:
            Movie_menu()
        elif choice1 == 2:
            director_menu()
        elif choice1 == 3:
            actors_menu()
        elif choice1 == 4:
            print("Back to Main menu")
            break
        else:
            print("Invalid choice,Please enter a valid option")
    cursor.close()
    conn.close()
    # movie = input("What's the Movie?🎥: ")
    # year = int(input("When was it released?📆:"))
    # directorId = int(input("Director's ID🪪: "))
    # create_movie(movie, year, directorId)
    # movie = input("Enter a Movie ID to delete🚮: ")
    # delete_movie(movie)
    # read_movies()

# if __name__ == "__main__":
#     name = input("enter a movie name:")
#     year = int(input("enter the year"))
#     directId = int(input("enter the director Id:"))
#     create_movie(name, year, directId)
#     delete_movie()
#     read_movies()
