class employee:
    increment = 1.5
    number_of_employee = 0

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        employee.number_of_employee += 1

    def increase(self):
        self.salary = int(self.salary * employee.increment)

    @classmethod
    def multiply_salary(cls, amount):
        cls.increment = amount

    @classmethod
    def from_string_to_value(cls, emp_str):
        fname, lname, salary = emp_str.split("-")
        return cls(fname, lname, int(salary))

#now this programmer class will do everything same as employee class
class programmer(employee):

    def __init__(self, fname, lname, salary, programming_lang, exp):
        super().__init__(fname,lname,salary)
        self.programming_language=programming_lang
        self.exp=exp

    def increase(self):
        self.salary = int(self.salary * (employee.increment + 0.5))

musk = programmer("Elon","musk", 40000, "java", "10 years")
print(musk.lname)
print(musk.__dict__)

print(f"number of employee {employee.number_of_employee}")

gautam = employee("Aayush", "Gautam", 40000)
nitesh = employee("Nitesh", "Bhandari", 4000000)
rikesh = employee("Rikesh", "Karki", 400000)

print(f"number of employee {employee.number_of_employee}")

# when you don't use the __inint__(self) to create a fuction then you ahve to type like this
# gautam.fname = "Aayush"
# gautam.lname = "Gautam"
# gautam.salary = 40000
#
# nitesh.fname = "Nitesh"
# nitesh.lname = "Bhandari"
# nitesh.salary = 400000
#
# rikesh.fname  = "Rikesh"
# rikesh.lname = "Karki"
# rikesh.salary = 400000


# print(type(nitesh.salary))
# print(type(gautam))
# print(gautam, nitesh, rikesh)

print(gautam.__dict__)

print(gautam.salary)
gautam.increase()
print(gautam.salary)

print(musk.salary)
musk.increase()
print(musk.salary)

# to test @classmethod

print(nitesh.salary)
"""
 Now as 'multiply_salary' is in @classmethode
  so it will change something in class that  i have declared it to..
 for example here the value of increment by 'cls.increment'
"""
print(f"increment value:{employee.increment}")
employee.multiply_salary(2)  # changes the value of increment in class employee
print(f"increment value:{employee.increment}")
nitesh.increase()
print(f"after changing value of increment:{nitesh.salary}")

# trying the from_string_to_value

krish = employee.from_string_to_value("Krish-Dunghel-57868")

print(employee.number_of_employee)

print(krish.__dict__)
print(type(krish.salary))


print(help(musk))

