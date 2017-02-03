from movie import Movie
from rental import Rental


class Customer:

    def __init__(self, name):
        self._name = name
        self._rentals = []

    def add_rental(self, arg):
        self._rentals.append(arg)

    @property
    def name(self):
        return self._name

    def statement(self):
        total_amount = 0
        frequent_renter_points = 0;
        rentals = self._rentals
        result = 'Rental record for ' + self.name + '\n'

        for rental in rentals:
            this_amount = 0

            if rental.movie.price_code == Movie.REGULAR:
                this_amount += 2
                if rental.days_rented > 2:
                    this_amount += (rental.days_rented - 2) * 1.5
            elif rental.movie.price_code == Movie.NEW_RELEASE:
                this_amount += rental.days_rented * 3
            elif rental.movie.price_code == Movie.CHILDREN:
                this_amount += 1.5
                if rental.days_rented > 3:
                    this_amount += (rental.days_rented - 3) * 1.5

            frequent_renter_points += 1
            if rental.movie.price_code == Movie.NEW_RELEASE and rental.days_rented > 1:
                frequent_renter_points += 1

            result += '\t' + rental.movie.title + '\t' + str(this_amount) + '\n'
            total_amount += this_amount

        result += 'You owed ' + str(total_amount) + '\n' + 'You earned ' + str(frequent_renter_points) + ' points\n'
        return result

if __name__ == '__main__':
    customer = Customer("Jamie")
    movies = [Movie("Interstella", Movie.REGULAR),
              Movie("Arrival", Movie.NEW_RELEASE),
              Movie("Moana", Movie.CHILDREN),
              Movie("LaLaLand", Movie.NEW_RELEASE)]

    for i in range(4):
        customer.add_rental(Rental(movies[i], i+3))

    print(customer.statement())
