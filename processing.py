import dict
import re

def lookUp(word, age):
    """Returns a word, based on given word, corresponding to given age"""
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
