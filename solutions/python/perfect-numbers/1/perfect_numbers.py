def classify(number):
    """ A perfect number equals the sum of its positive divisors.
    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number<=0:
        raise ValueError("Classification is only possible for positive integers.")
    factorlist=[]
    for num in range(1,number):
        if number%num==0:
            factorlist.append(num)
    if sum(factorlist)==number:
        return "perfect"
    elif sum(factorlist)<number:
        return "deficient"
    elif sum(factorlist)>number:
        return "abundant"
