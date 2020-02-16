from datetime import datetime, timedelta
from itertools import accumulate
import requests
import dill
import os

# The class `LunarDate` is modified from https://github.com/CutePandaSh/zhdate.git
def download_data():
    pwd_path = os.path.dirname(__file__)
    data_path = os.path.join(pwd_path, 'date_data')
    if os.path.exists(data_path):
        pass
    else:
        print('Downloading the required file')
        res = requests.get('https://raw.githubusercontent.com/beidongjiedeguang/guang/master/guang/Utils/date_data')
        with open(data_path, 'wb') as fo:
            fo.write(res.content)
    return data_path
data_path = download_data()
with open(data_path, 'rb') as fi:
    [CHINESENEWYEAR,CHINESEYEARCODE] = dill.load(fi)

class LunarDate():

    def __init__(self, lunar_year, lunar_month, lunar_day, leap_month=False):
        """初始化函数

        Arguments:
            lunar_year {int} -- 农历年
            lunar_month {int} -- 农历月份
            lunar_day {int} -- 农历日

        Keyword Arguments:
            leap_month {bool} -- 是否是在农历闰月中 (default: {False})

        """
        if not LunarDate.validate(lunar_year, lunar_month, lunar_day, leap_month):
            raise TypeError('农历日期不支持，超出农历1900年1月1日至2100年12月29日，或日期不存在')
        self.lunar_year = lunar_year
        self.lunar_month = lunar_month
        self.lunar_day = lunar_day
        self.leap_month = leap_month
        self.year_code = CHINESEYEARCODE[self.lunar_year - 1900]
        self.newyear = datetime.strptime(CHINESENEWYEAR[self.lunar_year - 1900], '%Y%m%d')

    def to_datetime(self):
        """农历日期转换称公历日期

        Returns:
            datetime -- 当前农历对应的公历日期
        """
        return self.newyear + timedelta(days=self.__days_passed())

    @staticmethod
    def from_datetime(dt):
        """静态方法，从公历日期生成农历日期

        Arguments:
            dt {datetime} -- 公历的日期

        Returns:
            LunarDate -- 生成的农历日期对象
        """
        lunar_year = dt.year
        if (datetime.strptime(CHINESENEWYEAR[lunar_year - 1900], '%Y%m%d') - dt).days > 0:
            lunar_year -= 1
        newyear_dt = datetime.strptime(CHINESENEWYEAR[lunar_year - 1900], '%Y%m%d')
        days_passed = (dt - newyear_dt).days
        year_code = CHINESEYEARCODE[lunar_year - 1900]
        month_days = LunarDate.decode(year_code)

        for pos, days in enumerate(accumulate(month_days)):
            if days_passed + 1 <= days:
                month = pos + 1
                lunar_day = month_days[pos] - (days - days_passed) + 1
                break

        leap_month = False
        if (year_code & 0xf) == 0 or month <= (year_code & 0xf):
            lunar_month = month
        else:
            lunar_month = month - 1

        if (year_code & 0xf) != 0 and month == (year_code & 0xf) + 1:
            leap_month = True

        return LunarDate(lunar_year, lunar_month, lunar_day, leap_month)

    @staticmethod
    def today():
        return LunarDate.from_datetime(datetime.now())

    def __days_passed(self):
        """私有方法，计算当前农历日期和当年农历新年之间的天数差值

        Returns:
            int -- 差值天数
        """
        month_days = LunarDate.decode(self.year_code)
        month_leap = self.year_code & 0xf  # 当前农历年的闰月，为0表示无闰月

        if (month_leap == 0) or (self.lunar_month < month_leap):  # 当年无闰月，或者有闰月但是当前月小于闰月
            days_passed_month = sum(month_days[:self.lunar_month - 1])
        elif (not self.leap_month) and (self.lunar_month == month_leap):  # 当前不是闰月，并且当前月份和闰月相同
            days_passed_month = sum(month_days[:self.lunar_month - 1])
        else:
            days_passed_month = sum(month_days[:self.lunar_month])

        return days_passed_month + self.lunar_day - 1

    def chinese(self):
        ZHNUMS = '零一二三四五六七八九十'
        zh_year = ''
        for i in range(0, 4):
            zh_year += ZHNUMS[int(str(self.lunar_year)[i])]
        zh_year += '年'

        if self.leap_month:
            zh_month = '闰'
        else:
            zh_month = ''

        if self.lunar_month == 1:
            zh_month += '正'
        elif self.lunar_month == 12:
            zh_month += '腊'
        elif self.lunar_month <= 10:
            zh_month += ZHNUMS[self.lunar_month]
        else:
            zh_month += f"十{ZHNUMS[self.lunar_month - 10]}"
        zh_month += '月'

        if self.lunar_day <= 10:
            zh_day = f'初{ZHNUMS[self.lunar_day]}'
        elif self.lunar_day < 20:
            zh_day = f'十{ZHNUMS[self.lunar_day - 10]}'
        elif self.lunar_day == 20:
            zh_day = '二十'
        elif self.lunar_day < 30:
            zh_day = f'二十{ZHNUMS[self.lunar_day - 20]}'
        else:
            zh_day = '三十'

        year_tiandi = LunarDate.__tiandi(self.lunar_year - 1900 + 36) + '年'

        shengxiao = "鼠牛虎兔龙蛇马羊猴鸡狗猪"

        return f"{zh_year}{zh_month}{zh_day} {year_tiandi} ({shengxiao[(self.lunar_year - 1900) % 12]}年)"

    def __str__(self):
        """打印字符串的方法

        Returns:
            str -- 标准格式农历日期字符串
        """
        if self.leap_month:
            return f"农历{self.lunar_year}年闰{self.lunar_month}月{self.lunar_day}日"
        else:
            return f"农历{self.lunar_year}年{self.lunar_month}月{self.lunar_day}日"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, another):
        if not isinstance(another, LunarDate):
            raise TypeError('比较必须都是LunarDate类型')
        cond1 = self.lunar_year == another.lunar_year
        cond2 = self.lunar_month == another.lunar_month
        cond3 = self.lunar_day == another.lunar_day
        cond4 = self.leap_month == another.leap_month
        return cond1 and cond2 and cond3 and cond4

    def __add__(self, another):
        if not isinstance(another, int):
            raise TypeError('加法只支持整数天数相加')
        return LunarDate.from_datetime(self.to_datetime() + timedelta(days=another))

    def __sub__(self, another):
        if isinstance(another, int):
            return LunarDate.from_datetime(self.to_datetime() - timedelta(days=another))
        elif isinstance(another, LunarDate):
            return (self.to_datetime() - another.to_datetime()).days
        elif isinstance(another, datetime):
            return (self.to_datetime() - another).days
        else:
            raise TypeError('减法只支持整数，LunarDate, Datetime类型')


    @staticmethod
    def __tiandi(anum):
        tian = '甲乙丙丁戊己庚辛壬癸'
        di = '子丑寅卯辰巳午未申酉戌亥'
        return f'{tian[anum % 10]}{di[anum % 12]}'

    @staticmethod
    def validate(year, month, day, leap):
        """农历日期校验

        Arguments:
            year {int} -- 农历年份
            month {int} -- 农历月份
            day {int} -- 农历日期
            leap {bool} -- 农历是否为闰月日期

        Returns:
            bool -- 校验是否通过
        """
        # 年份低于1900，大于2100，或者月份不属于 1-12，或者日期不属于 1-30，返回校验失败
        if not (1900 <= year <= 2100 and 1 <= month <= 12 and 1 <= day <= 30):
            return False

        year_code = CHINESEYEARCODE[year - 1900]

        # 有闰月标志
        if leap:
            if (year_code & 0xf) != month:  # 年度闰月和校验闰月不一致的话，返回校验失败
                return False
            elif day == 30:  # 如果日期是30的话，直接返回年度代码首位是否为1，即闰月是否为大月
                return (year_code >> 16) == 1
            else:  # 年度闰月和当前月份相同，日期不为30的情况，返回通过
                return True
        elif day <= 29:  # 非闰月，并且日期小于等于29，返回通过
            return True
        else:  # 非闰月日期为30，返回年度代码中的月份位是否为1，即是否为大月
            return ((year_code >> (12 - month) + 4) & 1) == 1

    @staticmethod
    def decode(year_code):
        """解析年度农历代码函数

        Arguments:
            year_code {int} -- 从年度代码数组中获取的代码整数

        Returns:
            [int] -- 当前年度代码解析以后形成的每月天数数组，已将闰月嵌入对应位置，即有闰月的年份返回长度为13，否则为12
        """
        month_days = list()
        for i in range(5, 17):
            if (year_code >> (i - 1)) & 1:
                month_days.insert(0, 30)
            else:
                month_days.insert(0, 29)
        if year_code & 0xf:
            if year_code >> 16:
                month_days.insert((year_code & 0xf), 30)
            else:
                month_days.insert((year_code & 0xf), 29)
        return month_days

    @staticmethod
    def month_days(year):
        """根据年份返回当前农历月份天数list

        Arguments:
            year {int} -- 1900到2100的之间的整数

        Returns:
            [int] -- 农历年份所对应的农历月份天数列表
        """
        return LunarDate.decode(
            CHINESEYEARCODE[year - 1900]
        )


    
