def getTopicsFromGeospace(channel, geospace):
    if isinstance(geospace, str):
        l = [channel + geospace]
        return l
    
    l = []
    for g in geospace:
        l.append(channel + g)
    
    return l