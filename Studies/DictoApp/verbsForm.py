def formsWeak(verb):
    leng = len(verb)
    pron = ['ich', 'du', 'er/sie/es', 'wir', 'ihr', 'sie/Sie']
    d = {}

    if verb[leng - 2:] == "en":
        verb = verb[:leng - 2]
        leng = len(verb)
    else:
        verb = verb[:leng - 1]
        leng = len(verb)

    if (verb[leng - 1] == "t" or verb[leng - 1] == "d" 
        or verb[leng - 3:] == "chn" or verb[leng - 3:] == "ffn"
        or verb[leng - 2:] == "dm" or verb[leng - 2:] == "gn"
        or verb[leng - 2:] == "tm"):
        d["ich"] = verb + "e"
        d["du"] = verb + "est"
        d["er/sie/es"] = d["ihr"] = verb + "et"
        d["wir"] = d["sie/Sie"] = verb + "en"
    elif (verb[leng - 1] == "ß" or verb[leng - 1] == "s" or verb[leng - 1] == "z"
        or verb[leng - 2:] == "ss"):
        d["ich"] = verb + "e"
        d["er/sie/es"] = d["ihr"] = d["du"] = verb + "t"
        d["wir"] = d["sie/Sie"] = verb + "en"
    elif verb[leng - 2:] == "er" or verb[leng - 2:] == "el":
        d["ich"] = verb + "e"
        d["du"] = verb + "st"
        d["er/sie/es"] = d["ihr"] = verb + "t"
        d["wir"] = d["sie/Sie"] = verb + "n"
    else:
        d["ich"] = verb + "e"
        d["du"] = verb + "st"
        d["er/sie/es"] = d["ihr"] = verb + "t"
        d["wir"] = d["sie/Sie"] = verb + "en"
    
    for ind in pron:
        print(ind, ": ", d[ind], " ", sep= "", end=" ")
    print()


def formsStrong(verb):
    leng = len(verb)
    pron = ['ich', 'du', 'er/sie/es', 'wir', 'ihr', 'sie/Sie']
    d = {}

    if verb[leng - 2:] == "en":
        verb = verb[:leng - 2]
        leng = len(verb)
    else:
        verb = verb[:leng - 1]
        leng = len(verb)

    if (verb[leng - 1] == "t" or verb[leng - 1] == "d" 
        or verb[leng - 1] == "a" or verb[leng - 1] == "m" 
        or verb[leng - 3:] == "chn" or verb[leng - 3:] == "ffn"
        or verb[leng - 2:] == "dm" or verb[leng - 2:] == "gn"
        or verb[leng - 2:] == "tm"):
        d["ich"] = verb + "e"
        d["du"] = verb + "est"
        d["er/sie/es"] = d["ihr"] = verb + "et"
        d["wir"] = d["sie/Sie"] = verb + "en"
    elif (verb[leng - 1] == "ß" or verb[leng - 1] == "s" or verb[leng - 1] == "z"
        or verb[leng - 2:] == "ss"):
        d["ich"] = verb + "e"
        d["er/sie/es"] = d["ihr"] = d["du"] = verb + "t"
        d["wir"] = d["sie/Sie"] = verb + "en"
    elif verb[leng - 2:] == "er" or verb[leng - 2:] == "el":
        d["ich"] = verb + "e"
        d["du"] = verb + "st"
        d["er/sie/es"] = d["ihr"] = verb + "t"
        d["wir"] = d["sie/Sie"] = verb + "n"
    else:
        d["ich"] = verb + "e"
        d["du"] = verb + "st"
        d["er/sie/es"] = d["ihr"] = verb + "t"
        d["wir"] = d["sie/Sie"] = verb + "en"

    if (verb.find("e") <= 4 or verb.find("a") <= 4 or verb.find("o") <= 4 
        or verb.find("au") <= 4):
        if verb.find("e") != -1:
            d["du"] = d["du"].replace("e", "i(e)", 1)
            d["er/sie/es"] = d["er/sie/es"].replace("e", "i(e)", 1)
        elif verb.find("a") != -1:
            d["du"] = d["du"].replace("a", "ä", 1)
            d["er/sie/es"] = d["er/sie/es"].replace("a", "ä", 1)
        elif verb.find("o") != -1: 
            d["du"] = d["du"].replace("o", "ö", 1)
            d["er/sie/es"] = d["er/sie/es"].replace("o", "ö", 1)
        elif verb.find("au") != -1:
            d["du"] = d["du"].replace("au", "äu", 1)
            d["er/sie/es"] = d["er/sie/es"].replace("au", "äu", 1)

    for ind in pron:
        print(ind, ": ", d[ind], " ", sep= "", end=" ")
    print()

#while True:
 #   formsStrong(input().strip())
formsWeak("kommen")