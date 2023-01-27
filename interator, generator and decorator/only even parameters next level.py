def math_operation(math_operation_, *args):
    """

    :param math_operation_: Enter "+", "-", "*", "/"
    :param args: Enter number split with comma
    :return:
    """

    def check():
        for i in args:
            if i % 2 != 0:
                return "Please add only even numbers!"
        plus_minus = 0
        multiplication_devision = 1
        if math_operation_ == "+":
            for i in args:
                plus_minus += i
            return plus_minus
        elif math_operation_ == "-":
            for i in range(len(args)):
                if i == 0:
                    plus_minus = args[0]
                    continue
                plus_minus -= args[i]
            return plus_minus
        elif math_operation_ == "*":
            for i in args:
                multiplication_devision *= i
            return multiplication_devision
        elif math_operation_ == "/":
            for i in range(len(args)):
                if i == 0:
                    multiplication_devision = args[0]
                    continue
                multiplication_devision /= args[i]
            return multiplication_devision
    return check

math1 = math_operation("+", 2,6,8,2,2,8)
print(math1())
