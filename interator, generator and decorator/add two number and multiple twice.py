def add(a, b):
    def multiple_twice():
        return (a+b)*2
    return multiple_twice

four_five = add(4, 5)
print(four_five())