def is_pangram(sentence):
    latin=["q","w","e","r","t","y","u","i","o","p","l","k","j","h","g","f","d","s","a","z","x","c","v","b","n","m"]

    for char in latin:
        if char not in sentence and char.upper() not in sentence:
            return False
    return True