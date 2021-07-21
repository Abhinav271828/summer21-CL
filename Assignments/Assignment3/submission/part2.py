def splitpos(word,pos):
    """
    Splits word at position pos
    """
    return (word[:pos], word[pos:])

def getv(word,clas):
    """
    For verbs:
    Two arguments 'word' and 'class'.
    Returns pair (base, affix)
    """
    if word[-1:] == 's':
        if clas in [1,2,4,5,6,8,9,10,11,12,13]:
            return splitpos(word,-1)
        elif clas % 7 == 0:
            return splitpos(word,-2)
        elif clas == 3:
            return (word[:-3] + 'y', 'es')
        elif word[-3:] == 'ses':
            return splitpos(word,-3)
        else:
            return (word,'')
    elif word[-3:] == 'ing':
        if clas in [1,3,5,6,7,10,11,12,14]:
            return splitpos(word,-3)
        elif clas in [2,4]:
            return (word[:-3] + 'e', 'ing')
        else:
            return splitpos(word,-4)
    elif word[-1:] == 'd':
        if clas == 2:
            return splitpos(word,-1)
        elif clas in [1,14]:
            return splitpos(word,-2)
        elif clas == 3:
            return (word[:-3] + 'y', 'ed')
        elif clas == 5:
            return (word[:-2] + 'y', 'd')
        elif clas in [9,13,15]:
            return splitpos(word,-3)
        else:
            return (word,'')
    elif word[-1:] == 'n':
        if clas == 4:
            return splitpos(word,-1)
        elif clas == 6:
            return (word[:-4] + 'eak', 'en')
        else:
            return (word,'')
    elif word[-3:] == 'ook':
        if clas == 4:
            return (word[:-3] + 'ake', '')
        else:
            return (word,'')
    elif word[-1:] == 't':
        if clas == 7 and word[-5:] == 'aught':
            return (word[:-5] + 'atch', 't')
        elif clas == 11 and word[-3:] == 'ept':
            return (word[:-3] + 'eep', 't')
        elif clas == 12 and word[-3:] == 'elt':
            return (word[:-3] + 'eel', 't')
        elif clas == 10:
            return splitpos(word,-1)
        else:
            return (word,'')
    else:
        return (word,'')

def getn(word,clas):
    """
    For nouns:
    Two arguments 'word' and 'class'.
    Returns pair (base, affix)
    """
    if word[-1:] == 's':
        if clas == 1:
            return splitpos(word,-1)
        elif clas == 2:
            return splitpos(word,-2)
        elif clas == 6 and word[-2:] == 'es':
            return (word[:-2] + 'is', 'es')
        elif clas == 3:
            return (word[:-3] + 'f', 'es')
        elif clas == 5:
            return (word[:-4] + 'ex', 'es')
        elif clas == 13:
            return (word[:-3] + 'x', 'es')
        elif clas == 14:
            return (word[:-3] + 'y', 'es')
        else:
            return (word,'')
    elif word[-1:] == 'a':
        if clas == 9:
            return (word[:-1] + 'um', 'a')
        elif clas == 10:
            return splitpos(word,-2)
        else:
            return (word,'')
    elif word[-1:] == 'i':
        if clas == 7:
            return (word[:-1] + 'us', 'i')
        else:
            return (word,'')
    elif word[-1:] == 'e':
        if clas == 8:
            return splitpos(word,-1)
        elif clas == 11 and word[-3:] == 'ice':
            return (word[:-3] + 'ouse', '')
        else:
            return (word,'')
    elif word[-1:] == 'x':
        if clas == 12:
            return splitpos(word,-1)
        else:
            return (word,'')
    else:
        return (word,'')

def getroot(word,clas,pos):
    """
    Three arguments 'word', 'class' and 'pos'.
    Calls getv() for verbs and getn() for nouns.
    """
    if pos == 'v':
        return getv(word,clas)
    elif pos == 'n':
        return getn(word,clas)

word = input("Enter the word: ")
pos = input("Enter part of speech [n|v]: ")
clas = int(input("Enter class number: "))

print("The root-affix decomposition of the word is:", getroot(word,clas,pos))
