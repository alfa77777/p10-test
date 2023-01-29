def return_num():
    for i in range(21):
        if i % 2 == 0:
            yield 0-i
            continue
        yield i


numbers = return_num()
while True:
    try:
        print(next(numbers))
    except StopIteration:
        print("Interation is over!!!")
        break
