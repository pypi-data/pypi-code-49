from volcano.general.stddef import Quality
from volcano.general import stdsvcdef
from volcano.general import variant

from . import build_cfg


class ConnectedValue(stdsvcdef.IFindTagHandler):
    def __init__(self, full_name: str, var: variant.Variant, is_obligatory: bool):
        assert full_name and isinstance(full_name, str), full_name
        assert isinstance(var, variant.Variant), var
        assert isinstance(is_obligatory, bool), is_obligatory

        self.full_name_ = full_name
        self.is_obligatory_ = is_obligatory
        self.var_ = var
        self.quality_ = Quality.QUALITY_NOT_INIT

        self.exists_ = False
        self.read_ = False
        self.pipe_set_ = None

        build_cfg.build_tag(None, full_name, var.type_str())

    def is_connected(self):
        return self.exists_

    def mark_unread(self):
        self.read_ = False

    def is_read(self):
        return self.read_

    def sync(self, services: dict):
        assert isinstance(services, dict), services

        assert 'find' in services, services
        assert isinstance(services['find'], stdsvcdef.IFindTagService), services
        services['find'].find_tag(self.full_name_, self)

        assert 'set' in services, services
        assert isinstance(services['set'], stdsvcdef.ISetValueService), services
        self.pipe_set_ = services['set']

    def on_find_tag_ok(self, tag_id: int, tag_name: str, vt: str, user_data):
        if self.var_.type_str() != vt:
            raise Warning('Tag "{}" has mismatched type. Expected {}, in fact {}'.format(self.full_name_, self.var_.type_str(), vt))

        self.exists_ = True

        # init tag with NS before we read it
        self.pipe_set_.set_tag(tag_name, self.var_.get_value(), self.quality_)

    def on_find_tag_err(self, tag_name_or_id, user_data):
        if self.is_obligatory_:
            raise Warning('Tag "{}" not found'.format(self.full_name_))

    def set(self, value, quality: int = 0):
        assert isinstance(quality, int), quality

        self.read_ = True

        if self.is_connected():
            if self.quality_ != quality or self.var_.get_value() != value:  # in Python None==None
                self.var_.set_value_w(value)
                self.quality_ = quality
                self.pipe_set_.set_tag(self.full_name_, value, quality)

    def invalidate(self, quality: int):
        self.set(None, quality)
