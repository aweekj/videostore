from price import *


class Movie:

    def __init__(self, title, price_code):
        self._title = title
        self._price = Price()
        self.price_code(price_code)

    @property
    def price_code(self):
        return self._price.price_code

    def price_code(self, price_code):
        if price_code == MovieCode.REGULAR:
            self._price = RegularPrice()
        elif price_code == MovieCode.NEW_RELEASE:
            self._price = NewReleasePrice()
        elif price_code == MovieCode.CHILDREN:
            self._price = ChildrenPrice()

    @property
    def title(self):
        return self._title

    def cost(self, days_rented):
        return self._price.cost(days_rented)

    def points(self, days_rented):
        return self._price.points(days_rented)
