def convert(number):
    dropsound=""
    if number%3==0:
        dropsound+="Pling"
    if number%5==0:
        dropsound+="Plang"
    if number%7==0:
        dropsound+="Plong"
    if dropsound=="":
        dropsound+=str(number)
    return dropsound
