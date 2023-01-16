import function
try:
    file = open("scond.txt", "r")
except Exception as a:
    print(a)
    function.collect_errors(a)
else:
    t = file.readlines()
    count = 0
    for i in t:
        if i[0] == "T":
            continue
        count += 1
    print(count)
    file.close()
