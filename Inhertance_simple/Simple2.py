# parent class
class Person(object):

    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)


class Employee(Person):
    def __init__(self, idnumber, name, salary, post):
        super().__init__(idnumber, name)
        self.salary = salary
        self.post = post


p = Person('Trishala', 45)
# class Person using its instance
p.display()
