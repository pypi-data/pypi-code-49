from threading import Timer
import os
from optimeed.core.tools import getPath_workspace
from abc import abstractmethod, ABCMeta
from .myjson import obj_to_json, json_to_obj, json_to_obj_safe, encode_str_json, decode_str_json, SaveableObject
import json
from .tools import indentParagraph, rgetattr, applyEquation, printIfShown, SHOW_WARNING
import copy
try:
    import pandas as pd
except ModuleNotFoundError:
    printIfShown("Failed to import pandas. Excel export might fail.", SHOW_WARNING)


class DataStruct_Interface(metaclass=ABCMeta):
    def __init__(self):
        self.info = ''

    @abstractmethod
    def save(self, filename):
        """Save the datastructure to filename"""
        pass

    @staticmethod
    @abstractmethod
    def load(filename, **kwargs):
        """Load the datastructure from filename"""
        pass

    def get_info(self):
        """Get simple string describing the datastructure"""
        return self.info

    def set_info(self, info):
        """Set simple string describing the datastructure"""
        self.info = info

    @staticmethod
    def get_extension():
        """File extension used for datastructure"""
        return ".json"

    def __str__(self):
        return str(self.info)


class AutosaveStruct:
    """Structure that provides automated save of DataStructures"""
    def __init__(self, dataStruct, filename='', change_filename_if_exists=True):
        if not filename:
            self.filename = getPath_workspace() + '/default_collection'
        else:
            self.filename = os.path.abspath(filename)

        self.theDataStruct = dataStruct

        self.set_filename(self.filename, change_filename_if_exists)
        self.timer = None

    def __str__(self):
        return str(self.theDataStruct)

    def get_filename(self):
        """Get set filename"""
        return self.filename

    def set_filename(self, filename, change_filename_if_exists):
        """

        :param filename: Filename to set
        :param change_filename_if_exists: If already exists, create a new filename
        """
        if not filename.endswith(self.theDataStruct.get_extension()):
            filename += self.theDataStruct.get_extension()

        if change_filename_if_exists:
            curr_index = 1
            head, tail = os.path.split(filename)
            base_name = os.path.splitext(tail)[0]
            while os.path.exists(filename):
                filename = head + '/' + base_name + '_' + str(curr_index) + self.theDataStruct.get_extension()
                curr_index += 1
        self.filename = filename

    def stop_autosave(self):
        """Stop autosave"""
        if self.timer is not None:
            self.timer.cancel()

    def start_autosave(self, timer_autosave):
        """Start autosave"""
        self.save()
        if timer_autosave > 0:
            self.timer = Timer(timer_autosave, lambda: self.start_autosave(timer_autosave))
            self.timer.daemon = True
            self.timer.start()

    def save(self, safe_save=True):
        """Save"""
        if not os.path.exists(os.path.dirname(self.filename)):
            os.makedirs(os.path.dirname(self.filename))

        if os.path.exists(self.filename) and safe_save:
            temp_file = self.filename + 'temp'
            self.theDataStruct.save(temp_file)
            os.replace(temp_file, self.filename)
        else:
            self.theDataStruct.save(self.filename)

    def get_datastruct(self):
        """Return :class:'~DataStruct_Interface'"""
        return self.theDataStruct

    def __getstate__(self):
        state = self.__dict__.copy()
        del state["timer"]
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        self.timer = None


