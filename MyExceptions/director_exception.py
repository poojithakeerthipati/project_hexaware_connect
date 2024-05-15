class DirectorNotFoundError(Exception):
    def __init__(self, director_id):
        super().__init__(f"Director with {director_id} is not found")
