#create an object for file and open the file located in the same directory
myFile = open("fruit.txt")

# read() function is used to read data from the given file.
content = myFile.read()

print(type(myFile))
myFile.close()
print(content)

# Can also use with inline function statment
with open("fruit.txt") as myFile:
    content = myFile.read()
print(content)

#For writing in a file, change mode of the file tp "w" in open function and use file.write("") function
with open("vegetable.txt", "w") as myFile:
    myFile.write("Tomatoes")

with open("first.txt", "w") as myFile:
    file = open("fruit.txt")
    content = file.read()
    myFile.write(content[:90])

# use seek(0) to bring the cursor back to the starting position of the file

#import sys and sys.builtin_module_names for getting the in built modules names of sys library

# time.sleep(number_of_seconds) to delay the output on the screen

import time
import os

while True:
    if os.path.exists("frut.txt"):
        with open("fruit.txt") as file:
            print(file.read())
    else:
        print("Given file does not exists")
    time.sleep(5)

    