class ListDataStruct(DataStruct_Interface):
    _INFO_STR = "info"
    _DATA_STR = "data"

    def __init__(self):
        super().__init__()
        self.theData = list()

    def save(self, filename):
        """Save data using json format. The data to be saved are automatically detected, see :meth:`~optimeed.core.myjson.obj_to_json` """
        theStr = '{{\n\t"{}": "{},\n'.format(ListDataStruct._INFO_STR, encode_str_json(self.get_info()))

        listStr = "[\n"
        for k, item in enumerate(self.theData):
            listStr += "\t" + json.dumps(obj_to_json(item))
            if k < len(self.theData)-1:
                listStr += ",\n"
        listStr += "\n]"

        theStr += '\t"{}": \n{}'.format(ListDataStruct._DATA_STR, indentParagraph(listStr, 3))
        theStr += "}"

        with open(filename, "w", encoding='utf-8') as f:
            f.write(theStr)

    @staticmethod
    def load(filename, theClass=None):
        """
        Load the file filename.

        :param filename: file to load
        :param theClass: optional. Can be used to fix unpickling errors.
        :return: self-like object
        """
        if filename:
            if not os.path.splitext(filename)[-1].lower():
                filename += ListDataStruct.get_extension()

            try:
                newStruct = ListDataStruct()
                with open(filename, 'r') as f:
                    theDict = json.load(f)
                newStruct.set_info(decode_str_json(theDict[ListDataStruct._INFO_STR]))
                if theClass is not None:
                    theData = [json_to_obj_safe(item, theClass) for item in theDict[ListDataStruct._DATA_STR]]
                else:
                    theData = [json_to_obj(item) for item in theDict[ListDataStruct._DATA_STR]]
                newStruct.set_data(theData)
                return newStruct
            except TypeError as e:
                printIfShown("{}, recommended to use theclass keyword in method load".format(e), SHOW_WARNING)
            except OSError:
                printIfShown("Could not read file ! " + filename, SHOW_WARNING)
            except EOFError:
                printIfShown("File empty ! " + filename, SHOW_WARNING)
        else:
            printIfShown("INVALID COLLECTION FILENAME: " + filename, SHOW_WARNING)

    def add_data(self, data_in):
        """Add a data to the list"""
        self.theData.append(copy.deepcopy(data_in))

    def get_data(self):
        """Get full list of datas"""
        return self.theData

    def set_data(self, theData):
        """Set full list of datas"""
        self.theData = theData

    def set_data_at_index(self, data_in, index):
        """Replace data at specific index"""
        self.theData[index] = data_in

    def set_attribute_data(self, the_attribute, the_value):
        """Set attribute to all data"""
        for item in self.get_data():
            setattr(item, the_attribute, the_value)

    def set_attribute_equation(self, attribute_name, equation_str):
        """
        Advanced method to set the value of attribute_name from equation_str

        :param attribute_name: string (name of the attribute to set)
        :param equation_str: formatted equation, check :meth:`~optimeed.core.CommonFunctions_Library.applyEquation`
        :return:
        """
        for item in self.get_data():
            setattr(item, attribute_name, applyEquation(item, equation_str))

    def get_list_attributes(self, attributeName):
        """
        Get the value of attributeName of all the data in the Collection

        :param attributeName: string (name of the attribute to get)
        :return: list
        """
        if not attributeName:
            return list()
        return [rgetattr(data, attributeName) for data in self.theData]

    # def coherence(self):
    #     """
    #     Call that method to ensure that all the elements are properly instantiated.
    #     This method calls the method "assign" from the data structure. If None: skip
    #     """
    #     newData = [None] * len(self.get_data())
    #     for index, item in enumerate(self.get_data()):
    #         newItem = item.__class__()
    #         try:
    #             newItem.assign(item)
    #         except AttributeError:
    #             pass
    #         newData[index] = newItem
    #     self.theData = newData

    def delete_points_at_indices(self, indices):
        """
        Delete several elements from the Collection

        :param indices: list of indices to delete
        """
        for index in sorted(indices, reverse=True):
            del self.get_data()[index]

    def export_xls(self, excelFilename, excelsheet='Sheet1', mode='w'):
        """Export the collection to excel. It only exports the direct attributes.

        :param excelFilename: filename of the excel
        :param excelsheet: name of the sheet
        :param mode: 'w' to erase existing file, 'a' to append sheetname to existing file
        """
        if len(self.get_data()):
            attributes = list(vars(self.get_data()[0]).keys())
            dictToExport = dict()
            for attribute in attributes:
                dictToExport[attribute] = [float(rgetattr(data, attribute)) for data in self.theData]

            writer = pd.ExcelWriter(excelFilename)
            if mode == 'a':
                try:
                    alldata = pd.read_excel(excelFilename, sheet_name=None)
                    for key in alldata:
                        alldata[key].to_excel(writer, sheet_name=key, index=False)
                except FileNotFoundError:
                    pass
            df = pd.DataFrame(dictToExport)
            df.to_excel(writer, sheet_name=excelsheet, index=False)
            writer.save()

    def merge(self, collection):
        """
        Merge a collection with the current collection

        :param collection: :class:`~optimeed.core.Collection.Collection` to merge
        """
        for item in collection.get_data():
            self.add_data(item)