"""the following code is copied from the network"""

import math
import ephem

def chinaCalendar(date): # 默认输入ut+8时间
    lunar_yue =["正月","二月","三月","四月","五月","六月","七月","八月","九月","十月","十一月","十二月"]
    nlrq = ["初一","初二","初三","初四","初五","初六","初七","初八","初九","初十","十一","十二","十三","十四","十五","十六","十七","十八","十九","二十","廿一","廿二","廿三","廿四","廿五","廿六","廿七","廿八","廿九","三十"]
    tiangan = ["甲","乙","丙","丁","戊","己","庚","辛","壬","癸"]
    dizhi = ["子","丑","寅","卯","辰","巳","午","未","申","酉","戌","亥"]
    gz = [''] * 60  # 六十甲子表
    for i in range(60):
        gz[i] = tiangan[i % 10] + dizhi[i % 12]

    def EquinoxSolsticeJD(year, angle):
        if 0 <= angle < 90:
            date = ephem.next_vernal_equinox(year)
        elif 90 <= angle < 180:
            date = ephem.next_summer_solstice(year)
        elif 180 <= angle < 270:
            date = ephem.next_autumn_equinox(year)
        else:
            date = ephem.next_winter_solstice(year)
        JD = ephem.julian_date(date)
        return JD

    # 计算二十四节气
    def SolarLongitube(JD):
        date = ephem.Date(JD - 2415020)
        s = ephem.Sun(date)  # date应为UT时间
        sa = ephem.Equatorial(s.ra, s.dec, epoch=date)
        se = ephem.Ecliptic(sa)
        L = se.lon / ephem.degree / 180 * math.pi
        return L

    def SolarTerms(year, angle):
        if angle > 270: year -= 1
        if year == 0: year -= 1  # 公元0改为公元前1
        JD = EquinoxSolsticeJD(str(year), angle)  # 初值
        JD1 = JD
        while True:
            JD2 = JD1
            L = SolarLongitube(JD2)
            JD1 += math.sin(angle * math.pi / 180 - L) / math.pi * 180
            if abs(JD1 - JD2) < 0.00001:
                break # 精度小于1 second
        return JD1 # UT

    def DateCompare(JD1, JD2): # 输入ut，返回ut+8的比较结果
        JD1 += 0.5 + 8/24
        JD2 += 0.5 + 8/24
        if int(JD1) >= int(JD2): return True
        else: return False

    def dzs_search(year): # 寻找年前冬至月朔日
        if year == 1: year -= 1  # 公元0改为公元前1
        dz = ephem.next_solstice(str(year-1) + '/12') # 年前冬至
        jd = ephem.julian_date(dz)
        # 可能的三种朔日
        date1 = ephem.next_new_moon(ephem.Date(jd - 2415020 - 0))
        jd1 = ephem.julian_date(date1)
        date2 = ephem.next_new_moon(ephem.Date(jd - 2415020 - 29))
        jd2 = ephem.julian_date(date2)
        date3 = ephem.next_new_moon(ephem.Date(jd - 2415020 - 31))
        jd3 = ephem.julian_date(date3)
        if DateCompare(jd, jd1): # 冬至合朔在同一日或下月
            return date1
        elif DateCompare(jd, jd2) and (not DateCompare(jd, jd1)):
            return date2
        elif DateCompare(jd, jd3): # 冬至在上月
            return date3
    
    
    JD = ephem.julian_date(date) - 8/24 # ut
    year = ephem.Date(JD + 8/24 - 2415020).triple()[0]
    shuo = []
    shuo.append(dzs_search(year))  # 冬至朔
    sJD1 = ephem.julian_date(shuo[0])
    next_dzs = dzs_search(year+1) # 次年冬至朔
    dzsJD = ephem.julian_date(next_dzs)
    if DateCompare(JD, dzsJD):
        shuo[0] = next_dzs
        next_dzs = dzs_search(year+2)
        dzsJD = ephem.julian_date(next_dzs)
    # 查找所在月及判断置闰
    run = ''
    szy = 0
    j = -1 # 计算连续两个冬至月中的合朔次数
    zry = 99 # 无效值
    flag = False
    while not DateCompare(sJD1, dzsJD): # 次年冬至朔前合朔即当年月份
        j += 1
        sJD1 = ephem.julian_date(shuo[j]) # 起冬至朔
        if DateCompare(JD, sJD1):
            szy += 1 # date所在月
            newmoon = int(sJD1 + 8/24 + 0.5)
        shuo.append(ephem.next_new_moon(shuo[j])) # i+1月朔
        if j == 0: continue # 冬至月一定含中气，从次月开始查找
        sJD2 = ephem.julian_date(shuo[j+1])  # 次月朔
        month = ephem.Date(sJD1 - 2415020).triple()[1] # 求某月的中气
        angle = (-90 + 30 * month) % 360 # 该月中气
        if j == 1:
            nian1 = ephem.Date(sJD1 - 2415020).triple()[0]
            qJD1 = SolarTerms(nian1, angle) # 每月中气
        else:
            qJD1 = qJD2 # 使用上次计算结果，节约计算
        nian2 = ephem.Date(sJD2 - 2415020).triple()[0]
        qJD2 = SolarTerms(nian2, (angle+30)%360) # 次月中气
        if not DateCompare(qJD1, sJD1) and DateCompare(qJD2, sJD2) and flag == False:
                zry = j + 1 # 置闰月
                flag = True # 仅第一个无中气月置闰
    rq = int(JD + 8/24 + 0.5) - newmoon # 日干支
    if j == 12 and zry != 99: # 连续两个冬至月间合朔12次则不闰
        zry = 99
    if szy % 12 == zry % 12 and zry != 99:
        run = '闰'
    if szy >= zry % 12 and zry != 99:
        szy -= 1
    # 判断节气月
    month = ephem.Date(date).triple()[1]
    angle = (-135 + 30 * month) % 360
    jJD2 = SolarTerms(year, (angle+30)%360) # 次月节气
    if angle == 225: # 再次月节气
        jJD3 = SolarTerms(year+1, (angle+60)%360)
    else:
        jJD3 = SolarTerms(year, (angle + 60) % 360)
    if angle == 255: # 每月节气
        jJD1 = SolarTerms(year-1, angle)
    else:
        jJD1 = SolarTerms(year, angle)
    daxue = False
    if DateCompare(JD, jJD3): # JD ≥ JD3
        jq = ephem.Date(jJD3 + 8/24 - 2415020)
        month2 = (angle + 15 - 210) // 30 % 12
        if angle == 225: daxue = True
    elif DateCompare(JD, jJD2): # JD2 ≤ JD ＜ JD3
        jq = ephem.Date(jJD2 + 8/24 - 2415020)
        month2 = (angle + 15 - 240) // 30 % 12
        if angle == 225 or (jq.triple()[1] == 12 and angle == 255): daxue = True  # 大雪或小寒
    else: # JD ＜ JD2
        jq = ephem.Date(jJD1 + 8/24 - 2415020)
        month2 = (angle + 15 - 270) // 30 % 12
        if angle == 255: daxue = True
    nian2 = jq.triple()[0]
    if nian2 < 0: nian2 += 1
    if daxue == True: nian2 += 1
    jqy = gz[(nian2 * 12 + month2 + 12) % 60] # 月干支
    if (szy - 3) % 12 >= 10 and ephem.Date(date).triple()[1] <= 3: year -= 1 # 年干支
    if year < 0: year += 1
        
    lunar_year = year
    lunar_month = (szy - 3) % 12 + 1
    lunar_day = rq + 1
    
    chinese_year = gz[(year - 4) % 60] + '年'
    chinese_month = jqy + '月'
    chinese_day = gz[int(JD + 8/24 + 0.5 + 49) % 60] + '日'
    return lunar_year, lunar_month, lunar_day, [chinese_year, chinese_month, chinese_day]