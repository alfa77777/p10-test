import function
try:
    file = open("frst.txt", "r")
except Exception as a:
    print(a)
    function.collect_errors(a)
else:
    print(file.read())
    file.close()
