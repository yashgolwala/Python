#give a string character and filepath as input paramters to a function
# and get occurences of that character as an output of that function

def process(character, filepath):
    myfile = open(filepath)
    content = myfile.read()
    myfile.close()
    count = content.count(character)
    return count

a = input("Enter Character")
b = input("File name")

print(process(a,b))