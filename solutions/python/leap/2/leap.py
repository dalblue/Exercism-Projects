def leap_year(year):
    """leap_year is a function that:
    takes in a paramter(year)
    returns a bool representing whether the year given is a leap year
    """
    isleap=False
    if year%4==0:
        if year%100==0:
            if year%400==0:
                isleap=True
            else:
                pass
        else:
            isleap=True
    else:
        pass
    return isleap
