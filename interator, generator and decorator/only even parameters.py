def add(a, b):
    def check():
        if a % 2 != 0 or b % 2 != 0:
            return "Please add only even numbers!"
        else:
            return a + b

    return check


def multiple(a, b, c, d):
    def check():
        numbers = [a, b, c, d]
        for i in numbers:
            if i % 2 != 0:
                return "Please add only even numbers!"
        return a * b * c * d

    return check


add1 = add(2, 4)
print(add1())  # 6

multiple1 = multiple(2, 4, 5, 6)
print(multiple1())  # Please add only even numbers!

multiple1 = multiple(2, 4, 6, 8)
print(multiple1())  # 384
