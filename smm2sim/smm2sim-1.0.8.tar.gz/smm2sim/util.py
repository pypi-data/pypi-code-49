playoff_series_ids = {
    1:('Round of 16',1),
    2:('Round of 16',2),
    3:('Round of 16',3),
    4:('Round of 16',4),
    5:('Round of 16',5),
    6:('Round of 16',6),
    7:('Round of 16',7),
    8:('Round of 16',8),
    9:('Quarterfinals',1),
    10:('Quarterfinals',2),
    11:('Quarterfinals',3),
    12:('Quarterfinals',4),
    13:('Semifinals',1),
    14:('Semifinals',2),
    15:('Championship',1)}

def extractText(tosearch, delim_left='', delim_right= None,
                reverse_left=False, reverse_right=False,
                optional_left=False, optional_right=False):
    rdelim = delim_left if delim_right is None else delim_right
    returnval = tosearch
    if delim_left != '':
        returnval = extractHelper(returnval, delim_left, reverse_left, optional_left, True)
    if rdelim != '':
        returnval = extractHelper(returnval, rdelim, reverse_right, optional_right, False)
    return returnval

def extractHelper(tosearch, delim, reverse_order, is_optional, is_left):
    cond1 = (is_left == (is_optional == reverse_order))
    cond2 = (not reverse_order) and is_left
    n = 2 if is_left else 0
    basefunc = str.rpartition if reverse_order else str.partition
    partitioned = basefunc(tosearch, delim)
    return partitioned[n] if (cond1 or partitioned[1] == delim) else partitioned[0] if cond2 else ''