def leap_year(year):
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
