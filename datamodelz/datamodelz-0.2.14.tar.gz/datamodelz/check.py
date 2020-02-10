import logging

from datamodelz.error import Error


class Check:
    """
    Takes a list of DataObject and runs the function on the entire list. Returns an error string.
    """
    def __init__(self, name: str, funct) -> None:
        self.name = name
        self.funct = funct

    def run(self, data_lst, metadata=None, other_data=None) -> str:
        logging.debug("running check {}".format(self.name))
        return self.funct(data_lst, metadata, other_data)


class CheckEach(Check):
    """
    Takes a list of DataObject and runs the function on each DataObject within the list. Returns an error string.
    """
    def __init__(self, name: str, funct) -> None:
        super().__init__(name, funct)

    def run(self, data_lst, metadata=None, other_data=None) -> str:
        errors = []
        logging.debug("running check all {}".format(self.name))
        for obj in data_lst:
            error = self.funct(obj, metadata, other_data)
            if not error.empty():
                errors.append(error)
        return errors

class BusinessCheck(Check):
    def __init__(self, name: str, funct) -> None:
        super().__init__(name, funct)

    def run(self, data_lst) -> Error:
        logging.debug("running check {}".format(self.name))
        return self.funct(data_lst)

class BusinessCheckEach(Check):
    """
    Takes a list of DataObject and runs the function on each DataObject within the list. Returns an error string.
    """
    def __init__(self, name: str, funct) -> None:
        super().__init__(name, funct)

    def run(self, data_lst) -> Error:
        logging.debug("running check each {}".format(self.name))
        for obj in data_lst:
            error = self.funct(obj)
            if error:
                return error
        return Error()
