from code import MovieCode


class Price:
    def __init__(self):
        self._price_code = -1

    @property
    def price_code(self):
        return self._price_code

    def cost(self, days_rented):
        result = 0
        return result

    def points(self, days_rented):
        result = 0
        return result


class RegularPrice(Price):

    @property
    def price_code(self):
        return MovieCode.REGULAR

    def cost(self, days_rented):
        result = 2
        if days_rented > 2:
            result += (days_rented - 2) * 1.5
        return result

    def points(self, days_rented):
        return 1


class NewReleasePrice(Price):

    @property
    def price_code(self):
        return MovieCode.NEW_RELEASE

    def cost(self, days_rented):
        return days_rented * 3

    def points(self, days_rented):
        if days_rented > 1:
            return 2
        else:
            return 1


class ChildrenPrice(Price):

    @property
    def price_code(self):
        return MovieCode.CHILDREN

    def cost(self, days_rented):
        result = 1.5
        if days_rented > 3:
            result += (days_rented - 3) * 1.5
        return result

    def points(self, days_rented):
        return 1

