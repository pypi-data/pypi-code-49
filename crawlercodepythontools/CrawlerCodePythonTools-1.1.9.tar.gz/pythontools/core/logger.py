from colorama import init
from colorama import Fore, Back, Style
import time, os
from pythontools.core import tools

init()

logs = []
logPath = ""
logFile = ""

def initLogDirectory(path):
    global logFile, logPath
    logPath = path
    logFile = path + "/" + time.strftime("log_%Y_%m_%d_%H_%M_%S", time.localtime()) + ".txt"
    tools.createFile(logFile)

def getLogByDisplayname(displayname):
    return tools.getFileContent(logPath + "/log_" + displayname.replace("/", "_").replace(":", "_").replace(" ", "_") + ".txt")

def getDisplayname(filename):
    pices = filename.replace("log_", "").replace(".txt", "").split("_")
    return pices[0] + "/" + pices[1] + "/" + pices[2] + " " + pices[3] + ":" + pices[4] + ":" + pices[5]

def getAllLogs():
    list = []
    for filename in os.listdir(logPath):
        list.append(getDisplayname(filename))
    return list

def info(info):
    outLog = "[" + time.strftime("%H:%M:%S", time.localtime()) + "] " + Fore.YELLOW + Style.BRIGHT + info + Style.RESET_ALL
    logs.append(outLog)
    try:
        tools.appendToFile(logFile, outLog)
    except:
        pass
    print(outLog)

def success(success):
    outLog = "[" + time.strftime("%H:%M:%S", time.localtime()) + "] " + Fore.GREEN + Style.BRIGHT + success + Style.RESET_ALL
    logs.append(outLog)
    try:
        tools.appendToFile(logFile, outLog)
    except:
        pass
    print(outLog)

def error(error):
    outLog = "[" + time.strftime("%H:%M:%S", time.localtime()) + "] " + Fore.RED + Style.BRIGHT + error + Style.RESET_ALL
    logs.append(outLog)
    try:
        tools.appendToFile(logFile, outLog)
    except:
        pass
    print(outLog)

def writeToLogFile(message):
    outLog = "§f" + "[" + time.strftime("%H:%M:%S", time.localtime()) + "] §r" + message
    try:
        tools.appendToFile(logFile, outLog)
    except:
        pass

def log(message):
    outLog = "§f" + "[" + time.strftime("%H:%M:%S", time.localtime()) + "] §r" + message
    logs.append(outLog)
    try:
        tools.appendToFile(logFile, outLog)
    except:
        pass
    if "§r" in message:
        message = message.replace("§r", Fore.RESET)
    if "§1" in message:
        message = message.replace("§1", Fore.BLUE)
    if "§9" in message:
        message = message.replace("§9", Fore.LIGHTBLUE_EX)
    if "§b" in message:
        message = message.replace("§b", Fore.LIGHTCYAN_EX)
    if "§3" in message:
        message = message.replace("§3", Fore.CYAN)
    if "§4" in message:
        message = message.replace("§4", Fore.RED)
    if "§c" in message:
        message = message.replace("§c", Fore.LIGHTRED_EX)
    if "§6" in message:
        message = message.replace("§6", Fore.YELLOW)
    if "§e" in message:
        message = message.replace("§e", Fore.LIGHTYELLOW_EX)
    if "§a" in message:
        message = message.replace("§a", Fore.LIGHTGREEN_EX)
    if "§2" in message:
        message = message.replace("§2", Fore.GREEN)
    if "§5" in message:
        message = message.replace("§5", Fore.MAGENTA)
    if "§d" in message:
        message = message.replace("§d", Fore.LIGHTMAGENTA_EX)
    if "§f" in message:
        message = message.replace("§f", Fore.WHITE)
    if "§7" in message:
        message = message.replace("§7", Fore.LIGHTWHITE_EX)
    if "§8" in message:
        message = message.replace("§8", Fore.LIGHTBLACK_EX)
    if "§0" in message:
        message = message.replace("§0", Fore.BLACK)
    print("[" + time.strftime("%H:%M:%S", time.localtime()) + "] " + Style.RESET_ALL + Style.BRIGHT + message + Style.RESET_ALL)
