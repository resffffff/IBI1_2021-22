class Staff:
    def __init__(self,first_name,last_name,location,role):
        self.first_name=first_name
        self.last_name = last_name
        self.location=location
        self.role=role
a=input()
b=input()
c=input()
d=input()
staff=Staff(a,b,c,d)
print(staff.first_name,staff.last_name,'  ',staff.location,'  ',staff.role)
