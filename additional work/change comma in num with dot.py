def change_text_sign(func):
    def change_sign(file_path):
        try:
            result = func(file_path)
        except FileNotFoundError:
            result = "File not found!!!"
        return result
    return change_sign


@change_text_sign
def change_comma_with_dot(file_path):
    with open(file_path) as file:
        lines = file.readlines()
        result = ""
        for line in lines:
            words = line.split('"')
            for word in words:
                try:
                    if word.count(",") == 1:
                        check = word.split(",")
                        for i in check:
                            if i.isalnum():
                                line = line.replace(f"{word.split(',')[0]},{word.split(',')[1]}",
                                                    f"{word.split(',')[0]}.{word.split(',')[1]}")
                except IndexError:
                    pass
            result += line
        with open("countries of the world 2.csv", "w") as f:
            f.write(result)
        return result


print(change_comma_with_dot("countries of the world 1.csv"))
