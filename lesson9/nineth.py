import function
try:
    file = open("nineth.txt", "r")
except Exception as a:
    print(a)
    function.collect_errors(a)
else:
    t = file.readlines()
    a = ""
    for i in t:
        for e in i:
            a += f"{e}#"
    print(a)
