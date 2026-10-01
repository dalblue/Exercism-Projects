SUBLIST = "sublist"
SUPERLIST = "superlist"
EQUAL = "equal"
UNEQUAL = "unequal"
def sublist(list_one, list_two):
    list1comp=""
    list2comp=""
    for char in list_one:
        list1comp+=str(char)
    for char in list_two:
        list2comp+=str(char)
    if list_one==list_two:
        return EQUAL
    if list_one!=list_two and len(list_one)==len(list_two):
        return UNEQUAL
    if list1comp in list2comp and len(list_one)<len(list_two) and len(list1comp)!=len(list2comp):
        return SUBLIST
    if list2comp in list1comp and len(list_one)>len(list_two) and len(list1comp)!=len(list2comp):
        return SUPERLIST
    return UNEQUAL