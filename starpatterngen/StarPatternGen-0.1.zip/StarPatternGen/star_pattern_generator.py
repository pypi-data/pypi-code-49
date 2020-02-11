def starGen(n_star):
    num = [n for n in range(1,n_star)]
    for i in num :
        print('*' * i)
    num.pop()
    for i in num[::-1] :
        print('*'*i)