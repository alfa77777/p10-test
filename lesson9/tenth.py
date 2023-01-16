import function
try:
    file = open("tenth.txt", "r")
except Exception as a:
    print(a)
    function.collect_errors(a)
else:
    t = file.readlines()
    a = ""
    for i in t:
        for e in i:
            if e == "J":
                a += "I"
                continue
            a += f"{e}"
    print(a)