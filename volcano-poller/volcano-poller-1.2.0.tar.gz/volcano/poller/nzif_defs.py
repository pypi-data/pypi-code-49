import os.path
import json
# import copy
# from jsonschema import validate

from volcano.general.named_parameters import DictReader

_DEFS = None
_NACK_CODES = {
    1: 'Недопустимая команда или параметр',
    2: 'Внутренняя ошибка счетчика',
    3: 'Не достаточен уровень доступа для удовлетворения запроса',
    4: 'Внутренние часы счетчика уже корректировались в течение текущих суток',
    5: 'Не открыт канал связи',
    6: 'Повторить запрос в течении 0,5 с',
    7: 'Не готов результат измерения по запрашиваемому параметру',
    8: 'Счетчик занят аналогичным процессом',
    9: 'Переполнение регистра единиц оплаты',
    10: 'Не возможно выполнить запрос управления',
}

'''
    type_code:  Код, возвращаемый счетчиком при отправке запроса на чтение Варианта Исполнения (2.4.3.24)
    ci:         Используется в расчетах измерений (см. 2.4.3.23; стр 116)
    ks:         Используется в расчетах измерений PQS (см. 2.4.3.23; стр 116)
    max_words_per_req:  2.4.4.1
                        В ответ на корректный запрос счетчик возвращает в поле данных ответа число байт, указанное
                        в поле «Число считываемых байт» запроса. Размер считываемого массива может составлять:
                        от 2 до 16 байт для счетчиков всех типов;
                        от 2 до 93 байт для счетчиков СЭТ-4ТМ.03, ПСЧ-4ТМ.05, ПСЧ-3ТМ.05;
                        от 2 до 133 байт для счетчиков ПСЧ-4ТМ.05М, ПСЧ-3ТМ.05М
    st_bytes:   Кол-во байт статуса. Для СЭТ 4ТМ 01 М ответ будет 4 байта, для остальных - 5
'''
def _load_type_defs(log) -> dict:

    if os.path.isfile('./nzif.json'):
        log.info('Using LOCAL file nzif.json')
        return _load_type_defs_from_file('./nzif.json')
    
    file_name = os.path.dirname(os.path.abspath(__file__)) + '/nzif.json'
    
    log.warn('Local file nzif.json not found, using: %s', file_name)
    
    return _load_type_defs_from_file(file_name)
    

