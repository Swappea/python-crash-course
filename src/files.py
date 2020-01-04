# Python has functions for creating, reading, updating, and deleting files.


# open a file
myFile = open('myfile.txt', 'w')

# get info 
print(myFile.name)
print(myFile.closed)
print(myFile.mode)

# write to file
myFile.write('I love python')
myFile.write(' and Javascript')

myFile.close()

# append to file
myFile = open('myfile.txt', 'a')
myFile.write(' and I also like PHP')
myFile.close()

# read from a file
myFile = open('myfile.txt', 'r+')
text = myFile.read(100)
print(text)
