import function
a = input("add/get info: ")
if a == "get info":
    employees = ""
    try:
        file = open("fourteenth.txt", "r")
    except Exception as a:
        print(a)
        function.collect_errors(a)
    else:
        t = file.readlines()
        for i in range(len(t)):
            q = t[i].split(", ")
            if float(q[2]) > 30000:
                employees += f"{t[i]}"
        print(employees)
else:
    b = input("write be like -> empcode, name, salary\n")
    try:
        file = open("fourteenth.txt", "a")
    except Exception as a:
        print(a)
        function.collect_errors(a)
    else:
        file.write(f"{b}\n")
