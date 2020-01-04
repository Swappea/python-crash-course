# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# create class


class User:
    # constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} years old'

    def has_birthday(self):
        self.age += 1


# extend class

class Customer(User):
    # constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} years old and my balance is {self.balance}'

# init user object
brad = User('Brad Traversy', "test@test.com", 31)

# init customer object
janet = Customer('Janet', 'test@test.com', 35)

# can access parent class method
janet.has_birthday() 

# accessing parents overriden method
janet.set_balance(25000)


brad.has_birthday()
print(brad.greeting())
print(janet.greeting())

