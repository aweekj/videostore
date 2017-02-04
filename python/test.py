import unittest

from movie import Movie
from rental import Rental
from customer import Customer
from price import *


class Test(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)

    def test_customer(self):
        customer = Customer("Jamie")
        self.assertEqual(customer.name, "Jamie")

    def test_statement(self):
        customer = Customer("Jamie")
        movies = [Movie("Interstella", MovieCode.REGULAR),
                  Movie("Arrival", MovieCode.NEW_RELEASE),
                  Movie("Moana", MovieCode.CHILDREN),
                  Movie("LaLaLand", MovieCode.NEW_RELEASE)]

        for i in range(4):
            customer.add_rental(Rental(movies[i], i+3))

        self.assertEqual(customer.statement(), "Rental record for Jamie\n"
                         + "\tInterstella\t3.5\n" + "\tArrival\t12\n" + "\tMoana\t4.5\n" + "\tLaLaLand\t18\n"
                         + "You owed 38.0\nYou earned 6 points\n")


if __name__ == '__main__':
    unittest.main()