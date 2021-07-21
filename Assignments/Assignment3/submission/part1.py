def adddel(word,delt,rep):
    """
    Executes the add-delete rule word(delt,rep)
    i.e. deletes the last "delt" letters and
    appends the string "rep"
    """
    if delt == 0:
        return (word + rep)
    return (word[:-delt] + rep)

def genv(word,clas):
    """
    For verbs:
    Two arguments 'word' and 'class'.
    Class 1: play, walk
    Class 2: dance, mince
    Class 3: marry, carry
    Class 4: take, shake
    Class 5: say, lay
    Class 6: speak, break
    Class 7: catch, teach
    Class 8: set, put
    Class 9: plan, ban
    Class 10: mean, learn
    Class 11: sleep, creep
    Class 12: feel, kneel
    Class 13: refer, infer
    Class 14: watch, reach
    Class 15: focus, gas
    """
    
    if clas == 1:
        rules = [(0,''), (0,'s'), (0,'ing'), (0,'ed'), (0,'ed')]
    elif clas == 2:
        rules = [(0,''), (0,'s'), (1,'ing'), (0,'d'), (0,'d')]
    elif clas == 3:
        rules = [(0,''), (1,'ies'), (0,'ing'), (1,'ied'), (1,'ied')]
    elif clas == 4:
        rules = [(0,''), (0,'s'), (1,'ing'), (3,'ook'), (0,'n')]
    elif clas == 5:
        rules = [(0,''), (0,'s'), (0,'ing'), (1,'id'), (1,'id')]
    elif clas == 6:
        rules = [(0,''), (0,'s'), (0,'ing'), (3,'oke'), (3,'oken')]
    elif clas == 7:
        rules = [(0,''), (0,'es'), (0,'ing'), (4,'aught'), (4,'aught')]
    elif clas == 8:
        rules = [(0,''), (0,'s'), (0,'ting'), (0,''), (0,'')]
    elif clas == 9:
        rules = [(0,''), (0,'s'), (0,'ning'), (0,'ned'), (0,'ned')]
    elif clas == 10:
        rules = [(0,''), (0,'s'), (0,'ing'), (0,'t'), (0,'t')]
    elif clas == 11:
        rules = [(0,''), (0,'s'), (0,'ing'), (3,'ept'), (3,'ept')]
    elif clas == 12:
        rules = [(0,''), (0,'s'), (0,'ing'), (3,'elt'), (3,'elt')]
    elif clas == 13:
        rules = [(0,''), (0,'s'), (0,'ring'), (0,'red'), (0,'red')]
    elif clas == 14:
        rules = [(0,''), (0,'es'), (0,'ing'), (0, 'ed'), (0,'ed')]
    elif clas == 15:
        rules = [(0,''), (0,'ses'), (0, 'sing'), (0,'sed'), (0,'sed')]
    
    forms = map(lambda p : adddel(word, p[0], p[1]),rules)
    return list(forms)

def genn(word,clas):
    """
    For nouns:
    Two arguments 'word' and 'class'.
    Class 1: house, table
    Class 2: watch, tomato
    Class 3: leaf, wolf
    Class 4: sheep, fish
    Class 5: index, matrix
    Class 6: axis, crisis
    Class 7: radius, syllabus
    Class 8: alga, alumna
    Class 9: medium, stratum
    Class 10: lemma, stigma
    Class 11: louse, mouse
    Class 12: tableau, bureau
    Class 13: pharynx, larynx
    Class 14: sky, cherry
    """
    
    if clas == 1:
        rules = [(0,''), (0,'s')]
    elif clas == 2:
        rules = [(0,''), (0,'es')]
    elif clas == 3:
        rules = [(0,''), (1,'ves')]
    elif clas == 4:
        rules = [(0,''), (0,'')]
    elif clas == 5:
        rules = [(0,''), (2,'ices')]
    elif clas == 6:
        rules = [(0,''), (2,'es')]
    elif clas == 7:
        rules = [(0,''), (2,'i')]
    elif clas == 8:
        rules = [(0,''), (0,'e')]
    elif clas == 9:
        rules = [(0,''), (2,'a')]
    elif clas == 10:
        rules = [(0,''), (0,'ta')]
    elif clas == 11:
        rules = [(0,''), (4,'ice')]
    elif clas == 12:
        rules = [(0,''), (0,'x')]
    elif clas == 13:
        rules = [(0,''), (1,'ges')]
    elif clas == 14:
        rules = [(0,''), (1,'ies')]
    
    forms = map(lambda p : adddel(word, p[0], p[1]),rules)
    return list(forms)

def getforms(word,clas,pos):
    """
    Three arguments 'word', 'class' and 'pos'.
    Calls genv() for verbs and genn() for nouns.
    """
    if pos == 'v':
        return genv(word,clas)
    elif pos == 'n':
        return genn(word,clas)

word = input("Enter the word: ")
pos = input("Enter part of speech [n|v]: ")
clas = int(input("Enter class number: "))

print("The forms of the word are:", getforms(word,clas,pos))