def _load_type_defs_from_file(file_name: str) -> dict:
    assert isinstance(file_name, str), file_name

    try:
        with open(file_name) as f:
            data = json.loads(f.read())

        all_defs = {}  # includes both abstract and non-anstract

        # json является списком, а не словарем, потому что нужно упорядочение типов, чего нет в ключах словаря.
        # порядок требуется, потому что мы используем based_on
        for item in data:
            dr = DictReader(item, exc_type=Warning, location=None)  # explicitly say we dont need location from loader

            type_id = dr.get_str('id')
            if type_id in all_defs:
                raise Warning('Duplicated id "{}"'.format(type_id))

            based = item.get('based_on')
            if based:
                if isinstance(based, str):
                    if based not in all_defs:
                        raise Warning('Base type "{}" not found. Existing types: {}'.format(based, all_defs.keys()))
                    based_on_list = [all_defs[based]]
                else:
                    if not isinstance(based, list):
                        raise Warning('"based_on" should be str or list. not {}'.format(based))
                    based_on_list = []
                    for x in based:
                        if x not in all_defs:
                            raise Warning('Base type "{}" not found. Existing types: {}'.format(x, all_defs.keys()))
                        based_on_list.append(all_defs[x])
            else:
                based_on_list = []

            def base(ls, prop_name, default=None):
                for x in ls:
                    if prop_name in x:
                        return x[prop_name]
                return default

            new_type_def = {
                "id": type_id,
                "abstract": dr.get_bool('abstract', optional=True, default=False),
                "Inom": dr.get_int('Inom', optional=True, default=base(based_on_list, 'Inom')),
                "Unom": dr.get_str('Unom', optional=True, default=base(based_on_list, 'Unom')),
                "direct": dr.get_bool('direct', optional=True, default=base(based_on_list, 'direct')),
                "3_phase": dr.get_bool('3_phase', optional=True, default=base(based_on_list, '3_phase')),
                "type_code": dr.get_int('type_code', optional=True, default=base(based_on_list, 'type_code')),
                "profiles": dr.get_bool('profiles', optional=True, default=base(based_on_list, 'profiles')),
                "ci": dr.get_int('ci', optional=True, default=base(based_on_list, 'ci')),
                "ks": dr.get_int('ks', optional=True, default=base(based_on_list, 'ks')),
                "max_words_per_req": dr.get_int('max_words_per_req', optional=True, default=base(based_on_list, 'max_words_per_req')),
                "st_bytes": dr.get_int('st_bytes', optional=True, default=base(based_on_list, 'st_bytes')),
                'msr-1ph': [],
                'msr-3ph': [],
                'energy': [],
            }
            for bs in based_on_list:
                new_type_def['msr-1ph'].extend(bs.get('msr-1ph', []))
                new_type_def['msr-3ph'].extend(bs.get('msr-3ph', []))
                new_type_def['energy'].extend(bs.get('energy', []))

            # 1 phase
            # {"tag": "F", "f": "F_Hz", "rwri": [4, 0, 0]}
            for x in item.get('msr-1ph', []):
                if not isinstance(x, dict):
                    raise Warning('"msr-1ph" should contain dictionary items <tag: str, f: str, rwri: [...]>, not {}'.format(x))
                _dr = DictReader(x, exc_type=Warning)
                _dr.get_str('tag')
                _dr.get_str('f', options=('Ki', 'Ku', 'Ca', 'I_A', 'U_V', 'E_kwth', 'PQS_kwt', 'F_Hz', 'Cos'))
                rwri = _dr.get_raw('rwri')
                rwri_ok = isinstance(rwri, list) and len(rwri) == 3 and isinstance(rwri[0], int) and (0 <= rwri[0] <= 0xff) and isinstance(
                    rwri[1], int) and (0 <= rwri[1] <= 0xff) and isinstance(rwri[2], int) and (0 <= rwri[2] <= 0xff)
                if not rwri_ok:
                    raise Warning('"rwri" should be [p1: byte, p2: byte, p3: byte], not {}'.format(rwri))

                new_type_def['msr-1ph'].append(x)

            # 3 phase
            # {"tags": [null,  "Ia",   "Ib",   "Ic"],   "f": "I_A",     "rwri": [2, 0, null]},
            for x in item.get('msr-3ph', []):
                if not isinstance(x, dict):
                    raise Warning('"msr-3ph" should contain dictionary items <tags:[...], f: str, rwri: [...]>, not {}'.format(x))
                _dr = DictReader(x, exc_type=Warning)
                tags = _dr.get_raw('tags')
                tags_ok = isinstance(tags, list) and len(tags) == 4 and (tags[0] is None or isinstance(tags[0], str)) and isinstance(
                    tags[1], str) and isinstance(tags[2], str) and isinstance(tags[3], str)
                if not tags_ok:
                    raise Warning('"tags" should be [All: str | null, Ph1: str, Ph2: str, Ph3: str], not {}'.format(tags))

                _dr.get_str('f', options=('Ki', 'Ku', 'Ca', 'I_A', 'U_V', 'E_kwth', 'PQS_kwt', 'F_Hz', 'Cos'))
                rwri = _dr.get_raw('rwri')
                rwri_ok = isinstance(rwri, list) and len(rwri) == 3 and isinstance(rwri[0], int) and (0 <= rwri[0] <= 0xff) and isinstance(
                    rwri[1], int) and (0 <= rwri[1] <= 0xff) and rwri[2] in ('P', 'Q', None)
                if not rwri_ok:
                    raise Warning('"rwri" should be [p1: byte, p2: byte, p3: "P" | "Q" | null], not {}'.format(rwri))

                new_type_def['msr-3ph'].append(x)

            # Energy
            # {"tags": ["Eap", "Ean", "Erp", "Ern"], "arr": 0}
            for x in item.get('energy', []):
                if not isinstance(x, dict):
                    raise Warning('"energy" should contain dictionary items <tags:[...], arr: int>, not {}'.format(x))
                _dr = DictReader(x, exc_type=Warning)
                tags = _dr.get_raw('tags')
                tags_ok = isinstance(tags, list) and len(tags) == 4 and isinstance(tags[0], str) and isinstance(
                    tags[1], str) and isinstance(tags[2], str) and isinstance(tags[3], str)
                if not tags_ok:
                    raise Warning('"tags" should be [str, str, str, str], not {}'.format(tags))

                _dr.get_int('arr')

                new_type_def['energy'].append(x)

            if not new_type_def['abstract']:
                for n in ('Inom', 'Unom', 'direct', '3_phase', 'type_code', 'profiles', 'ci', 'ks', 'max_words_per_req', 'st_bytes'):
                    if new_type_def[n] is None:
                        raise Exception('{}: Type {} is not marked as abstract, but field "{}" is not set'.format(file_name, type_id, n))

            all_defs[type_id] = new_type_def

        return all_defs

    except Exception as ex:
        raise Warning('{}: {}'.format(file_name, ex))


def get_nzif_defs(log) -> dict:
    global _DEFS    # pylint: disable=global-statement

    if _DEFS is None:
        _DEFS = {}
        all_defs = _load_type_defs(log)
        for k, v in all_defs.items():
            if not v['abstract']:
                _DEFS[k] = v

    return _DEFS


def get_nzif_nack_codes() -> dict:
    global _NACK_CODES      # pylint: disable=global-statement
    return _NACK_CODES
