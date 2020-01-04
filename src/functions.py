# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

# create function


def sayHello(name, age=30):
    print(f'Hello {name} and my age is {age}')

# sayHello('John')
# sayHello('Jane', 25)

# return values


def getSum(num1, num2):
    total = num1 + num2
    return total

# num = getSum(3, 4)
# print(num)

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions


getSumL = lambda num1, num2 : num1 + num2
print(getSumL(10, 3))