def is_isogram(phrase):
    punctuation=["-"," "]
    seenlist=[]
    isiso=True
    for char in phrase:
        if char not in punctuation:
            if char.lower() not in seenlist:
                seenlist.append(char.lower())
            elif char.lower() in seenlist:
                isiso=False
    return isiso
