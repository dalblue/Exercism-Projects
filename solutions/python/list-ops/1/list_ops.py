def append(list1, list2):
    for item in list2:
        list1.append(item)
    return list1


def concat(lists):
    newlist=[]
    for list in lists:
        for item in list:
            newlist.append(item)
    return newlist


def filter(function, list):
    yeslist=[]
    for item in list:
        if function(item):
            yeslist.append(item)
    return yeslist


def length(list):
    return len(list)


def map(function, list):
    outlist=[]
    for item in list:
        outlist.append(function(item))
    return outlist



def foldl(function, list, initial):
    for num in list:
        initial=function(initial, num)
        
    return initial

def foldr(function, list, initial):
    for num in reversed(list):
        initial=function(initial, num)
    return initial


def reverse(list):
    newlist=[]
    if len(list)==0:
        return []
    else:
        for item in list[-1::-1]:
            newlist.append(item)
    return newlist