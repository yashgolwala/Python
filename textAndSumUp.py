def check(list):
    new_list = [float(var) for var in list]
    return sum(new_list)
    
list = ['1.2', '2.6', '3.3']
print(check(list))