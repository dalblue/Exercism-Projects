def label(colors):
    colorlist=["black","brown","red","orange","yellow","green","blue","violet","grey","white"]
    resvalue=""
    resvaluefinal=""
    count=1
    for count, char in enumerate(colors):
        if all(char=="black" for char in colors):
            resvalue="0"
            break
        if count<=1:
            if char=="black" and char==colors[0]:
                pass
            else:
                resvalue+=str(colorlist.index(char))
        elif count==2:
            resvalue+=(str(0)*(colorlist.index(char)))
        elif count>2:
            break
    if not int(resvalue):
        resvaluefinal+=resvalue+" "
    elif int(resvalue)%1000000000==0:
        if len(resvalue)==11:
            resvaluefinal+=resvalue[0:2]
        if len(resvalue)==10:
            resvaluefinal+=resvalue[0]
        resvaluefinal+=" giga"
    elif int(resvalue)%100000==0:
        if len(resvalue)==9:
            resvaluefinal+=resvalue[0:3]
        if len(resvalue)==8:
            resvaluefinal+=resvalue[0:2]
        if len(resvalue)==7:
            resvaluefinal+=resvalue[0]
        resvaluefinal+=" mega"
    elif int(resvalue)%1000==0:
        if len(resvalue)==6:
            resvaluefinal+=resvalue[0:3]
        if len(resvalue)==5:
            resvaluefinal+=resvalue[0:2]
        if len(resvalue)==4:
            resvaluefinal+=resvalue[0]
        resvaluefinal+=" kilo"
    else:
        resvaluefinal+=resvalue+" "
    resvaluefinal+="ohms"
    return resvaluefinal