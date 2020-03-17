#create a function which allows only number to be stored in a list and display

def check(list):
    new_list = [var for var in list if type(var)==int]
    return new_list

list = [99, 'no data', 95, 94, 'no data']

print(check(list))

#create a function which allows only positive number to be stored in a list and display
def check(list):
    new_list =[var for var in list if var > 0]
    return new_list

list = [-5, 3, -1, 101]
print(check(list))

#create a function which allows only positive number to be stored in a list and and stores 0 for negative number

def check(list):
    new_list = [var if var > 0 else 0 for var in list]
    return new_list
list = [-5, 3, -1, 101]
print(check(list))

def check(list):
    new_list = [var if type(var)==int else 0 for var in list]
    return new_list

list = [99, 'no data', 95, 96, 'no data']
print(check(list))