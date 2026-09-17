def square(number):
    if number==None:
        raise TypeError("total() missing 1 required positional argument: 'number'")
    if number<1 or number>64:
        raise ValueError("square must be between 1 and 64")
    return 2**(number-1)


def total():
    t=0
    for numbers in range(64):
        t+=square(numbers+1)
        
    return t

print(total())