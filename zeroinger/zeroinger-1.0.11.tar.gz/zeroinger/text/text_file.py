from logzero import logger


class TextFile:
    @staticmethod
    def load_lines(file_path: str, encoding: str = 'utf-8') -> list:
        """
        :param file_path: file path
        :param encoding: default utf-8 
        :return: list of line 
        """
        data = []
        inf = open(file_path, 'r', encoding=encoding)
        for line in inf:
            # delete \n in the end
            data.append(line.replace('\n', ''))
        inf.close()
        return data
        pass

    @staticmethod
    def dump_lines(file_path: str, list_of_line: list, encoding: str = 'utf-8') -> None:
        """
        :param file_path: 
        :param list_of_line: 
        :param encoding: 
        :return: 
        """
        outf = open(file_path, 'w', encoding=encoding)
        for line in list_of_line:
            if not line is None:
                outf.write(line + '\n')
        outf.close()
        pass

    @staticmethod
    def load_dict(file_path: str, encoding: str = 'utf-8', delimiter: str = '\t') -> dict:
        """
        文件中包含多行，每个多个元素，以 delimiter代表的字符作为分割，载入为dict
        :param file_path: 
        :param encoding: 
        :param delimiter: 
        :return: 
        """
        data = {}
        inf = open(file_path, 'r', encoding=encoding)
        for line in inf:
            line = line.strip()
            box = line.split(delimiter)
            if len(box) == 2:
                data[box[0]] = box[1]
        inf.close()

        return data

    @staticmethod
    def dump_dict(file_path: str, dict_data: dict, encoding: str = 'utf-8', delimiter: str = '\t') -> None:
        """
        :param file_path: 
        :param dict_data: 
        :param encoding: 
        :param delimiter: 
        :return: 
        """
        outf = open(file_path, 'w', encoding=encoding)
        for key in dict_data:
            value = str(dict_data[key])
            if value is not None:
                outf.write('{}{}{}\n'.format(key, delimiter, value))
        outf.close()
        pass
