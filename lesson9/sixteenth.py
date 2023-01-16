import function
a = input("add/get info: ")
if a == "get info":
    fees = 0
    try:
        file = open("sixteenth.txt", "r")
    except Exception as a:
        print(a)
        function.collect_errors(a)
    else:
        t = file.readlines()
        for i in range(len(t)):
            q = t[i].split(", ")
            fees += float(q[3])
        print(fees)
else:
    b = input("write be like -> rollno, name, class, fees\n")
    try:
        file = open("sixteenth.txt", "a")
    except Exception as a:
        print(a)
        function.collect_errors(a)
    else:
        file.write(f"{b}\n")
