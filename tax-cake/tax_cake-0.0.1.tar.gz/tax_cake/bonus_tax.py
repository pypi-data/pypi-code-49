

#遍历最好的分配方案
def searchBestSuit(salary,bonus,fetchMoney,step):

    suitDict = {}

    while fetchMoney <= bonus + salary:
        print ('计税月薪，扣除五险一金和抵扣后为：%i' %salary)
        print ('绩效年终奖 %i' %bonus)
        print ('本月领取 %i 元' %(fetchMoney))
        total = allocateBonus(salary,bonus,fetchMoney)
        suitDict[fetchMoney] = total
        fetchMoney += step
        pass

    for (fetch,total) in  suitDict.items():
        print ('本月领取%.2f元，2020年个税总额是%.2f' %(fetch,total))

    return






#例如张三月薪40000，每个月五险一金扣除6000,买房利息抵扣1000元
# 年终奖为80000， 本月提取10000元，剩下70000被划作年终奖金额

#那么输入的参数应该如下
# salary = 40000 - 6000 - 1000 =33000
# bonus = 80000 绩效奖金
# fetchMoney = 10000 本月提取
# return : 张三2020年全年缴纳的个税 = 12个月个税+年终奖个税
def allocateBonus(monthSalary,totalBonus,fetchMoney):
    realBonus = totalBonus - fetchMoney
    yearSalary = 12 * monthSalary + fetchMoney
    taxDict = pinYearTaxDict(yearSalary)
    taxRate = taxDict['rate']
    deduction = taxDict['deduction']
    yearTax = yearSalary * taxRate - deduction
    print("您全年收入（12个月工资+年终奖划入工资部分）为 %i 对应的税率是 %.2f,速算扣除数为 %.2f" %(yearSalary,taxRate,deduction))
    print("您今年收入个税个税为 %.2f 人民币" %(yearTax))
    
    taxDict = pinBonusTaxDict(realBonus)
    
    taxRate = taxDict['rate']
    deduction = taxDict['deduction']
    print ("您实际年终奖金额为 %.2f,对应的税率是 %.2f,速算扣除数为 %.2f" %(realBonus,taxRate,deduction))
    bonusTax = realBonus * taxRate - deduction
    print("您缴纳的年终奖个税为 %.2f 人民币" %(bonusTax))
    total = yearTax + bonusTax
    print ("按照这个方案，您在今年全年需要缴纳的个税=全年工资个税+年终奖个税= %.2f + %.2f = %.2f "
    %(yearTax,bonusTax,total))
    print ('++++++++++++++++++++++')
    return total

def pinYearTaxDict(money):
    if money <= 36000:
        return taxDict(0.03,0)
    elif money <= 144000:
        return taxDict(0.1,2520)
    elif money <= 300000:
        return taxDict(0.2,16920)
    elif money <= 420000:
        return taxDict(0.25,31920)
    elif money <= 660000:
        return taxDict(0.3,52920)
    elif money <= 960000:
        return taxDict(0.35,85920)

    return taxDict(0.45,181920)

def pinBonusTaxDict(realBonus):
    monthBouns = realBonus / 12
    if monthBouns <= 3000:
        return taxDict(0.03,0)
    elif monthBouns <= 12000:
        return taxDict(0.1,210)
    elif monthBouns <= 25000:
        return taxDict(0.2,1410)
    elif monthBouns <= 35000:
        return taxDict(0.25,2660)
    elif monthBouns <= 55000:
        return taxDict(0.3,4410)
    elif monthBouns <= 80000:
        return taxDict(0.35,7160)
    return taxDict(0.45,15160)

def taxDict(rate,deduction):
    return { 'rate' : rate, 'deduction' : deduction}


# 计税月薪= 每个月税前工资 - 五险一金 - 个税抵扣。
salary = 20000 
# 绩效年终奖
bonus = 80000
#本月提取
fetchMoney = 5000
#遍历步长,单位:元
step = 2000
#遍历出最佳方案
searchBestSuit(salary,bonus,fetchMoney,step)
#total = allocateBonus(salary,bonus,fetchMoney)




