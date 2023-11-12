from ArrayAggregation import ArrayAggregation


class MatrixAggregation(ArrayAggregation):
    def __init__(self, matrix):
        self.__matrix__ = matrix

    def max(self):
        value = self.__matrix__[0][0]

        for row in self.__matrix__:
            for element in row:
                if element > value:
                    value = element

        return value

    def min(self):
        value = self.__matrix__[0][0]

        for row in self.__matrix__:
            for element in row:
                if element < value:
                    value = element

        return value

    def sum(self):
        value = 0
        for row in self.__matrix__:
            for element in row:
                value += element

        return value

    def product(self):
        value = 1
        for row in self.__matrix__:
            for element in row:
                value *= element

        return value

    def average(self):
        length = 0
        for row in self.__matrix__:
            length += len(row)

        return self.sum() / length
