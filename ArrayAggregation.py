class ArrayAggregation:
    def __init__(self, array):
        self.__array__ = array

    def max(self):
        value = self.__array__[0]

        for i in self.__array__:
            if i > value:
                value = i

        return value

    def min(self):
        value = self.__array__[0]

        for i in self.__array__:
            if i < value:
                value = i

        return value

    def sum(self):
        value = 0
        for i in self.__array__:
            value += i

        return value

    def product(self):
        value = 1
        for i in self.__array__:
            value *= i

        return value

    def average(self):
        return self.sum() / len(self.__array__)

