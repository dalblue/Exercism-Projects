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
    slicedict={0:resvalue,
                11:resvalue[0:2],
                10:resvalue[0],
                9:resvalue[0:3],
                8:resvalue[0:2],
                7:resvalue[0],
                6:resvalue[0:3],
                5:resvalue[0:2],
                4:resvalue[0]}
    if not int(resvalue):
        resvaluefinal+=resvalue+" "
    elif int(resvalue)%1000000000==0:
        resvaluefinal+=slicedict.get(len(resvalue))
        resvaluefinal+=" giga"
    elif int(resvalue)%100000==0:
        resvaluefinal+=slicedict.get(len(resvalue))
        resvaluefinal+=" mega"
    elif int(resvalue)%1000==0:
        resvaluefinal+=slicedict.get(len(resvalue))
        resvaluefinal+=" kilo"
    else:
        resvaluefinal+=resvalue+" "
    resvaluefinal+="ohms"
    return resvaluefinal