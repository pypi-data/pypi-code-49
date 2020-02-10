
#from tax_rules import pinYearTaxDict

import sys
sys.path.append('tax_rules.py')
class YearSalaryTaxCalculator:

    _monthThreshold = 5000

    def __init__(self):
        return
     #计算单月的个税
    def taxOfMonth(self,monthIndex,monthSalary,taxSum,yearSum):
        assert(monthIndex >= 0 and monthIndex < 12 )
        assert(monthSalary > self._monthThreshold)
        inputSum = (monthSalary - self._monthThreshold) * (monthIndex +1)     
        taxDict = pinYearTaxDict(inputSum)
        rate = taxDict['rate']
        deduction = taxDict['deduction']
        tax = inputSum * rate - deduction - taxSum
        return tax

    #按照月薪，预估全年的累计数个税
    def yearSalaryTax(self,monthSalary):
        
        if monthSalary <= self._monthThreshold:
            raise Exception('十分遗憾，您的薪水太低,作为纳税人的荣誉被剥夺了')
            return 0

        monthIndex = 0
        salarySum = 0
        taxSum =0
        while (monthIndex < 12):
            salarySum += monthSalary
            monthTax = self.taxOfMonth(monthIndex,monthSalary,taxSum,salarySum)
            print('%i 月份缴纳个税 %.2f 元' %(monthIndex+1,monthTax))
            taxSum += monthTax
            monthIndex += 1
        return taxSum
    
    def yearSalaryTextInput(self):
        text = ("请输入您扣除五险一金和个税低折扣后的月薪: "
        "(例如您税前月薪30000元，五险一金扣除5000元，"
        "赡养两位老人抵扣2000元，"
        "第一套房贷利息抵扣1000元，"
        "您在此应该输入的的金额应该是30000-5000-2000-1000=22000) ")
        return text
    
    def yearSalayMain(self):
        try:
            text = self.yearSalaryTextInput()
            monthSalary = int(input(text))
            #cal = YearSalaryTaxCalculator()
            ys = self.yearSalaryTax(monthSalary)
            print('按照您现在的薪水，您一年缴纳个税是 %.2f 元' %(ys))
        except Exception as e:
            print (e)
        return

cal = YearSalaryTaxCalculator()
cal.yearSalayMain()


   