import re
import csv

class Copy:
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer
        self.data = list()

    def __construct(self, data):
        field = 0
        message_tmps = list()
        tmp_list = list()
        check_datetime = '\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}'
        check_datetime_message = '\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}[\]\n\w \d)]+'
        index_check = [
            '[\w\d_-]+',
            '\w+',
            check_datetime,
            '\d+',
            '\w+',
            '[\d\w]+',
            '.*\n{0,1}',
        ]
        for string in data:
            if field == 6 and string.find('\n') != -1:
                words = string.split('\n')
                tmp_list.append(words[0])
                self.data.append(tmp_list)
                tmp_list = [words[1]]
                field = 1
            elif field != 2 and re.search(index_check[field], string):
                tmp_list.append(string)
                field += 1
            elif field == 2 and re.search(index_check[field], string) and not re.search(check_datetime_message, string):
                tmp_list.append(''.join(message_tmps))
                message_tmps = list()
                tmp_list.append(string)
                field += 1
            elif field == 2:
                message_tmps.append(string)
            if field == 7:
                self.data.append(tmp_list)
                tmp_list = list()
                field = 0
        return tmp_list

    def construct_csv(self, file_path):
        reader = self.reader.read_line(file_path)
        string = reader.readline()
        new_list = re.split(',', string)
        header = new_list[0:7]
        tmp = new_list[7]
        last_header, first_field = tmp.split('\n')
        header.append(last_header)
        self.data.append(header)
        del new_list[0:8]
        new_list.insert(0, first_field)
        queue_list = list()
        for string in reader:
            new_list = re.split(',', string)
            self._transform(new_list)
            queue_list.extend(new_list)
            if self._is_complete_row(queue_list):
                self.__construct(queue_list)
                queue_list = list()
        reader.close()

    def restruct_csv(self, source_path, destination_path):
        with open(source_path, 'r') as reader, open(destination_path, 'w') as file_writer:

            writer = csv.writer(file_writer, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            string = reader.readline()
            new_list = re.split(',', string)
            header = new_list[0:7]
            tmp = new_list[7]
            last_header, first_field = tmp.split('\n')
            header.append(last_header)
            writer.writerow(header)
            queue_list = list()
            #To support case owner name is different line
            post_queue = list()
            complete_list = False
            for line in reader:
                #To support case owner name is different line
                if (3 > len(queue_list) > 0) and (re.search('\n', queue_list[0]) or re.search('\n', queue_list[1])):
                    id_match = re.search('[\w\d_-]+', line)
                    if id_match:
                        post_queue[-1][-1] = post_queue[-1][-1] + '\n' + ','.join(queue_list).rstrip()
                        writer.writerow(post_queue[0])
                        complete_list = False
                        post_queue = list()
                        queue_list = list()
                line_list = re.split(',', line)
                self._transform(line_list)
                queue_list.extend(line_list)
                if self._is_complete_row(queue_list):
                    self.__construct(queue_list)
                    queue_list = list()
                    complete_list = True
                    if len(post_queue):
                        writer.writerow(post_queue[0])
                        post_queue = list()
                        queue_list = list()
                    if len(self.data):
                        post_queue.extend(self.data)
                        self.data = list()
            if len(post_queue):
                writer.writerow(post_queue[0])
                post_queue = list()
                queue_list = list()

    def _is_complete_row(self, new_list):
        """Check whether the list including a competed row or not (already have all column)"""
        field = 0
        index_check = ['\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', '\d+', '\w+', '[\d\w]+', '.*\n{0,1}']
        if len(new_list) < 8:
            return False
        for string in new_list:
            match = re.search(index_check[field], string)
            message_match = re.search('\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}[\]\n\w \d)]+', string)
            if field == 0 and match and not message_match:
                field += 1
            elif field != 0 and match:
                field += 1
            if field == 5:
                break
        return True if field == 5 else False

    def _transform(self, new_list):
        """Concate string between line to create complete list (have all row)"""
        index = None
        for string in new_list:
            datetime_match = re.search('\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', string)
            message_match = re.search('\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}[\]\n\w \d)]+', string)
            if datetime_match and not message_match:
                index = new_list.index(string)
                break
        if index:
            if index == 2:
                tmps = new_list[:index]
                del new_list[:index]
                new_list.insert(index - 1, ','.join(tmps))

        elif len(new_list) > 3:
            tmps = new_list[2:]
            del new_list[2:]
            new_list.append(','.join(tmps))

    def construct(self, file_path):
        """Crate nested list to represent data"""
        reader = self.reader.read_line(file_path)
        queue_list = list()
        for string in reader:
            new_list = re.split(',', string)
            #To support case owner name is different line
            if (3 > len(queue_list) > 0) and (re.search('\n', queue_list[0]) or re.search('\n', queue_list[1])):
                id_match = re.search('[\w\d_-]+', string)
                if id_match:
                    self.data[-1][-1] = self.data[-1][-1] + '\n' + ','.join(queue_list)
                    queue_list = list()
            self._transform(new_list)
            queue_list.extend(new_list)
            if self._is_complete_row(queue_list):
                self.__construct(queue_list)
                queue_list = list()
        reader.close()

    def to_csv(self, file_path):
        self.writer.to_csv(self.data, file_path)
