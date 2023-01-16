import function
try:
    file = open("eleventh.txt", "r")
except Exception as a:
    print(a)
    function.collect_errors(a)
else:
    t = file.readlines()
    a = 0
    m = 0
    for i in t:
        for e in i:
            if e.lower() == "a":
                a += 1
            elif e.lower() == "m":
                m += 1
    print(f'"a" or "A" = {a}\n"m" or "M" = {m}')