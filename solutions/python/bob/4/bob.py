def response(hey_bob):
    lower=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    upper=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    punctuation=["'",".",",","-","?","!"]
    numbers=["1","2","3","4","5","6","7","8","9","0"]
    def isyelling(hey_bob):
        hasupper=False
        haslower=False
        for char in upper:
            if char in hey_bob:
                hasupper=True
                break
        for char in lower:
            if char in hey_bob:
                haslower=True
                break
        if hasupper and not haslower:
            return True
        return False

    def issilent(hey_bob):
        for char in lower:
            if char in hey_bob:
                return False
        for char in upper:
            if char in hey_bob:
                return False
        for char in punctuation:
            if char in hey_bob:
                return False
        for char in numbers:
            if char in hey_bob:
                return False
        return True
                
    def isquestion(hey_bob):
        if issilent(hey_bob)==True:
            return False
        for char in hey_bob[-1::-1]:
            if char==" ":
                pass
            if char=="?": 
                return True
            if char not in ("?"," "):
                return False
    bobsays=""
    if not isyelling(hey_bob) and isquestion(hey_bob):
        bobsays="Sure."
    elif isyelling(hey_bob) and not isquestion(hey_bob):
        bobsays="Whoa, chill out!"
    elif isyelling(hey_bob) and isquestion(hey_bob):
        bobsays="Calm down, I know what I'm doing!"
    elif issilent(hey_bob):
        bobsays="Fine. Be that way!"
    else:
        bobsays="Whatever."

    return bobsays