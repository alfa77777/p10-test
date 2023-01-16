import function
a = input("add/get info: ")
if a == "get info":
    b = input("enter author name: ")
    lst = []
    try:
        file = open("twelfth.txt", "r")
    except Exception as a:
        print(a)
        function.collect_errors(a)
    else:
        t = file.readlines()
        for i in range(len(t)):
            q = t[i].split(", ")
            if b in q:
                lst.append(q[1])
        print(lst)
else:
    b = input("write be like -> 'book_no, book_name, author, price': ")
    try:
        file = open("twelfth.txt", "a")
    except Exception as a:
        print(a)
        function.collect_errors(a)
    else:
        file.write(f"{b}\n")
