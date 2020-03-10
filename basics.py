import datetime
x = datetime.datetime.now()
print("Current date and Time is" , x)

# dir(datatype) can give the functions applicable using that datatype
# help(datatype.functionName can give you the documentation of that function
# dir(__builtins__) to know the built in funtions of python

student_grades=[9.8,8.3,10]

my_sum = sum(student_grades)
length = len(student_grades)
mean = my_sum/length
print("total sum",my_sum,"mean is", mean)

# { } is used to define dictionary 
# x = {"Hello": 1, "World": 2}

x = {"Hello": 1, "World": 2}
print(x)

# ( ) is used for defining tuples and ALSO tuples are immutable while list are mutable i.e. you can add more items to the list 
# using append() method
# x = (1,2,3) here, x.append(4) will not work
# x = [1,2,3,] here, x.append(4) will work

day_temperatures = {'morning': (1.2,2.1,1.12), 'noon': (2.2,22.2,34.1), 'evening': (3.4,4.3,1.0)}

""" Summary: Integers, Floats, Lists, Dictionaries, Tuples, dir, help
In this section you learned that:

Integers are for representing whole numbers:

rank = 10
eggs = 12
people = 3
Floats represent continuous values:

temperature = 10.2
rainfall = 5.98
elevation = 1031.88
Strings represent any text:

message = "Welcome to our online shop!"
name = "John"
serial = "R001991981SW"
Lists represent arrays of values that may change during the course of the program:

members = ["Sim Soony", "Marry Roundknee", "Jack Corridor"]
pixel_values = [252, 251, 251, 253, 250, 248, 247]
Dictionaries represent pairs of keys and values:

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
volcano_elevations = {"Glacier Peak": 3213.9, "Rainer": 4392.1}
Keys of a dictionary can be extracted with:

phone_numbers.keys()
Values of a dictionary can be extracted with:

phone_numbers.values()
Tuples represent arrays of values that are not to be changed during the course of the program:

vowels = ('a', 'e', 'i', 'o', 'u')
one_digits = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
To find out what attributes a type has:

dir(str)
dir(list)
dir(dict)
To find out what Python builtin functions there are:

dir(__builtins__)
Documentation for a Python command can be found with:

help(str)
help(str.replace)
help(dict.values)

To clear the python terminal shell, press ctrl + l
To clear the termial shell, write clear
If you want to go to the terminal shell again, write exit() in python shell
 """

# workdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]
# weekend = ["Sat", "Sun"]
# workdays.append(weekend[0])

workdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]
weekend = ["Sat", "Sun"]
workdays.append(weekend[0])
print("After append",workdays)

# To print the portion of the list use list[index_number_start:index_number_end] 
 # NOTE : that upper limit is not included in i.e. index_number_end is not included in the above function 
 # NOTE : Slicing or indexing or __getitem__ cannot be used directly on dictionary and it forces you to access the data using 
 # key only i.e. dictName["key"]

print("From 1 to 4 ",workdays[1:4])

# if you want to print from start index 0 then you can simple even write listName[:index_number_end] 
print("From start to 5",workdays[:5])

# if you want to print from index n upto the end then you can simple even write listName[index_number_start:] 
print("From 2 to the end",workdays[2:])

# for printing directly the value at the last index of the list use listName[-1] and similarly for last second we can use -2 and so on
print("Use -1 to get the last index value of the list", workdays[-1])

print("Slicing -2:",workdays[-2:])

# use negative slicing accurately or you might get empty list as result
print("Slicing -2:-4",workdays[-2:-4])

print("Slicing -4;-2",workdays[-4:-2])


# Accessing string by index character stored in a list and accessing that list also using index count i.e. listName[][]
myList= ["MacBook",1,2,"World","Python"]
print("Accessing String index character after accessing list ", myList[0][3], myList[-1][-1])

# Complex accessing 
print(myList[-2:-1][-1][-1])

"""
Summary: Positive/Negative Indexes, Slicing
In this section you learned that:

Lists, strings, and tuples have a positive index system:

["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
   0      1      2      3      4      5      6
And a negative index system:

["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
  -7     -6     -5     -4     -3     -2     -1
In a list, the 2nd, 3rd, and 4th items can be accessed with:

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[1:4]
Output: ['Tue', 'Wed', 'Thu']
First three items of a list:

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[:3]
Output:['Mon', 'Tue', 'Wed'] 
Last three items of a list:

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[-3:]
Output: ['Fri', 'Sat', 'Sun']
Everything but the last:

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[:-1] 
Output: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'] 
Everything but the last two:

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[:-2] 
Output: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'] 
A single in a dictionary can be accessed using its key:

phone_numbers = {"John Smith":"+37682929928","Marry Simpons":"+423998200919"}
phone_numbers["Marry Simpsons"]
Output: '+423998200919'
"""
# defining function using def key word i.e. def fun(variableName): and make sure of indentation 

def mean(value):
    if type(value) == dict:
        #can ene use isinstance(value, dict)
        value = value.values()
    result_mean = sum(value) / len(value)
    return result_mean

print(mean([1,5,8,0,6,3,7]))

print(mean(day_temperatures["morning"]))

# None is an specific object in Python which means nothing like null in JAVA

def function(value):
    if value.__len__() <=8:
        return False
    else:
        return True

user_input = input("Enter Password")
print(function(user_input))

def temp(value):
    if value > 8:
        return "Hot"
    elif value >= 2 and value <= 8:
        return "Warm"
    else:
        return "Cold"

user_input = float(input("Enter Temperature"))
print(temp(user_input))


user_input = input("enter your name")
message = "hello %s" %user_input.capitalize()
# or in python 3.6 we can write
# message = f"Hello {user_input}!"
print(message)

name = input("first name: ")
lastName = input("last Name: ")

message = "Hello %s %s" % (name, lastName)
message = f"Hello {name} {lastName}"
print(message)


#for name in names: 

colors = [11, 34, 98, 43, 45, 54, 54]
for each in colors:
    if each > 50:
        print(each)

student_grades = {"Marry": 9.1, "Harry": 10, "Jarry": 8}

for grades in student_grades.items():
    print(grades)

# for grades in student_grades.values(): 
#   print(grades)

# for grades in student_grades.keys(): 
#   print(grades)

for pair in student_grades.items():
    print(f"{pair[0]} got {pair[1]} grades out of 10") 
    #print("{} got {} grades".format(pair[0], pair[1]))
    #print("%s got %s grades" %(pair[0],pair[1]))

for key,value in student_grades.items():
    print(key,"got",value)
    #print("{} got {} marks".format(key,value))
    #print(f"{key} got {value} marks")
    #print("%s got %s marks" %(key,value))

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for value in phone_numbers.values():
    print(value.replace("+","00"))