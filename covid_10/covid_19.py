class Covid19:
    @staticmethod
    def find_hearder(file_path, header):
        with open(file_path) as file:
            lines = file.readlines()
            line = lines[0].split(",")
            count = 0
            try:
                while line[count] != header:
                    count += 1
            except IndexError:
                return "Invalide header name"

        return count

    @staticmethod
    def total_case_btw_100k_1m(file_path):
        with open(file_path) as file:
            lines = file.readlines()
            result = ""
            for i in range(len(lines)):
                line = lines[i].split(",")
                try:
                    if 100000 < int(line[Covid19.find_hearder(file_path, "TotalCases")]) < 1000000:
                        with open("total case 100k and 1m.csv", "a") as f:
                            f.write(f"{lines[i]}\n")
                            result += f"{lines[i]}\n"
                except ValueError:
                    pass
            return result

    @staticmethod
    def active_case_in_countries(file_path, country_name):
        with open(file_path) as file:
            lines = file.readlines()
            for i in range(len(lines)):
                line = lines[i].split(",")
                if line[Covid19.find_hearder(file_path, "Country/Region")] == country_name:
                    return line[Covid19.find_hearder(file_path, "ActiveCases")]

    @staticmethod
    def all_total_case_in_continent(file_path, contonent):
        with open(file_path) as file:
            lines = file.readlines()
            total_case = 0
            for i in range(len(lines)):
                line = lines[i].split(",")
                if line[Covid19.find_hearder(file_path, "Continent")] == contonent:
                    total_case += int(line[Covid19.find_hearder(file_path, "TotalCases")])
        return total_case

# print(Covid19.all_total_case_in_continent("worldometer_data.csv", "Asia"))
# print(Covid19.active_case_in_countries("worldometer_data.csv", "USA"))
# print(Covid19.total_case_btw_100k_1m("worldometer_data.csv"))
