import csv


class DepartmentEmployees:
    def __init__(self, department_info_path, employees_info_path):
        self.department_info_path = department_info_path
        self.employees_info_path = employees_info_path

    def get_department_data_with_dict(self):
        try:
            with open(self.department_info_path) as csv_file:
                csv_reader = csv.DictReader(csv_file)
                return [row for row in csv_reader]
        except (FileNotFoundError, UnicodeDecodeError) as e:
            print(e)

    def get_employees_data_with_dict(self):
        try:
            with open(self.employees_info_path) as csv_file:
                csv_reader = csv.DictReader(csv_file)
                return [row for row in csv_reader]
        except (FileNotFoundError, UnicodeDecodeError) as e:
            print(e)

    def department_employees(self):
        depart = self.get_department_data_with_dict()
        empl = self.get_employees_data_with_dict()
        result = ""
        with open("department_employees.csv", "w") as f:
            result += 'Employee ID,DOB,DOJ,Department_name\n'
            for i in empl:
                for e in depart:
                    if i["Department_ID"] == e["Department_ID"]:
                        depart_name = e["Department_Name"]
                result += f"{i['Employee ID']},{i['DOB']},{i['DOJ']},{depart_name}\n"
            f.write(result)


dep_emp = DepartmentEmployees("Department_Information.csv", "Employee_Information.csv")

dep_emp.department_employees()
