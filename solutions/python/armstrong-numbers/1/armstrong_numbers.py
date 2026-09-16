def is_armstrong_number(number):
    t=0
    for digit in str(number):
        t+=int(digit)**(len(str(number)))
    if t==number:
        return True
    if t!=number:
        return False
        
