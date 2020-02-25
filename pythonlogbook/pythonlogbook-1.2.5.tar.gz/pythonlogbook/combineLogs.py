# the goal of this program is to combine all logs into one log file
#The code below works like this:
#a list is made that contains all the contents of a folder
#The list is then sorted so that the files that start with lower numbers are put at the front and files with higher numbers are put at the back
#The while loop then travels up the list, starting from the bottom and does the same thing for subfolders
#Once the date folder is entered, the files are read and written to output folder
import os

from mdutils.mdutils import MdUtils

originalPath = r"/home/luke/Documents/logbook"
saveLocation = r"/home/luke/Documents"
outputFileLocation = "/home/luke/Documents" + "/output.txt"

def main():
    createFile()

    #I feel like I could put this in the makeFolderList function somehow
    yearFolders = os.listdir(originalPath)
    yearFolders.sort() #Sort in Ascending numeric order

    #Not sure if putting parameters here is the best practice but it seems like the only way it will work
    dateParameters = ["none"]
    monthParameters = [dateParameters]
    yearParameters = [originalPath, yearFolders, monthParameters]

    makeFolderList(*yearParameters)
    removeExtraLines()
    print("Logs combined")

def makeMd():
    main()
    lastDate = 0
    lastMonth = 0
    lastYear = 0
    lastTime = ""
    os.chdir(saveLocation)
    mdOutputLocation = saveLocation + 'logbook.md'
    if os.path.exists(mdOutputLocation): #If file output.txt exists, remove it. If it doesn't, create it
        os.remove(mdOutputLocation)

    mdFile = MdUtils(file_name='logbook',title='My Logbook')
    with open(outputFileLocation, "r") as textDoc:
        lines = textDoc.readlines()
    for line in lines:
        firstTwoDigits = line[:2]
        if firstTwoDigits.isdigit():

            date = line[:2]
            month = line[3:5]
            year = line[6:10]
            lastTime = line[11:19]

            if year != lastYear:
                mdFile.new_header(level=1, title=year)
                lastYear = year

            if month != lastMonth:
                monthWorded = monthToWords(month)
                mdFile.new_header(level=2, title=monthWorded)
                lastMonth = month

            if date != lastDate:
                mdFile.new_header(level=3, title=date)
                lastDate = date
        if (firstTwoDigits.isdigit() == False) and (line != "\n"):
            entryContent = lastTime + " - " + line
            mdFile.new_paragraph(entryContent)
    mdFile.create_md_file()
    print("md file created")
    
def createFile():
    if os.path.exists(outputFileLocation): #If file output.txt exists, remove it. If it doesn't, create it
        os.remove(outputFileLocation)
    else:
        open(outputFileLocation, 'a').close()
        print("Output.txt created")

def makeList(ogPath, prevList, counter):
        nextPath = ogPath + "/" + prevList[counter]
        newList = os.listdir(nextPath)
        newList.sort()
        return newList, nextPath

def makeFolderList(lastPath, currentFolderList, nextParamList): #nextListName
    count = 0
    while count < len(currentFolderList):
        nextFolderList, currentPath = makeList(lastPath, currentFolderList, count)
        if nextParamList != "none":
            makeFolderList(currentPath, nextFolderList, *nextParamList)
        elif nextParamList == "none":
            addData(nextFolderList, currentPath)
        count = count + 1

def addData(entries, dateFolderPath):
    d = 0
    while d < len(entries):
        entryPath = dateFolderPath + "/" + entries[d]
        with open(entryPath) as input:
            dateLine = input.readline()
            contentLine = input.readline()
            with open(outputFileLocation, "a") as output:
                output.writelines(dateLine)
                output.writelines(contentLine)
                output.writelines("\n")
                output.writelines("\n")
        d = d + 1

def removeExtraLines():
    lastLine = 0
    currentLine = 0
    with open(outputFileLocation, "r") as output:
        lines = output.readlines()
    with open(outputFileLocation, "w") as output:
        #deletes content of output file
        output.seek(0)
        output.truncate()

        for line in lines:
            if line == "\n":
                currentLine = 1
            else:
                currentLine = 0
            if lastLine == 0 or currentLine == 0:
                output.write(line)

            lastLine = currentLine
            currentLine = 0
    output.close()

def monthToWords(number):
    if number == "01":
        return "January"
    if number == "02":
        return "February"
    if number == "03":
        return "March"
    if number == "04":
        return "April"
    if number == "05":
        return "May"
    if number == "06":
        return "June"
    if number == "07":
        return "July"
    if number == "08":
        return "August"
    if number == "09":
        return "September"
    if number == "10":
        return "October"
    if number == '11':
        return "November"
    if number == "12":
        return "December"
makeMd()



#Sample output format
#year


#month year

#day month year
#time-"entry content"
