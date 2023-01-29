def get_names():
    with open("planets.txt") as info:
        lines = info.readlines()
        for line in lines:
            if line[0:4] == "name":
                yield line.split(" ")[2]


words1 = get_names()
while True:
    try:
        print(next(words1))
    except StopIteration:
        print("Interation is over!!!")
        break
