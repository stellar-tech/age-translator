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
    'meanie': ['jerk', 10],
    'jerk': ['asshole', 16],
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
    'phone': ['telephone', 70],
    'doggy': ['dog', 10],
    'kitty': ['cat', 10],
    'birdie': ['bird', 10],
    'bunny': ['rabbit', 10],
    'iirc': ['if I recall correctly', 40],
    'email': ['AOL', 50]
}

oldDict = {}
for key in youngDict.keys():
    oldDict[(youngDict.get(key))[0]] = [key, (youngDict.get(key))[1]]

# One-way young-to-old
youngDict['bruh']=['bro', 18]
youngDict['bro']=['brother', 25]
youngDict['fam']=['friends', 18]
youngDict['bae']=['baby', 25]
youngDict['turnt']=['crazy', 16]
youngDict['uber']=['taxi', 60]
youngDict['lyft']=['taxi', 60]
youngDict['computer']=['machine', 62]
youngDict['signature']=['John Hancock', 60]
youngDict['trouble']=['a pickle', 73]
youngDict['candy']=['hard candy', 65]
youngDict['hackathon']=['computer party', 40]
youngDict['nickelback']=['the music of Satan', 63]
youngDict['twitter']=['facebook', 65]
youngDict['snapchat']=['facebook', 65]
youngDict['instagram']=['facebook', 65]
youngDict['linkedin']=['facebook', 65]
youngDict['tumblr']=['facebook', 65]
youngDict['xbox']=['nintendo', 65]
youngDict['playstation']=['nintendo', 65]
youngDict['programming']=['hacking', 50]
youngDict['hacked']=['possessed', 60]

def dictLookup(word, age):
    check = ''
    uppercase = (word[0].isupper())
    while check != word:
        check = word
        key = word.lower()
        if youngDict.get(key) != None:
            if (youngDict.get(key))[1] <= age:
                word = (youngDict.get(key))[0]
                key=word.lower() # Preserve ability to check oldDict on second pass
        if oldDict.get(key) != None:
            if (oldDict.get(key))[1] > age:
                word = (oldDict.get(key))[0]
    if uppercase:
        word=word[0].upper()+word[1:]
    return word