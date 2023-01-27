def sum_index(*args):
    def check_type():
        if len(args) == 1:
            for i in args:
                if type(i) != list:
                    return "Please send only list."
                sum_ = 0
                for index, value in enumerate(i):
                    sum_ += index
                return sum_
        else:
            return "Please send only list."

    return check_type


sum1 = sum_index(2, 4, 5, 6)
print(sum1())
# result: Please send only list.

sum2 = sum_index([2, 4, 5, 6])
print(sum2())
# result: 6
