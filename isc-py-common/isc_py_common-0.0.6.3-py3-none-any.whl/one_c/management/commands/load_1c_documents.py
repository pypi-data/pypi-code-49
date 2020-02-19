import configparser
import logging
import os
from datetime import datetime
from os.path import getmtime
from tkinter import *
from tkinter import filedialog
from uuid import UUID
from xml.dom.minidom import parseString

from django.core.management import BaseCommand
from lxml import etree
from tqdm import tqdm

from isc_common import setAttr
from one_c.models.document_1c import Document_1c
from one_c.models.documents_param_1c import Documents_param_1c
from one_c.models.documents_param_cross_1c import Documents_param_cross_1c
from one_c.models.entity_1c import Entity_1c
from one_c.models.files_1c import Files_1c
from one_c.models.param_type import Param_type

logger = logging.getLogger(__name__)


class ExceptionOnDocLoading(Exception):
    pass


class V8Exch(object):
    def __init__(self, pbar, filename):
        self.filename = filename
        self.pbar = pbar
        self.started = False
        self.entities = dict()
        self.attributes = dict()
        self.step = 0
        self.tags = 0

    def start(self, tag, attrib):
        if not self.started:
            m = re.search('({.*})', tag)
            if m:
                ns = m.group(1)
                tag = tag.replace(ns, '')
                if tag == 'Data':
                    self.started = True
        else:
            index = tag.find('CatalogObject.')
            if index == -1:
                self.tag = tag
                self.param_type = self.attributes.get(tag)
                if self.param_type == None:
                    self.param_type, created = Param_type.objects.get_or_create(code=tag)
                    setAttr(self.attributes, tag, self.param_type)
            else:
                tag = tag.replace('CatalogObject.', '')
                self.tag = tag
                self.entity = self.entities.get(tag)
                if self.entity == None:
                    self.entity, created = Entity_1c.objects.get_or_create(code=tag)
                    setAttr(self.entities, tag, self.entity)

                self.step += 1
                logger.debug(f'step: {self.step}, tags: {self.tags}')

            # logger.debug(f'tag: {tag}')

    def end(self, tag):
        self.tags += 1

    def data(self, data):
        if data.strip() != '':
            # logger.debug(f'tag: {self.tag}, data: {data}')
            if self.tag == 'Ref':
                self.document, created = Document_1c.objects.get_or_create(entity=self.entity, ref=UUID(data.strip()))
                # logger.debug(f'set: document: {self.document} created: {created}')

                if self.pbar:
                    self.pbar.update(1)
            else:
                param, create = Documents_param_1c.objects.get_or_create(type=self.param_type, value=data.strip())
                Documents_param_cross_1c.objects.create(document=self.document, param=param)

                # logger.debug(f'rec document_param: {document_param}')

    def close(self):
        if self.pbar:
            self.pbar.close()


class Command(BaseCommand):
    config = configparser.ConfigParser()
    config['DEFAULT'] = {}

    config.sections()
    config.read('config.ini')

    help = "Загрузка документов из 1С"
    root = Tk()

    def _float_2_timestamp(self, value):
        return datetime.fromtimestamp(value)

    def handle(self, *args, **options):

        try:
            try:
                initialdir = self.config['DEFAULT']['1cdir']
                if not os.path.exists(initialdir):
                    initialdir = None
            except KeyError:
                initialdir = None

            self.root.filename = filedialog.askopenfilename(title="Выберите файл документов", initialdir=initialdir)
            dir, _ = os.path.split(self.root.filename)
            self.config['DEFAULT']['1cdir'] = dir
            logger.debug(f'filename : {self.root.filename}')
            self.root.withdraw()

            date_modification = self._float_2_timestamp(getmtime(self.root.filename))
            file, created = Files_1c.objects.get_or_create(real_name=self.root.filename, file_modification_time=date_modification, props=Files_1c.props.imp)

            if created:
                file = open(self.root.filename, 'r')
                data = file.read()
                file.close()
                dom = parseString(data)
                qty = len(dom.getElementsByTagName('Ref'))

                pbar = tqdm(total=qty)

                # with transaction.atomic():
                parser = etree.XMLParser(target=V8Exch(pbar, self.root.filename))
                etree.parse(self.root.filename, parser)
            else:
                logger.warning(f'Файл: {self.root.filename}, уже импортирован !')

            with open('config.ini', 'w') as configfile:
                self.config.write(configfile)
        except ExceptionOnDocLoading as ex:
            self.root.withdraw()
            logger.error('\n !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')

            for msg_item in ex.args:
                logger.error(msg_item)

            logger.error('\n !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
