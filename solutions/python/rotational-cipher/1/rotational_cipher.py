def rotate(text, key):
    alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    cipherdict={}
    ciphered=""
    for index,e in enumerate(alphabet):
        if index<26-key:
            cipherdict[e]=alphabet[index+key]
        if index>=26-key:
            cipherdict[e]=alphabet[index-(26-key)]
    for char in text:
        if char in alphabet or char.lower() in alphabet:
            if char in alphabet:
                ciphered+=cipherdict[char]
            if char not in alphabet:
                ciphered+=cipherdict[char.lower()].upper()
        if char not in alphabet and char.lower() not in alphabet:
            ciphered+=char
    return ciphered