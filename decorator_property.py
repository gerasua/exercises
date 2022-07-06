# Python Oriented Object
#

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Gerardo', 'Suarez')

print(emp_1.first)
print(emp_1.last)
print(emp_1.email)
print(emp_1.fullname())