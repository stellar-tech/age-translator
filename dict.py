youngDict = {
    'lol': ['lmao', 18], 
    'lmao': ['laughter', 40]
}

oldDict = {}
for key in youngDict.keys():
    oldDict[(youngDict.get(key))[0]] = [key, (youngDict.get(key))[1]]

def dictLookup(word, age):
    check = ''
    word = word.lower()
    while check != word:
        check = word
        if youngDict.get(word) != None:
            if (youngDict.get(word))[1] <= age:
                word = (youngDict.get(word))[0]
        if oldDict.get(word) != None:
            if (oldDict.get(word))[1] > age:
                word = (oldDict.get(word))[0]
    return word