class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return f"Name: {self.name} AGE: {self.age} years old."
    

class Licence:
    def __init__(self, licence_number, issue_date):
        self.licence_number = licence_number
        self.issue_date = issue_date

    def display_info(self):
        return f"Licence Number: {self.licence_number}, Issue Date: {self.issue_date}"
    

class LMS:
    def __init__(self):
        self.Details = {}

    def add_people_licence(self, peole_obj, licence_obj):
        find_current_length = len(self.Details) + 1

        new_obj = {
            "people" : peole_obj,
            "license": licence_obj,
            "approved": False 
        }

        self.Details[find_current_length]= new_obj

    def list_data(self):
        for key, value in self.Details.items():
            people_info = value["people"].display_info()
            licence_info = value["license"].display_info()
            approved_status = "Approved" if value["approved"] else "Not Approved"
            print(f"Key: {key}, {people_info}, {licence_info}, Status: {approved_status}")


LMS_obj = LMS()

p1 = People("Rujal", 25)
l1 = Licence("123456", "2016-01-02")


LMS_obj.add_people_licence(p1,l1)
LMS_obj.add_people_licence(p1,l1)
LMS_obj.add_people_licence(p1,l1)
LMS_obj.add_people_licence(p1,l1)

LMS_obj.list_data()






