# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create tuple
fruits = ('Apples', 'Oranges', 'Grapes')
# fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

# single value needs trailing comma
fruits2 = ('Apples',)

# get a value
print(fruits[1])

# item assignment is not supported in tuple
# fruits[0] = 'pears'

# delete tuple
del fruits2

# length
print(len(fruits))

# A Set is a collection which is unordered and unindexed. No duplicate members.

# create a set
fruits_set = {'Apples', 'Oranges', 'Mango'}

# check if in set
print('Apples' in fruits_set)

# add to set
fruits_set.add('Pears')

# adding duplicates. wont give any error.
fruits_set.add('Apples')

# remove from set
# fruits_set.remove('Apples')

# clear set
# fruits_set.clear()

# delete
# del fruits_set

print(fruits_set)