def square_of_sum(number):
    t=0
    for num in range(number+1):
       t+=num
    return t**2


def sum_of_squares(number):
    t=0
    for num in range(number+1):
        t+=num**2
    return t


def difference_of_squares(number):
    return square_of_sum(number)-sum_of_squares(number)
