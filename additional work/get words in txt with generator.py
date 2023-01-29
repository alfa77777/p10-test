def get_words():
    try:
        with open("test.txt") as text:
            line_words = text.readlines()
            for words in line_words:
                for word in words.split(" "):
                    yield word
    except FileNotFoundError:
        print("File not found")


words1 = get_words()
while True:
    try:
        print(next(words1))
    except StopIteration:
        print("Interation is over!!!")
        break
