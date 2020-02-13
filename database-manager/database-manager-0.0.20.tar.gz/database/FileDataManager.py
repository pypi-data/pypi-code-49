import logging
import os


class FileDataManager:

    def __init__(self, logger_name, tab_length=4):
        self.logger = logging.getLogger(logger_name)
        self.file = None
        self.file_path = os.path.abspath(__file__)
        self.tab = ""
        for i in range(tab_length):
            self.tab += " "

    def open(self, file_path):
        self.file_path = os.path.join(self.file_path, file_path)
        self.file = open(self.file_path, "w+")
        self.logger.info("Opened file " + self.file_path)

    def write(self, text="", tabs=0, spaces=0):
        for i in range(tabs):
            self.file.write(self.tab)
        for i in range(spaces):
            self.file.write(" ")
        self.file.write(text)
        if len(text.split("\n", 1)[0]) > 0:
            self.logger.info("Wrote \"" + text.split("\n", 1)[0] + "\" to file.")
        else:
            self.logger.info("Wrote new line(s) to file.")

    def write_line(self, text="", tabs=0, spaces=0, lines=1):
        for i in range(lines):
            text += "\n"
        self.write(text, tabs, spaces)

    def close(self):
        self.file.close()
        self.logger.info("Closed file.")
