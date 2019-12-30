import json
from difflib import get_close_matches

def translate(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys())) > 0 :
        yn=input("Did u mean %s instead? Enter Y for Yes and N for No" % get_close_matches(word,data.keys())[0])
        if yn=="Y":
            return data[get_close_matches(word,data.keys())[0]]
        elif yn=="N":
            return "The word doesn't exists in dictionary."
        else :
            return "We didn't understand ur entry."
            
    else:
        return "The word does't exists in the dictionary"

data=json.load(open("data.json"))
word=input("Enter word :")
output=translate(word)

if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)