def is_valid(isbn):
    multiplier=10
    totalbeforemod=0
    if len(isbn)<10:
        return False
    if len(isbn)>10 and "-" not in isbn:
        return False
    for char in isbn:
        if char!="-" and char!="X" and char not in["1","2","3","4","5","6","7","8","9","0"]:
            return False
        if char!="-" and char!="X":
            totalbeforemod+=int(char)*multiplier
            multiplier-=1
        if char=="X":
            totalbeforemod+=10
    return totalbeforemod%11==0
