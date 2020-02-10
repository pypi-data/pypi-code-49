# coding: utf-8
import sys
import os
import io
import json
from xml.etree import ElementTree as ET
from pyWebFramework.dll.IeWebFramework import TaskManager as TaskManagerBase, RunJsException, IeCore
from pyWebFramework.core.settings import settings
import importlib


def prettyXml(xml_str, indent, newline, level=0):  # elemnt为传进来的Elment类，参数indent用于缩进，newline用于换行
    element = ET.fromstring(xml_str)

    def _prettyXml(element, indent, newline, level=0):
        if element:  # 判断element是否有子元素
            if element.text == None or element.text.isspace():  # 如果element的text没有内容
                element.text = newline + indent * (level + 1)
            else:
                element.text = newline + indent * (level + 1) + element.text.strip() + newline + indent * (level + 1)
                # else:  # 此处两行如果把注释去掉，Element的text也会另起一行
            # element.text = newline + indent * (level + 1) + element.text.strip() + newline + indent * level
        temp = list(element)  # 将elemnt转成list
        for subelement in temp:
            if temp.index(subelement) < (len(temp) - 1):  # 如果不是list的最后一个元素，说明下一个行是同级别元素的起始，缩进应一致
                subelement.tail = newline + indent * (level + 1)
            else:  # 如果是list的最后一个元素， 说明下一行是母元素的结束，缩进应该少一个
                subelement.tail = newline + indent * level
            _prettyXml(subelement, indent, newline, level=level + 1)  # 对子元素进行递归操作

    _prettyXml(element, indent, newline, level)

    if not isinstance(element, ET.ElementTree):
        element = ET.ElementTree(element)

    sio = io.StringIO()
    element.write(sio, encoding="unicode")
    tail = element.getroot().tail
    if not tail or tail[-1] != "\n":
        sio.write("\n")
    return sio.getvalue()


class TaskManager(TaskManagerBase):
    current_task = None

    def __init__(self, tasks):
        super(TaskManager, self).__init__()
        self.tasks = tasks
        self.task_insts = []

    def OnCreateTask(self, taskId, taskType):
        print('on create task: id=%s type=%s' % (taskId, taskType))

        for task_inst in self.task_insts:
            if task_inst.id == taskId and task_inst.type == taskType:
                TaskManager.current_task = task_inst
                self.SetCreatedTaskInst(task_inst)
                return

        for task_cls in self.tasks:
            if task_cls.id == taskId and task_cls.type == taskType:
                task_inst = task_cls()
                # setattr(task_inst, 'task_manager', self)
                task_inst.task_manager = self
                self.task_insts.append(task_inst)
                TaskManager.current_task = task_inst
                self.SetCreatedTaskInst(task_inst)
                return
        print('Unknown task id=%s type=%s' % (taskId, taskType))

    def OnReleaseTask(self, task_inst):
        if TaskManager.current_task == task_inst:
            TaskManager.current_task = None

        if task_inst in self.task_insts:
            # delattr(task_inst, 'task_manager')
            task_inst.task_manager = None
            task_inst.PyOnRelease()
            task_inst.OnReleaseAllPages()
            self.task_insts.remove(task_inst)

    def OnReleaseAllTasks(self):
        TaskManager.current_task = None

        while len(self.task_insts):
            task_inst = self.task_insts.pop()
            # delattr(task_inst, 'task_manager')
            task_inst.task_manager = None
            task_inst.PyOnRelease()
            task_inst.OnReleaseAllPages()


class ModuleBase(object):
    tasks = []
    ie = IeCore.IE_DEF

    def run(self, task_file=''):
        self.__init_settings__()

        tm = TaskManager(self.tasks)

        if not task_file:
            task_file = 'task.json'

        if not os.path.exists(task_file):
            print('任务文件没找到: ' + task_file)
            return False

        json_file = ''
        xml_file = task_file

        # 传入json任务文件，生成xml文件
        if task_file.endswith('.json'):
            json_file = task_file

            xml_file = task_file[:-5] + '.xml'

            json_str = open(task_file, 'rb').read().decode('gb2312', 'ignore')

            j = json.loads(json_str)
            xml_str = j['data']

            xml_str = prettyXml(xml_str, '\t', '\n')

            open(xml_file, 'w', encoding='utf-8').write(xml_str)

            task_file = xml_file

        if self.ie == IeCore.IE_DEF:
            self.ie = IeCore.IE_11  # 默认改为ie11

        success = tm.DoTask(task_file, self.ie)

        # 任务跑完后将xml结果写回json文件
        if json_file:
            xml_str = open(xml_file, 'rb').read().decode('utf-8', 'ignore')
            json_str = open(json_file, 'rb').read().decode('gb2312', 'ignore')
            j = json.loads(json_str)

            xml_str = prettyXml(xml_str, '', '')

            status, message = self.__get_result_from_xml(xml_str)

            j['data'] = xml_str
            j['status'] = status
            j['message'] = message

            json_str = json.dumps(j, ensure_ascii=False, indent='   ')
            open(json_file, 'w', encoding='gb2312').write(json_str)

        return success

    def __init_settings__(self):
        try:
            module_settings = importlib.import_module("settings")
            settings.load_settings(module_settings)
        except ModuleNotFoundError:
            pass

    def __get_result_from_xml(self, xml_str):
        xml_root = ET.fromstring(xml_str)
        xml_TaskSet = xml_root.find('TaskSet')
        xml_Task = xml_TaskSet.find('Task')

        last_code = ''
        last_desc = ''
        for xml_TableSet in xml_Task.findall('TableSet'):
            xml_Result = xml_TableSet.find('Result')
            if not xml_Result:
                continue

            xml_Code = xml_Result.find('Code')
            xml_Desc = xml_Result.find('Desc')

            if not xml_Code.text.startswith('200'):
                return xml_Code.text, xml_Desc.text
            else:
                last_code = xml_Code.text
                last_desc = xml_Desc.text

        return last_code, last_desc
