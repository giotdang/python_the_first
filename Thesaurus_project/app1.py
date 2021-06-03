
import json #to load and handle a json file
from difflib import get_close_matches
data=json.load(open("data.json"))
keys=data.keys()
def definition(word):
    w=word.lower()
    w1=word.title()
    w2=word.upper()
    if w in data:
        return data[w]
    elif w1 in data:
        return data[w1]
    elif w2 in data:
        return data[w2]
    elif len(get_close_matches(w,keys))>0:
        confirm= input(f"Did you mean {get_close_matches(w,keys)[0]} instead? Press Y/N for Yes/No: ").lower()
        if confirm =="y":
            return data[get_close_matches(w,keys)[0]]
        elif confirm =="n":
            return "Word doesn't exist"
        else:
            return "We didn't understand your query"
    else:
        return "Word doesn't exist"
while 1:
    word=input("Enter your word: ")
    output=definition(word)
    if type(output)== list:
        index=1
        for item in output:
            print(f"{index}.{item}")
            index+=1
    else:
        print(output)
