youngDict = {
    'lol': ['lmao', 18],
    'lmao': ['laughing', 40],
    'otw': ['on the way', 40],
    'ffs': ['goddamnit', 40],
    'yolo': ['you only live once', 40],
    'tbh': ['to be honest', 30],
    'idgaf': ["I don't give a fuck", 16],
    'ghosted': ['disappeared', 35],
    'goddamnit': ['gosh darn it', 60],
    'weed': ['pot', 30],
    'pot': ['marijuana', 45],
    'marijuana': ["Devil's lettuce", 80],
    'doodoo': ['poo', 6],
    'poo': ['poop', 8],
    'poop': ['crap', 11],
    'crap': ['shit', 15],
    'dm': ['message', 25],
    'message': ['fax', 60],
    'fax': ['telegram', 85],
    'fortnite': ['video games', 32],
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
    'grandma': ['grandmother', 18],
    'trolling': ['pranking', 30],
    'strangest': ['darndest', 75],
    'dating': ['courting', 70],
    'phone': ['telephone', 70]
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