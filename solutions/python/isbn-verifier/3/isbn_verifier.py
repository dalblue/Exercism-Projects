def is_valid(isbn):
    multiplier=10
    totalbeforemod=0
    if len(isbn)<10:
        return False
    if len(isbn)>10 and "-" not in isbn:
        return False
    for char in isbn:
        if char not in["X","-","1","2","3","4","5","6","7","8","9","0"]:
            return False
        if char not in ["X", "-"]:
            totalbeforemod+=int(char)*multiplier
            multiplier-=1
        if char=="X":
            totalbeforemod+=10
    return totalbeforemod%11==0
