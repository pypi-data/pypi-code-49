import random, json, os, codecs, shutil

def getFileContent(path):
    with codecs.open(path, 'r', encoding='utf8') as file:
        content = file.readlines()
        lines = []
        file.close()
        for line in content:
            lines.append(line.replace("\n", ""))
        return lines

def getLineFromFile(path, line):
    file = open(path, "r")
    content = file.readlines()
    file.close()
    return content[line].replace("\n", "")

def getRandomLineFromFile(path):
    file = open(path, "r")
    content = file.readlines()
    file.close()
    return (content[random.randint(0, len(content) - 1)]).replace("\n", "")

def appendToFile(path, text):
    with codecs.open(path, 'a', encoding='utf8') as file:
        file.write(text + "\n")
        file.close()

def writeToFile(path, text):
    with codecs.open(path, 'w', encoding='utf8') as file:
        file.write(text + "\n")
        file.close()

def removeFromFile(path, text):
    file = open(path, "r")
    lines = file.readlines()
    file.close()
    file = open(path, "w")
    for line in lines:
        if line != text + "\n":
            file.write(line)
    file.close()

def replaceTextInFile(path, text, replacement):
    file = open(path, "r")
    lines = file.readlines()
    file.close()
    file = open(path, "w")
    for line in lines:
        if line == text + "\n":
            file.write(replacement + "\n")
        else:
            file.write(line)
    file.close()

def getFirstLineFromFileAndRemoveLine(path):
    file = open(path, "r")
    content = file.readlines()
    file.close()
    file = open(path, "w")
    for line in content:
        if line != content[0]:
            file.write(line)
    file.close()
    return content[0].replace("\n", "")

def createFile(path):
    file = open(path, "w")
    file.close()

def createDirectory(path):
    try:
        os.mkdir(path)
    except:
        pass

def clearFile(path):
    file = open(path, "w")
    file.close()

def existFile(path):
    return os.path.isfile(path)

def existDirectory(path):
    return os.path.isdir(path)

def copyFile(file, dir_path):
    if os.path.isdir(file):
        createDirectory(dir_path + "\\" + os.path.basename(file))
        for f in os.listdir(file):
            copyFile(file + "\\" + f, dir_path + "\\" + os.path.basename(file))
    else:
        shutil.copyfile(file, dir_path + "\\" + os.path.basename(file))

def removeFile(path):
    os.remove(path)

def clearDirectory(path):
    for f in os.listdir(path):
        if os.path.isdir(path + "\\" + f):
            clearDirectory(path + "\\" + os.path.basename(f))
        else:
            removeFile(path + "\\" + f)

def loadJson(path):
    with open(path, "r", encoding='utf-8') as json_data:
        data = json.load(json_data)
        json_data.close()
        return data

def saveJson(path, data):
    with open(path, "w", encoding='utf-8') as json_data:
        json.dump(data, json_data)
        json_data.close()
