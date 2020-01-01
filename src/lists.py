# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create list
# numbers = [1, 2, 3, 4]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']


# Use a constructor
# numbers2 = list((1, 2, 3, 4))

# get a value
print(fruits[1])

# length
print(len(fruits))

# append to list
fruits.append('Mangos')

# remove
fruits.remove('Oranges')

# insert
fruits.insert(2, 'Strawberries')

# change value
fruits[0] = 'Bluberries'

# remove with pop
fruits.pop(3)

# reverse
fruits.reverse()

# sort
fruits.sort()

# reverse sort
fruits.sort(reverse=True)

print(fruits)