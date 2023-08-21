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

    #here to use .format, '{}' is necessary
    def __repr__(self):
        return '{},{},{}'.format(self.fname,self.lname,self.salary)

    def __str__(self):
        return "the name of employee is {}".format(self.fname)

print(f"number of employee {employee.number_of_employee}")

gautam = employee("Aayush", "Gautam", 68930)
nitesh = employee("Nitesh", "Bhandari", 47453)
rikesh = employee("Rikesh", "Karki", 3454)


print(repr(gautam))
print(gautam)