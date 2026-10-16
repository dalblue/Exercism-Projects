"""
This exercise stub and the test suite contain several enumerated constants.
Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).
You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = "sublist"
SUPERLIST = "superlist"
EQUAL = "equal"
UNEQUAL = "unequal"


def sublist(list_one, list_two):
    list1comp=""
    list2comp=""
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
    elif list_one!=list_two and len(list_one)==len(list_two):
        return UNEQUAL
    elif list1comp in list2comp and len(list_one)<len(list_two) and len(list1comp)!=len(list2comp):
        return SUBLIST
    elif list2comp in list1comp and len(list_one)>len(list_two) and len(list1comp)!=len(list2comp):
        return SUPERLIST
    return UNEQUAL
