import csv


class InstagramAccountInCountry:
    def __init__(self, file_path, country_name):
        self.file_path = file_path
        self.country_name = country_name

    def get_data_with_dict(self):
        try:
            with open(self.file_path) as csv_file:
                csv_reader = csv.DictReader(csv_file)
                return [row for row in csv_reader]
        except (FileNotFoundError, UnicodeDecodeError) as e:
            print(e)

    def separate_accounts_by_country(self):
        info = self.get_data_with_dict()
        result = "No,Rank,Username,Owner,Followers(millions)[2],Profession/Activity,Country/Continent\n"
        lst = []
        for e in info:
            if e["Country/Continent"] == self.country_name:
                lst.append(e)
        if len(lst) > 0:
            with open(f"{self.country_name} accounts.csv", "w") as f:
                count = 0
                for i in lst:
                    if i["Country/Continent"] == self.country_name:
                        count += 1
                        result += f"{count},{i['Rank']},{i['Username']},{i['Owner']}," \
                                  f"{i['Followers(millions)[2]']},{i['Profession/Activity']},{i['Country/Continent']}\n"
                f.write(result)
        else:
            print("Invalid country name!!!")


United_States = InstagramAccountInCountry("List of most-followed Instagram accounts.csv", "United States")
United_States.separate_accounts_by_country()
