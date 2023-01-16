import function
try:
    file = open("seventh.txt", "r")
except Exception as a:
    print(a)
    function.collect_errors(a)
else:
    t = file.readlines()
    count = 0
    for i in range(len(t)):
        a = t[i].split(" ")
        for e in a:
            if e[-1] == "e":
                count += 1
    print(count)
