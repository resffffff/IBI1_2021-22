class staff():
    def __init__(self, first_name, last_name, location, role):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.role = role
    def check(self):
        return "His/Her full name is %s %s.\nHe/She is working in %s.\nThe role of him/her is %s." %(self.first_name, self.last_name, self.location, self.role)
# check. Log in the name of a student called Morty Race
staff1 = staff(first_name='Morty', last_name='Rice', location='the university of Edinburgh', role='student')
print(staff1.check())