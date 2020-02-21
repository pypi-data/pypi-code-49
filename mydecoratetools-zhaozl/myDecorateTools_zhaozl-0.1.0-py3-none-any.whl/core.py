from time import strftime, localtime, time

'''
时间工具箱
'''


def myTimer(level, minimumUnit='s'):
    '''
    :param level:内容丰富度，both/time_lasting/time_start_end
    :param minimumUnit:最小时间间隔单位，default=s/m/h
    :return:
    '''
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            startTime = time()
            def content(startTime, endTime, level, minimumUnit):
                lastTime = endTime - startTime
                startTime = strftime('%H:%M:%S', localtime(startTime))
                endTime = strftime('%H:%M:%S', localtime(endTime))
                if minimumUnit == 'm':
                    lastTime = str(lastTime / 60)[0:3] + '分钟'
                elif minimumUnit == 'h':
                    lastTime = str(lastTime / 3600)[0:3] + '小时'
                elif minimumUnit == 's':
                    lastTime = str(lastTime)[0:3] + '秒'
                contentBoth = '====================过程时间信息====================\n' + \
                              '\t\t开始：'+str(startTime)+'\t\t\t结束：'+str(endTime)+'\n' + \
                              '\t\t经过：'+str(lastTime)+'\n' + \
                              '===================================================='
                contentPoints = '====================过程时间信息====================\n' + \
                                '\t\t开始：'+str(startTime)+'\t\t\t结束：'+str(endTime)+'\n' + \
                                '===================================================='
                contentGap = '====================过程时间信息====================\n' + \
                             '\t\t经过：'+str(lastTime)+'\n' + \
                             '===================================================='
                if level == 'both':
                    contentStr = contentBoth
                elif level == 'time_lasting':
                    contentStr = contentGap
                elif level == 'time_start_end':
                    contentStr = contentPoints
                return contentStr
            func(*args, **kwargs)
            endTime = time()
            contentStr = content(startTime, endTime, level, minimumUnit)
            print(contentStr)
            return
        return inner_wrapper
    return wrapper
