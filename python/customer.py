from price import MovieCode
from rental import Rental
from movie import Movie


class Customer:

    def __init__(self, name):
        self._name = name
        self._rentals = []

    def add_rental(self, arg):
        self._rentals.append(arg)

    @property
    def name(self):
        return self._name

    @property
    def rentals(self):
        return self._rentals

    def statement(self):
        result = 'Rental record for ' + self.name + '\n'

        for rental in self.rentals:
            result += '\t' + rental.movie.title + '\t' + str(rental.cost()) + '\n'

        result += 'You owed ' + str(self.calculate_total_cost()) + '\n' \
                  + 'You earned ' + str(self.calculate_total_point()) + ' points\n'
        return result

    def html_statement(self):
        result = '<h1><em>Rental record for ' + self.name + '</em></h1><p>\n'

        for rental in self.rentals:
            result += rental.movie.title + ': ' + str(rental.cost()) + '<br>\n'

        result += '<p>You owed <em>' + str(self.calculate_total_cost()) + '</em><p>\n' \
                  + 'You earned <em>' + str(self.calculate_total_point()) + '</em> points<p>\n'
        return result

    def calculate_total_cost(self):
        result = 0
        for rental in self.rentals:
            result += rental.cost()
        return result

    def calculate_total_point(self):
        result = 0
        for rental in self.rentals:
            result += rental.points()
        return result


if __name__ == '__main__':
    customer = Customer("Jamie")
    movies = [Movie("Interstella", MovieCode.REGULAR),
              Movie("Arrival", MovieCode.NEW_RELEASE),
              Movie("Moana", MovieCode.CHILDREN),
              Movie("LaLaLand", MovieCode.NEW_RELEASE)]

    for i in range(4):
        customer.add_rental(Rental(movies[i], i+3))

    print(customer.statement())
