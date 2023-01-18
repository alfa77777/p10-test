class Countries:
    @staticmethod
    def population_gt_20m(file_path):
        with open(file_path) as f:
            lines = f.readlines()
            countries = ""
            for i in range(len(lines)):
                words = lines[i].split(",")
                try:
                    if int(words[2]) > 20000000:
                        countries += f"{words[0]}\n"
                except ValueError:
                    pass
            return countries

    @staticmethod
    def c_countries(file_path):
        with open(file_path) as f:
            lines = f.readlines()
            c_countries = ""
            for i in range(len(lines)):
                words = lines[i].split(",")
                try:
                    if words[0][1] == "C":
                        c_countries += f"{words[0]}\n"
                except ValueError:
                    pass
            with open("c countries.txt", "w") as c:
                c.write(f"{c_countries}\n")
            return c_countries


print(Countries.population_gt_20m("countries of the world.csv"))
print(Countries.c_countries("countries of the world.csv"))
