

# Single Inheritance : only 1 child

# Base or Super class. Note object in bracket.
# (Generally, object is made ancestor of all classes)
# In Python 3.x "class Person" is
# equivalent to "class Person(object)"


class Person(object):
    def __init__(self, name):
        self.name = name

    def displayname(self):
        print("Person Name is ", self.name)


class Employee(Person):
    def __init__(self, name, id):
        # self.name = name
        # invoking the __init__ of the parent class
        # Person.__init__(self, name)
        super().__init__(name)
        self.id = id
        pass

    def displayname(self):
        print("Employee Name is", self.name)


person1 = Person('Trishala')
person1.displayname()
person2 = Employee('Trisha', 1)
person2.displayname()
