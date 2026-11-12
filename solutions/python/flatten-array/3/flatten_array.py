def flatten(iterable):
    masterlist=[]
    def flattener(iterable):
        for item in iterable:
            if not isinstance(item, list) and item!=None:
                masterlist.append(item)
            elif isinstance(item, list):
                flattener(item)
    flattener(iterable)
    return masterlist
