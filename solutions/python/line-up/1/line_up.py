def line_up(name, number):
    special=["1","2","3"]
    elseall=["11","12","13"]
    numberest=str(number)
    numfix=""
    if numberest[-1] not in special:
        numfix="th"
    if numberest[-1] in special:
        if len(numberest)==1:
            if numberest=="1":
                numfix="st"
            if numberest=="2":
                numfix="nd"
            if numberest=="3":
                numfix="rd"
        elif len(numberest)!=1:
            if numberest[-1]=="1":
                if numberest[-2]=="1":
                    numfix="th"
                else:
                    numfix="st"
            if numberest[-1]=="2":
                if numberest[-2]=="1":
                    numfix="th"
                else:
                    numfix="nd"
            if numberest[-1]=="3":
                if numberest[-2]=="1":
                    numfix="th"
                else:
                    numfix="rd"
    inline=f"{name}, you are the {numberest}{numfix} customer we serve today. Thank you!"
    return inline