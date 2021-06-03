
def sentence(phrase):
    interrogatives=("how","when",'what')
    capitalPhrase=phrase.capitalize()
    if phrase.startswith(interrogatives):
        return f'{capitalPhrase}?'
    else:
        return f'{capitalPhrase}.'

finalResult=[]
#while True:
#    user_input=input("Say somthing: ")
#    if user_input== "\end":
#        break
#    else :
#        finalResult.append(sentence(user_input))

print(" ".join(finalResult))
txt = "5-4|2-3|10|4-5"

x = txt.split("|")
i=0
for i in range(len(x)):
    x[i]=x[i].split("-")
    print(x[i])

rollList=[]
for item in x:
    rollList.extend(item)

rollList=[int(i) for i in rollList]

print(x)
print(rollList)


