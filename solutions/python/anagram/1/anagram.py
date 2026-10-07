def find_anagrams(word, candidates):
    anagrams=[]
    wordset=set()
    wordlist=[]
    for char in word:
        wordset.add(char.lower())
        wordlist.append(char.lower())
    for item in candidates:
        anagram=False
        candidateset=set()
        candidatelist=[]
        for char in item:
            candidateset.add(char.lower())
            candidatelist.append(char.lower())
        for char in candidatelist:
            if wordlist.count(char)==candidatelist.count(char):
                if candidateset==wordset and item.lower()!=word.lower() and len(item.lower())==len(word.lower()):
                    anagram=True
            else:
                anagram=False
                break
        if anagram:
            anagrams.append(item)
    return anagrams
