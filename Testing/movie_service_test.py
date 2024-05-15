import unittest
from DAO import MovieService
from Entity import Movie


class TestMovieServiceModule(unittest.TestCase):
    # Setup: Arrange
    def setUp(self):
        self.movie_service = MovieService()

    def test_add_movie(self):
        title = "Leo"
        year = 2023
        director_id = 6
        new_movie = Movie(title, year, director_id)
        created_movie = self.movie_service.create_movie(new_movie)
        self.assertTrue(created_movie)


if __name__ == "__main__":
    unittest.main()
