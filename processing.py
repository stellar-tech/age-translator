import dict

def lookUp(word, age):
    """Returns a word, based on given word, corresponding to given age"""
    return dict.dictLookup(word,age)

def stringProcessor(text, age):
    """Returns processed text corresponding to given age"""
    inarr = text.split()
    outarr = []
    for word in inarr:
        outarr.append(lookUp(word, age))
    return ' '.join(word for word in outarr).capitalize()