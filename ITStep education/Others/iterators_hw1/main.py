from math import sqrt
from itertools import count, islice


def is_prime(n):
    return all(n % i for i in islice(count(2), int(sqrt(n) - 1)))


class PrimesIterator:
    def __init__(self, end):
        self.start = 1
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start > self.end:
            raise StopIteration
        if is_prime(self.start):
            return self.start
        else:
            return self.__next__()


for n in PrimesIterator(50): print(n)