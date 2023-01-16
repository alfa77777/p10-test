import function
try:
    file = open("third.txt", "r")
except Exception as a:
    print(a)
    function.collect_errors(a)
else:
    t = file.readlines()
    count = 0
    for i in range(len(t)):
        a = t[i].split(" ")
        count += len(a)
    print(count)
    file.close()
