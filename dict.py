youngDict = {
    'lol': ['lmao', 18], 
    'lmao': ['laughing', 40],
    'ffs': ['goddamnit', 40],
    'goddamnit': ['gosh darn it', 60],
    'doodoo': ['poo', 6],
    'poo': ['poop', 8],
    'poop': ['crap', 11],
    'crap': ['shit', 15],
    'peepee': ['weiner', 10],
    'weiner': ['penis', 14],
    'penis': ['dick', 17],
    'dick': ['no no area', 60],
    'daddy': ['dad', 9],
    'dad': ['father', 30],
    'mama': ['mommy', 4],
    'mommy': ['mom', 9],
    'mom': ['mother', 30],
    'grownup': ['adult', 13],
    'meanie': ['bully', 9],
    'wee': ['pee', 7],
    'pee': ['piss', 11],
    'piss': ['urinate', 25],
    'yummy': ['yum', 6],
    'yum': ['tasty', 13],
    'tasty': ['delicious', 18],
    'grandpa': ['grandfather', 18],
    'grandma': ['grandmother', 18]
}

oldDict = {}
for key in youngDict.keys():
    oldDict[(youngDict.get(key))[0]] = [key, (youngDict.get(key))[1]]
    
youngDict['<3']=['love', 40]
youngDict[':)']=['happy', 40]
youngDict[':(']=['sad', 40]

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