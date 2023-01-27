"""
get next multiple with interator
"""


class GetMultipleWithInterator:

    def __init__(self, num):
        self.num = num

    def __iter__(self):
        self.n = self.num
        return self

    def __next__(self):
        pow_number = self.n
        self.n += self.num
        return pow_number


numbers = GetMultipleWithInterator(13)
iterator = iter(numbers)
for i in range(5):
    print(next(iterator))

"""
get next multiple with generator
"""


class GetMultipleWithGenerator:

    def __init__(self, num):
        self.num = num

    def generator(self):
        for number in range(5):
            yield (number + 1) * self.num


numbers = GetMultipleWithGenerator(3)
for value in numbers.generator():
    print(value)
