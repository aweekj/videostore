class Rental:

    def __init__(self, movie, days_rented):
        self._movie = movie
        self._days_rented = days_rented

    @property
    def movie(self):
        return self._movie

    @property
    def days_rented(self):
        return self._days_rented

    def cost(self):
        return self.movie.cost(self.days_rented)

    def points(self):
        return self.movie.points(self.days_rented)