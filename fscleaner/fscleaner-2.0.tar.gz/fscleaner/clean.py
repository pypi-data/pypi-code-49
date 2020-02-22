import os
import sys
import logging

DELETEFLAG = "d"
SPACEFLAG = "s"
PATHFLAG = "p"


class fsclean:

    """
    fsclean constructor

    :arg
        commands (string) : a string which contains flags
        -p for providing path
        -s for providing alternative of space in file names
        -d for deleting the files with the mentioned types

        we are in c:\\my doc\\the folder\\ and to rename
        folder names from name [the folder] to [the_folder]
        and to delete .zip files commands will be
        -p c:\\my doc\\the folder\\
        -s _
        -d .zip

        and we have to provide it in one line separated by a space
         -p c:\\my doc\\the folder\\ -s _ -d .zip

    :return
        fsclean object
    """
    def __init__(self, commands):
        command_sets = self.process(commands)
        self.path = command_sets[PATHFLAG]
        self.space = command_sets[SPACEFLAG]
        self.delete = command_sets[DELETEFLAG]

    '''activate() call this method to clean the folder and its files based on your command'''
    def activate(self):
        self.clean(self.path)

    def processFiles(self, path, fileName):
        if self.delete.__contains__(self.fileExtension(fileName)):
            os.remove(self.joinPath(path, fileName))
        else:
            os.rename(self.joinPath(path, fileName), self.joinPath(path, self.newFormat(fileName)))

    def processDirectory(self, fileName, fileNames, path, pos):
        directoryName = fileName
        newDirectoryName = self.newFormat(directoryName)
        fileNames[pos] = newDirectoryName
        os.rename(self.joinPath(path, directoryName), self.joinPath(path, newDirectoryName))
        self.clean(self.joinPath(path, newDirectoryName))

    def newFormat(self, fileName):
        delimiter = ""
        if (self.space != ""):
            delimiter = self.space
        return fileName.replace(" ", delimiter)

    def clean(self, path):
        file_names = list()
        try:
            file_names = os.listdir(path)
        except FileNotFoundError:
            logging.basicConfig(filename='error.log', level=logging.ERROR)
            logging.error('No folder found with path' + path)
            return

        fileCount = len(file_names)
        if fileCount == 0:
            return
        for pos in range(fileCount):
            file_name = file_names[pos]
            if self.isDirectory(self.joinPath(path, file_name)):
                self.processDirectory(file_name, file_names, path, pos)
            elif self.isFile(self.joinPath(path, file_name)):
                self.processFiles(path, file_name)

    def isDirectory(self, path):
        return os.path.isdir(path)

    def isFile(self, path):
        return os.path.isfile(path)

    def fileExtension(self, path):
        return os.path.splitext(path)[1]

    def joinPath(self, portion1, portion2):
        return os.path.join(portion1, portion2)


    def process(self, commands):
        command_sequences = commands.split("-")
        command_sets = {DELETEFLAG: [], SPACEFLAG: "", PATHFLAG: ""}
        for command_sequence in command_sequences:
            if command_sequence != "":
                command = command_sequence[0]
                command_input = command_sequence[1:].strip()
                if command_sets.__contains__(command):
                    if command == DELETEFLAG:
                        command_sets[command] = set(command_input.split(" "))
                    else:
                        command_sets[command] = command_input
                else:
                    print("unknown option -" + command_sequence[0])
        return command_sets


