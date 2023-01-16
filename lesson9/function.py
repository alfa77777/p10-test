from datetime import datetime


def collect_errors(a):
    with open("Exeptions.txt", "a") as error:
        error.write(f"{a}, time: {datetime.now()}\n")
