#Import JSON library to do manipulation over the json files. ( import json)
# After importing the json, you can load the file or data of the file using json.load() and passing file
# object into the that load function. File object can be created using open("filenamePath")

#If you want a specific word from the file, store the json.load in a varibale and access that variable like.
#for e.g. data = json.load(open("data.json")) followed by data["rain"] to get the data of rain

#use difflib library and Sequence Matcher class from that library

import json
from difflib import get_close_matches
#from autocorrect import Speller

data = json.load(open("data.json"))

def retrieve(word):
    wordLower = word.lower() #if RAin instead of rain
    wordTitle = word.title() #if Paris or any noun
    wordUpper = word.upper() #USA or like words
   # wordAutoCorrect = Speller(lang='en')
   # wordNew = Speller(wordLower)
    wordNew = get_close_matches(wordLower, data.keys(),cutoff=0.7)[0]
    if wordLower in data:
        return data[wordLower]
    elif wordTitle in data:
        return data[wordTitle]
    elif wordUpper in data:
        return data[wordUpper]
    if (wordLower.replace('.','')) in data: # For handling dots in input like U.S.A.
        return data[wordLower.replace('.','')]
    elif (wordTitle.replace('.','')) in data:
        return data[wordTitle.replace('.','')]
    elif (wordUpper.replace('.','')) in data:
        return data[wordUpper.replace('.','')]
    #elif wordNew in data:
     #   return data[wordNew]
    elif wordNew in data:
        flag = input("Did you mean " +wordNew+ " ? Yes or No ? ")
        if (flag[0]=='Y' or flag[0]=='y'):
            return data[wordNew]
        else:
            return "Word Does not exist. Try again!"
    else:
        return "Word does not exist!"


word = input("Enter Word:")
result = retrieve(word)

if type(result) == list:
    for contents in result:
        print(contents)
else:
    print(result)
