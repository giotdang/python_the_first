
def sentence(phrase):
    interrogatives=("how","when",'what')
    capitalPhrase=phrase.capitalize()
    if phrase.startswith(interrogatives):
        return f'{capitalPhrase}?'
    else:
        return f'{capitalPhrase}.'

finalResult=[]
while True:
    user_input=input("Say somthing: ")
    if user_input== "\end":
        break
    else :
        finalResult.append(sentence(user_input))

print(" ".join(finalResult))


