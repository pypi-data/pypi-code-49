import sys
from rzqtest import tools
tools.setStat(sys.argv)
urls = tools.getUrl(tools.G['urlfile'])
result_before = []
result_after = []
tools.G['isCert'] and result_before.append(tools.verifyCert(urls))
tools.G['isCert'] and result_after.append(tools.makeRecords(result_before[-1], "Cert"))
tools.G['isCert'] and tools.G['isPrint'] and print(result_after[-1])
tools.G['isUrl'] and result_before.append(tools.verifyAddress(urls))
tools.G['isUrl']  and result_after.append(tools.makeRecords(result_before[-1], "Access"))
tools.G['isUrl'] and tools.G['isPrint'] and print(result_after[-1])
tools.G['isSend'] and tools.send("".join(result_after),"测试结果")