def sentence_maker(phrase):
    interrogatives = ("why","how","what")
    capitalized = phrase.capitalize()
    #startswith function checks whether the string starts with the given values
    if phrase.startswith(interrogatives): 
        return f"{capitalized}?"
    else:
        return f"{capitalized}."

conversation = []

while True:
    userInput = input("Say something: ")
    if userInput == "\end":
        if conversation.__len__() >= 0:
            break
    else:
        conversation.append(sentence_maker(userInput))

print(" ".join(conversation))
