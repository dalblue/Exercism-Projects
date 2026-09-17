def steps(number):
    steps=0
    if number<1:
        raise ValueError("Only positive integers are allowed")
    while number!=1:
        if number%2==0:
            number=int(number/2)
            steps+=1
            if number==1:
                break
        if number%2==1:
            number=int((number*3)+1)
            steps+=1
            if number==1:
                break
    return steps