# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# create dict
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 40
}

# use a constructor
# person_1 = dict(first_name='Jane', last_name='Doe', age=30)

# get value
print(person['first_name'])
print(person.get('last_name'))

# add key value
person['phone'] = '555-555-5555'

# get dict keys
print(person.keys())

# get dict items
print(person.items())

# copy dict
person2 = person.copy()
person2['city'] = 'Oregon'

# remove item
del(person['age'])
person.pop("last_name")

# clear
person2.clear()

# length
print(len(person))

# list of dict
people = [
    {
        'name': 'John',
        'age': 30
    },
    {
        'name': 'Jane',
        'age': 50
    },
    {
        'name': 'Sara',
        'age': 12
    }
]
print(people[0]['name'])
print(person, type(person))
print(person2, type(person2))
