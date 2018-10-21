import dict
import re
import random

def lookUp(word, age):
    """Returns a word, based on given word, corresponding to given age"""

    # Handle small children
    if age<3:
        babyTalk = ["goo", "ga", "waa", "WAA", "waah"]
        return babyTalk[random.randint(0, len(babyTalk)-1)]

    # If 3 or older, use the actual translation dictionary
    return dict.dictLookup(word,age)

def stringProcessor(text, age):
    """Returns processed text corresponding to given age"""
    inarr = re.findall(r"[\w']+|[.,!?;]", text)
    outarr = []
    text = ""
    for word in inarr:
        outarr.append(lookUp(word, age))
    for word in outarr:
        if (word != ',' and word != '.') and text != "":
            text = text + ' ' + word
        else:
            text = text + word
    x = text.capitalize()
    return x
