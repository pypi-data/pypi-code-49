def quotient(a,b):
    quo=a/b
    return(quo)

def remainder(a,b):
    rem=a%b
    return(rem)

def floordiv(a,b):
    div=a//b
    return(div)

def product(a,b):
    prod=a*b
    return(prod)

def power(a,b):
    pow=a**b
    return(pow)

def sum(a,b):
    add=a+b
    return(add)

def subtract(a,b):
    sub=a-b
    return(sub)

def iseven(n):
    while(n>0):
        r=remainder(n,10)
        temp=remainder(r,2)
        if(temp==0):
            return True
        else:
            return False
        n=floordiv(n,10)

def isodd(n):
    while(n>0):
        r=remainder(n,10)
        temp=remainder(r,2)
        if(temp!=0):
            return True
        else:
            return False
        n=floordiv(n,10)

def prteven(n):
    s=digreverse(n)
    while(s>0):
        r=remainder(s,10)
        c=iseven(r)
        if (c==True):
            print(r,end=(' '))
        s=floordiv(s,10)

def prtodd(n):
    s=digreverse(n)
    while(s>0):
        r=remainder(s,10)
        c=isodd(r)
        if (c==True):
            print(r,end=(' '))
        s=floordiv(s,10)

def digcount(n):
    c=0
    while(n>0):
        r=remainder(n,10)
        c=c+1
        n=floordiv(n,10)
    return(c)        

def prtevencount(n):
    x=0
    while(n>0):
        r=remainder(n,10)
        c=iseven(r)
        if(c == True):
            x=x+1
    print(x)

def prtoddcount(n):
    x=0
    while(n>0):
        r=remainder(n,10)
        c=isodd(r)
        if(c==True):
            x=x+1
    print(x)

def evensum(n):
    x=0
    while(n>0):
        r=remainder(n,10)
        c=iseven(r)
        if(c==True):
            x=x+r
    return(x)

def oddsum(n):
    x=0
    while(n>0):
        r=remainder(n,10)
        c=isodd(r)
        if(c==True):
            x=x+r
    return(x)

def digitsum(n):
    x=0
    while(n>0):
        r=remainder(n,10)
        x=x+r
        n=floordiv(n,10)
    return(x)

def isprime(n):
    if n<=1:
        return False
        
    if n<=3:
        return True
        
    if (n%2==0 or n%3==0):
        return False
    i=5
    while(i * i<=n):
        if(n%i==0 or n%(i+2)==0):
            return False
            
        i=i+6
    return True

def primedigitcount(n):
    x=0
    while(n>0):
        r=remainder(n,10)
        c=isprime(r)
        if c == True:
            x=x+1
        n=floordiv(n,10)
    return(x)

def prtprime(n):
    s=digreverse(n)
    while(s>0):
        r=remainder(s,10)
        c=isprime(r)
        if c == True:
            print(r,end=(' '))
        s=floordiv(s,10)

def primedigitsum(n):
    x=0
    while(n>0):
        r=remainder(n,10)
        c=isprime(r)
        if c == True:
            x=x+r
        n=quotient(n,10)
    return(x)

def digreverse(n):
    s=0
    while(n>0):
        r=remainder(n,10)
        s=(s*10)+r
        n=floordiv(n,10)
    return(s)

def ispalindrome(n):
    s=0
    x=digreverse(n)
    if n == x:
        return True
    else:
        return False

def factor(n):
    i=1
    for i in range(1,n+1):
        if n%i==0:
            return(i)

def factorcount(n):
    i=1
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
    return(c)

def factorsum(n):
    i=1
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+i
    return c

def factorial(n):
    i=1
    c=1
    for i in range(1,n+1):
        c=c*i
    return c

def isstrong(n):
    m=n
    s=0
    while(m>0):
        f=1
        i=1
        r=remainder(m,10)
        while(i<=r):
            f=f*i
            i=i+1
        s=s+f
        m=floordiv(m,10)
    if(s==n):
        return True
    else:
        return False


def isperfect(n):
    s=0
    for i in range(1,n):
        if(n%i==0):
            s=s+i
    if(s==n):
        return True
    else:
        return False

def isarmstrong(n):
    m=n
    s=0
    while(n>0):
        r=remainder(n,10)
        s=s+r*r*r
        n=floordiv(n,10)
    if m==s:
        return True
    else:
        return False


def digitproduct(n):
    x=1
    while(n>0):
        r=remainder(n,10)
        x=x*r
        n=floordiv(n,10)
    return(x)

