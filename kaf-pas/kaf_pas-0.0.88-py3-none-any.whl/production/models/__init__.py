from isc_common.number import StrToInt
from kaf_pas.ckk.models.attr_type import Attr_type
from kaf_pas.system.models.contants import Contants

SPC_CLM_COUNT_ATTR, _ = Attr_type.objects.get_or_create(code='SPC_CLM_COUNT')
progress_deleted = 'Прогресс удален.'
p_id = StrToInt(Contants.objects.get(code='audo_top_level').value)
