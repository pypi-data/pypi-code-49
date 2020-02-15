def frac(dec):
    n = 1
    m = str(dec)
    y, u = m.split('.')
    l = len(u)

    dec *= (10**l)
    n *= (10**l)
    dec = int(dec)

    i = dec
    while i > 1:
        rest1 = dec%i
        rest2 = n%i

        if rest1 == 0 and rest2 == 0:
            dec /= i
            n /= i
            i = dec
        else:
            i -= 1
    dec = int(dec)
    n = int(n)

    fraction = str(dec) + '/' + str(n)
    return fraction


def addFrac(f1, f2):
    try:
        n1, n2 = f1.split('/')
    except:
        n1 = f1
        n2 = 1
    f1 = [int(n1), int(n2)]
    try:
        n1, n2 = f2.split('/')
    except:
        n1 = f2
        n2 = 1
    f2 = [int(n1), int(n2)]

    m1 = f2[1]
    m2 = f1[1]
    for i in range (0, 2):
        f1[i] *= m1
        f2[i] *= m2
        
    t = f1[0] + f2[0]
    if t < 0:
        g = True
        t *= -1
    else:
        g = False
    n = f1[1]

    i = min([t, n])
    while i > 1:
        rest1 = t%i
        rest2 = n%i

        if rest1 == 0 and rest2 == 0:
            t /= i
            n /= i
            i = min([t, n])
        else:
            i -= 1
            
    if t == n:
        frac = str('1')
    elif t == 0:
        frac = 0
        return frac
    else:
        frac = str(int(t)) + '/' + str(int(n))
        n1, n2 = frac.split('/')
        if n2 == '1':
            frac = n1

    if g:
        frac = '-' + frac
    try:
        int(frac)
    except:
        pass
    return frac


def subFrac(f1, f2):
    f2 = str(f2)

    try:
        n1, n2 = f2.split('/')
    except:
        n1 = f2
        n2 = str('1')

    n1 = int(n1)
    n1 *= -1
    f2 = str(n1) + '/' + n2

    frac = addFrac(f1, f2)
    return frac


def multFrac(f1, f2):
    try:
        n1, n2 = f1.split('/')
    except:
        n1 = f1
        n2 = 1
    f1 = [int(n1), int(n2)]
    try:
        n1, n2 = f2.split('/')
    except:
        n1 = f2
        n2 = 1
    f2 = [int(n1), int(n2)]

    g1 = False
    if f1[0] < 0 and f1[1] > 0 or f1[1] < 0 and f1[0] > 0:
        g1 = True
    g2 = False
    if f2[0] < 0 and f2[1] > 0 or f2[1] < 0 and f2[0] > 0:
        g2 = True
    if g1 == True and not g2 == True or g2 == True and not g1 == True:
        g = True
    else:
        g = False

    t = f1[0]*f2[0]
    if t < 0:
        t *= -1
    n = f1[1]*f2[1]
    if n < 0:
        n *= -1

    i = min([t, n])
    while i > 1:
        rest1 = t%i
        rest2 = n%i
        if rest1 == 0 and rest2 == 0:
            t /= i
            n /= i
            i = min([t, n])
        else:
            i -= 1

    if t == n:
        frac = str('1')
    elif t == 0:
        frac = 0
        return frac
    else:
        frac = str(int(t)) + '/' + str(int(n))
        n1, n2 = frac.split('/')
        if n2 == '1':
            frac = n1

    if g:
        frac = '-' + frac
    try:
        int(frac)
    except:
        pass
    return frac


def divFrac(f1, f2):
    f2 = str(f2)

    try:
        n1, n2 = f2.split('/')
    except:
        n1 = f2
        n2 = str('1')

    f2 = n2 + '/' + n1
    
    frac = multFrac(f1, f2)
    return frac


def powerFrac(f1, p):
    n1, n2 = f1.split('/')

    t = int(n1)
    n = int(n2)

    for i in range (1, p):
        t *= t
        n *= n
    
    i = min([t, n])
    while i > 1:
        rest1 = t%i
        rest2 = n%i
        if rest1 == 0 and rest2 == 0:
            t /= i
            n /= i
            i = min([t, n])
        else:
            i -= 1

    if t == n:
            frac = str('1')
    elif t == 0:
        frac = 0
        return frac
    else:
        frac = str(int(t)) + '/' + str(int(n))
        n1, n2 = frac.split('/')
        if n2 == '1':
            frac = n1
    return frac