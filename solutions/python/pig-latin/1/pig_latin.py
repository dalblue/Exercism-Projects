def translate(text):
    textwords=text.split(" ")
    piglatin=""
    vowels=['a','e','i','o','u']
    for word in textwords:
        if word[0:2]=="xr" or word[0:2]=="yt" or word[0] in vowels:
            piglatin+=word
        elif word[0] not in vowels:
            if "qu" in word[0:3]:
                previous=''
                current=''
                for char in word:
                    if previous=="u":
                        piglatin+=char
                    if previous!="u":
                        previous=char
                for char in word:
                    if current!="u":
                        piglatin+=char
                        current=char
                    if current=="u":
                        break
            elif len(word)<=2 and 'y' in word:
                if word[0]=='y':
                    piglatin+=word[1]+word[0]
                if word[1]=='y':
                    piglatin+=word[1]+word[0]
            elif word[0]=='y':
                piglatin+=word[1:]+word[0]
            elif 'y' in word[1:3]:
                current=''
                for char in word:
                    if current!='y':
                        current=char
                    if current=='y':
                        piglatin+=char
                current=''
                for char in word:
                    current=char
                    if current!='y':
                        piglatin+=char
                    if current=='y':
                        break
            else:
                current=''
                for char in word:
                    if current not in vowels:
                        current=char
                    if current in vowels:
                        piglatin+=char
                current=''
                for char in word:
                    current=char
                    if current not in vowels:
                        piglatin+=char
                    if current in vowels:
                        break
        piglatin+="ay"
        if word!=textwords[-1]:
            piglatin+=' '
                
    return piglatin