import function
try:
    file = open("fifth.txt", "r")
except Exception as a:
    print(a)
    function.collect_errors(a)
else:
    t = file.readlines()
    lst = []
    for i in range(len(t)):
        a = t[i].split(" ")
        for e in a:
            if len(e) < 4:
                lst.append(e)
    print(lst)
