# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# core modules
import datetime
# import time
# only import particular module
# from datetime from date
from time import time

# pip modules
from camelcase import CamelCase

# import custom module
from validator import validate_email

today = datetime.date.today()
timestamp = time()
# print(timestamp)


c = CamelCase()
# print(c.hump('hello there world'))

email = "swapneshsangle1@gmail.com"
w_email = 'adssddsds'

print(validate_email(email))
print(validate_email(w_email))