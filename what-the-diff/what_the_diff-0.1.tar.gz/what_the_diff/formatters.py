from termcolor import colored


class Removed:
    """
    Removed text info from old to new

    Properties:

    lines - Removed line numbers in the old file
    sentences - Removed sentences corresponding to the line numbers

    Method:

    format() - returns colored output of the removed text information
    id() - returns the line which the change begins, the id is used for sorting with other change formatters
    """

    def __init__(self, lines, sentences):
        self.lines = lines
        self.sentences = sentences

    def id(self):
        return min(self.lines)

    def format(self):
        if len(self.lines) == 0:
            return ""
        min_line = self.lines[0]
        max_line = self.lines[-1]

        return f"{min_line},{max_line}d{max_line+1}\n" + "\n".join([f"{colored('<', 'red')} {colored(i, 'red')}" for i in self.sentences])


class Added:
    """
    Added text info from old to new

    Properties:

    lines - Added line numbers in the old file
    sentences - Added sentences corresponding to the line numbers

    Methods:

    format() - returns colored output of the added text information
    id() - returns the line which the change begins, the id is used for sorting with other change formatters
    """

    def __init__(self, lines, sentences):
        self.lines = lines
        self.sentences = sentences

    def id(self):
        return min(self.lines)

    def format(self):
        min_line, max_line = min(self.lines), max(self.lines)

        return f"{min_line}a{min_line+1},{max_line+1}\n" + "\n".join([f"{colored('>', 'green')} {colored(i, 'green')}" for i in self.sentences])


class Updated:
    """
    Updated text info from old to new

    Properties:

    lines - Updated line numbers in the new file
    sentences - Updated sentences corresponding to the line numbers

    Methods:

    format() - returns colored output of the updated text information
    id() - returns the line which the change begins, the id is used for sorting with other change formatters
    """

    def __init__(self, lines, sentences):
        self.lines = lines
        self.sentences = sentences

    def id(self):
        return self.lines[0]

    def format(self):
        self.lines
        return f"{self.lines[0]+1}c{self.lines[1]+1}\n" + colored(f"< {self.sentences[0]}\n", "red") + "---\n" + colored(f"> {self.sentences[1]}", "green")
