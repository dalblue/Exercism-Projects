def value(colors):
    colorlist=["black","brown","red","orange","yellow","green","blue","violet","grey","white"]
    resvalue=""
    count=1
    for char in colors:
        if count<=2:
            resvalue+=str(colorlist.index(char))
            count+=1
        else:
            break
    return int(resvalue)