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
    isperfect=""
    if sum(factorlist)==number:
        isperfect="perfect"
    if sum(factorlist)<number:
        isperfect="deficient"
    if sum(factorlist)>number:
        isperfect="abundant"
    return isperfect