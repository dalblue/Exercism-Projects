def distance(strand_a, strand_b):
    hamdist=0
    if len(strand_a)==len(strand_b):
        for count, char in enumerate(strand_a):
            if char!=strand_b[count]:
                hamdist+=1
            else:
                pass
        return hamdist
    else:
        raise ValueError("Strands must be of equal length.")