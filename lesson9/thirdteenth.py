import function
a = input("add/get info: ")
if a == "get info":
    count = 0
    try:
        file = open("thirdteenth.txt", "r")
    except Exception as a:
        print(a)
        function.collect_errors(a)
    else:
        t = file.readlines()
        for i in range(len(t)):
            q = t[i].split(", ")
            if float(q[2]) > 75:
                count += 1
        print(count)
else:
    b = input("write be like -> admission_number, Name, Percentage\n")
    try:
        file = open("thirdteenth.txt", "a")
    except Exception as a:
        print(a)
        function.collect_errors(a)
    else:
        file.write(f"{b}\n")
