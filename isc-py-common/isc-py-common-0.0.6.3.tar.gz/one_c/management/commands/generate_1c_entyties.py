import configparser
import logging
import os
import shutil
from tkinter import *

from django.core.management import BaseCommand
from transliterate import translit
from transliterate.exceptions import LanguageDetectionError

from code_generator.core.writer_model import WriterModel
from one_c.models.entity_1c import Entity_1c
from one_c.models.one_c_params_entity_view import One_c_params_entity_view
from project import settings

logger = logging.getLogger(__name__)


class ExceptionOnDocLoading(Exception):
    pass


class Command(BaseCommand):
    config = configparser.ConfigParser()
    config['DEFAULT'] = {}

    config.sections()
    config.read('config.ini')

    help = "Создание мат вьюшек для документов из 1С"
    root = Tk()

    def fill_space(self, qty):
        res = ''
        while True:
            res += ' '
            qty -= 1
            if qty == 0:
                return res

    def uncapitalize(self, str):
        return str[0:1].lower() + str[1:]

    def dbl_qutes_str(self, str):
        return f'"{str}"'

    def qutes_str(self, str):
        return f"'{str}'"

    def handle(self, *args, **options):
        try:
            if not os.path.exists(settings.ONE_C_DIR):
                raise Exception(f'Path: {settings.ONE_C_DIR} not exists.')

            if not os.path.exists(settings.BASE_PATH_TEMPLATE):
                raise Exception(f'Path: {settings.BASE_PATH_TEMPLATE} not exists.')

            group_replace_map = dict(
                ITEMS=[],
                GROUP_NAME="ONE_C",
                ICON="Common.ur_entity",
                TITLE="Пользователи",
                TITLE_BUTTON="1С",
            )

            isc_replace_map = dict(
                ITEMD_EDITOR=[]
            )

            common_urls_file = f'{settings.ONE_C_DIR}{os.sep}common_urls.py'
            writerCommonUrls = WriterModel(path_output=common_urls_file, template_path=f'{settings.BASE_PATH_TEMPLATE}{os.sep}templates{os.sep}common_urls.pmd')

            isc_fields = isc_replace_map.get('ITEMD_EDITOR')
            isc_fields.append(f'{self.fill_space(2)}readonly {group_replace_map.get("GROUP_NAME")} : {group_replace_map.get("GROUP_NAME")}Statics;')
            isc_output_file = f'{settings.ONE_C_DIR}{os.sep}ts{os.sep}Isc.ts'
            writerIsc = WriterModel(path_output=isc_output_file, template_path=f'{settings.BASE_PATH_TEMPLATE}{os.sep}templates{os.sep}Isc.pmd')

            group_items = group_replace_map.get('ITEMS')
            group_output_file = f'{settings.ONE_C_DIR}{os.sep}ts{os.sep}groups{os.sep}group_one_c.ts'
            writerGroup = WriterModel(path_output=group_output_file, template_path=f'{settings.BASE_PATH_TEMPLATE}{os.sep}templates{os.sep}group.pmd')

            model_output_dir = f'{settings.ONE_C_DIR}{os.sep}models'
            if os.path.exists(model_output_dir):
                shutil.rmtree(model_output_dir)
            os.makedirs(model_output_dir)

            views_output_dir = f'{settings.ONE_C_DIR}{os.sep}views'
            if os.path.exists(views_output_dir):
                shutil.rmtree(views_output_dir)
            os.makedirs(views_output_dir)

            urls_output_dir = f'{settings.ONE_C_DIR}{os.sep}urls'
            if os.path.exists(urls_output_dir):
                shutil.rmtree(urls_output_dir)
            os.makedirs(urls_output_dir)

            datasource_output_dir = f'{settings.ONE_C_DIR}{os.sep}ts{os.sep}datasources'
            if os.path.exists(datasource_output_dir):
                shutil.rmtree(datasource_output_dir)
            os.makedirs(datasource_output_dir)

            list_grid_editor_output_dir = f'{settings.ONE_C_DIR}{os.sep}ts{os.sep}editors'
            if os.path.exists(list_grid_editor_output_dir):
                shutil.rmtree(list_grid_editor_output_dir)
            os.makedirs(list_grid_editor_output_dir)

            menu_item_output_dir = f'{settings.ONE_C_DIR}{os.sep}ts{os.sep}menu_items'
            if os.path.exists(menu_item_output_dir):
                shutil.rmtree(menu_item_output_dir)
            os.makedirs(menu_item_output_dir)

            common_urls_map = dict(
                LIST_PATH=[]
            )
            common_urls = common_urls_map.get('LIST_PATH')

            for entity in sorted(Entity_1c.objects.filter(), key=lambda record: record.code):
                try:
                    entity_code = translit(entity.code, reversed=True).replace("'", '')
                except LanguageDetectionError:
                    entity_code = entity.code

                model_name = f'{entity_code}_model'
                common_urls.append(f'{self.fill_space(4)}path({self.qutes_str("logic/")}, include({self.qutes_str("kaf_pas.k_one_c.urls." + self.uncapitalize(entity_code))})),')

                model_output_file = f'{model_output_dir}{os.sep}{self.uncapitalize(entity_code)}.py'
                views_output_file = f'{views_output_dir}{os.sep}{self.uncapitalize(entity_code)}.py'
                urls_output_file = f'{urls_output_dir}{os.sep}{self.uncapitalize(entity_code)}.py'

                datasource_output_file = f'{datasource_output_dir}{os.sep}{self.uncapitalize(entity_code)}.ts'
                list_grid_editor_output_file = f'{list_grid_editor_output_dir}{os.sep}{self.uncapitalize(entity_code)}.ts'
                menu_item_output_file = f'{menu_item_output_dir}{os.sep}{self.uncapitalize(entity_code)}.ts'

                writerModel = WriterModel(path_output=model_output_file, template_path=f'{settings.BASE_PATH_TEMPLATE}{os.sep}templates{os.sep}model.pmd')
                writerViews = WriterModel(path_output=views_output_file, template_path=f'{settings.BASE_PATH_TEMPLATE}{os.sep}templates{os.sep}views.pmd')
                writerUrls = WriterModel(path_output=urls_output_file, template_path=f'{settings.BASE_PATH_TEMPLATE}{os.sep}templates{os.sep}urls.pmd')

                writerDatasource = WriterModel(path_output=datasource_output_file, template_path=f'{settings.BASE_PATH_TEMPLATE}{os.sep}templates{os.sep}datasource.pmd')
                writerListEditor = WriterModel(path_output=list_grid_editor_output_file, template_path=f'{settings.BASE_PATH_TEMPLATE}{os.sep}templates{os.sep}list_grid_editor.pmd')
                writerMennuItem = WriterModel(path_output=menu_item_output_file, template_path=f'{settings.BASE_PATH_TEMPLATE}{os.sep}templates{os.sep}menu_item.pmd')

                model_replace_map = dict(
                    QUERY_SET="pass",
                    NAME_MODEL=model_name,
                    FIELDS_MAPPING='',
                    FIELDS=[
                        f'{self.fill_space(4)}entity = ForeignKeyProtect(Entity_1c)',
                        f'{self.fill_space(4)}ref = UUIDField(primary_key=True)'
                    ],
                    IMPORTS=[
                        'from django.db.models import Model',
                        'from django.db.models import UUIDField, TextField',
                        'from isc_common.fields.related import ForeignKeyProtect',
                        'from one_c.models.entity_1c import Entity_1c',
                    ],
                    _STR_='f"(ref: {self.ref}, entity: {self.entity})"',
                    META=[
                        f'{self.fill_space(8)}managed = False',
                        f'{self.fill_space(8)}db_table = "{entity_code}_mview"'
                    ]
                )

                view_replace_map = dict(
                    PACKAGE_MODEL_MANAGER=f'from kaf_pas.k_one_c.models.{self.uncapitalize(entity_code)} import {entity_code}_model, {entity_code}_modelManager',
                    NAME_MODEL=model_name,
                )

                url_replace_map = dict(
                    PACKAGE_MODEL=f'from kaf_pas.k_one_c.views import {self.uncapitalize(entity_code)}',
                    PACKAGE_VIEW=entity_code,
                    LPACKAGE_VIEW=self.uncapitalize(entity_code),
                    NAME_MODEL=model_name,
                )

                datasource_replace_map = dict(
                    NAME_MODEL=model_name,
                    NAME_PARAM=entity_code,
                    FIELDS=[
                        f'{self.fill_space(12)}uuidField("ref", "ID", true, true, 255, false, false),'
                    ]
                )

                list_grid_editor_replace_map = dict(
                    NAME_MODEL=model_name,
                    ITEMS_TYPE=[
                        'new MiListRefresh(),'
                    ],
                    PERMISSIONS=''
                )

                menu_item_replace_map = dict(
                    NAME_MODEL=model_name,
                    NAME_PARAM=entity.code,
                    ICON="Common.ur_entity"
                )

                isc_fields.append(f'{self.fill_space(2)}readonly {model_name} : {model_name}Statics;')

                group_items.append(f'{self.fill_space(56)}get_{model_name}(ownerApp),')
                # group_items.append(f'{self.fill_space(56)}<MenuSSItem>{{isSeparator: true}},')

                model_fields = model_replace_map.get('FIELDS')
                datasource_fields = datasource_replace_map.get('FIELDS')

                for param in One_c_params_entity_view.objects.filter(entity=entity):
                    try:
                        param_code = translit(param.code, reversed=True).replace("'", '')
                    except LanguageDetectionError:
                        param_code = param.code

                    model_fields.append(f'{self.fill_space(4)}{param_code} = TextField()')
                    datasource_fields.append(f'{self.fill_space(12)}nameField("{param_code}", "{param.code}", false, false, 255, false, false),')

                logger.debug(f'Write: {model_output_file}')

                writerCommonUrls.write_entity(replace_map=common_urls_map)
                writerModel.write_entity(replace_map=model_replace_map)
                writerViews.write_entity(replace_map=view_replace_map)
                writerUrls.write_entity(replace_map=url_replace_map)
                writerDatasource.write_entity(replace_map=datasource_replace_map)
                writerListEditor.write_entity(replace_map=list_grid_editor_replace_map)
                writerMennuItem.write_entity(replace_map=menu_item_replace_map)

            writerIsc.write_entity(replace_map=isc_replace_map)
            writerGroup.write_entity(replace_map=group_replace_map)

        except ExceptionOnDocLoading as ex:
            self.root.withdraw()
            logger.error('\n !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')

            for msg_item in ex.args:
                logger.error(msg_item)

            logger.error('\n !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
