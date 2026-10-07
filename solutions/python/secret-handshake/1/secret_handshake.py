def commands(binary_str):
    handshake=[]
    for count, char in enumerate(binary_str[-1::-1]):
        if count+1==1:
            if int(char):
                handshake.append("wink")
        if count+1==2:
            if int(char):
                handshake.append("double blink")
        if count+1==3:
            if int(char):
                handshake.append("close your eyes")
        if count+1==4:
            if int(char):
                handshake.append("jump")
        if count+1==5:
            if int(char):
                handshake.reverse()
    return handshake
    pass
