
# indefinite Non default  arguments
def numOfStrings(*args):
    listt = [ str(var).upper() for var in args]
    return sorted(listt)

print(numOfStrings("Hi","How are you","ABC","abc"))