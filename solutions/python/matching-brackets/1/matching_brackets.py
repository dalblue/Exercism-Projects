#(is_paired("{[)][]}")
#(is_paired("(((185 + 223.85) * 15) - 543)/2")
def is_paired(input_string):
    bracketleft=["{","[","("]
    bracketright=["}","]",")"]
    bracketdict={")":"(",
                 "}":"{",
                 "]":"["}
    brackets=[]
    for char in input_string:
        if char in bracketleft:
            brackets.append(char)
        elif char in bracketright:
            if not brackets or bracketdict[char]!=brackets.pop():
                return False
    return not brackets