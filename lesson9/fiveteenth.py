import function
a = input("add/get info: ")
if a == "get info":
    students = ""
    try:
        file = open("fiveteenth.txt", "r")
    except Exception as a:
        print(a)
        function.collect_errors(a)
    else:
        t = file.readlines()
        for i in range(len(t)):
            q = t[i].split(", ")
            if int(q[0]) == 1005:
                students += f"{t[i]}"
        print(students)
else:
    b = input("write be like -> rollno, name, class, fees\n")
    try:
        file = open("fiveteenth.txt", "a")
    except Exception as a:
        print(a)
        function.collect_errors(a)
    else:
        file.write(f"{b}\n")
