import json
from difflib import get_close_matches

# converts file into dictionary 
data = json.load(open("data.json"))

class words():
    def __init__(self,word):
        self.word=word

    def search_word(self):
        self.word=self.word.lower()
        if self.word in data:
            return data[self.word]
        elif len(get_close_matches(self.word, data.keys()))>0:

            yn=input("Did you mean %s instead? Enter y if yes, Enter n if no "% get_close_matches(self.word, data.keys())[0]).lower()

            if yn == "y":
                return data[get_close_matches(self.word,data.keys())[0]]
            elif yn == "n":
                return ("Word doesn't exist please check it ")

            else:
                return "Enter a valid input"

        else:
            return "Please check the word again"

word = words(input("enter a word: "))

if type(word)==list:
    for item in word:
        print(item)
else:
    print(word.search_word())