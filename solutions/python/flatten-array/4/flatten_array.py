def flatten(iterable):
    masterlist=[]
    def flattener(iterable):
        for item in iterable:
            if not isinstance(item, list) and not isinstance(item, type(None)):
                masterlist.append(item)
            elif isinstance(item, list):
                flattener(item)
    flattener(iterable)
    return masterlist
