import itertools as it
from collections import OrderedDict
from inspect import ismethod
from operator import itemgetter

from dotmap import DotMap

from .dates import *


class DicPlus(DotMap):
    def __init__(self, *args, **kwargs):
        self._map = OrderedDict()
        self._dynamic = True
        if kwargs:
            if '_dynamic' in kwargs:
                self._dynamic = kwargs['_dynamic']
        if args:
            d = args[0]
            # for recursive assignment handling
            trackedIDs = {id(d): self}
            if isinstance(d, dict):
                for k, v in self.__call_items(d):
                    if isinstance(v, dict):
                        if id(v) in trackedIDs:
                            v = trackedIDs[id(v)]
                        else:
                            v = self.__class__(v, _dynamic=self._dynamic)
                            trackedIDs[id(v)] = v
                    if type(v) is list:
                        l = []
                        for i in v:
                            n = i
                            if isinstance(i, dict):
                                n = self.__class__(i, _dynamic=self._dynamic)
                            l.append(n)
                        v = l
                    self._map[k] = v
        if kwargs:
            for k, v in self.__call_items(kwargs):
                if k is not '_dynamic':
                    self._map[k] = v

    def __call_items(self, obj):
        if hasattr(obj, 'iteritems') and ismethod(getattr(obj, 'iteritems')):
            return obj.iteritems()
        else:
            return obj.items()

    def __getitem__(self, k):
        if k not in self._map and self._dynamic and k != '_ipython_canary_method_should_not_exist_':
            # returns an empty string (usefull for group_by)
            # return ''
            return self.__class__()
        return self._map[k]

    def format(self, variables):
        '''takes a DotMap object (dm) that has placeholders like {user.name}
        and fill the placeholders with the content of variables (can be DotMap or dict object)
        '''
        dp = DicPlus()
        variables = DicForMap(variables)
        for k, v in self.items():
            if type(v) == DicPlus:
                v = v.format(variables)
            elif type(v) in (list, tuple):
                l = []
                for i in v:
                    n = i
                    if type(i) == DicPlus:
                        n = i.format(variables)
                    elif type(i) == str:
                        n = i.format_map(variables)
                    l.append(n)
                if type(v) is tuple:
                    v = tuple(l)
                else:
                    v = l
            elif type(v) == str:
                v = v.format_map(variables)
            dp[k] = v
        return dp

    def overwrite(self, dp_other, lists="append", format_date=True):
        # Recursive Function that overwrites or replicates the data from dp_other into self. "lists" appends the other elements to self

        for k, v in dp_other.items():
            if type(v) == DicPlus:
                v = self[k].overwrite(v, lists)
            elif type(v) in (list, tuple):
                if lists == "append":
                    v = self[k] + [x for x in v if x not in self[k]]
            if format_date:
                abs_date = absolute_date(v)
                if abs_date["found"]:
                    v = abs_date["datetime"]
            self[k] = v
        return self

    @property
    def clean_json(self):
        dp = DicPlus()
        for k, v in self.items():
            if type(v) == DicPlus:
                v = v.clean_json
            elif type(v) in (list, tuple):
                l = []
                for i in v:
                    n = i
                    if type(i) == DicPlus:
                        n = i.clean_json
                    elif type(i) == datetime:
                        n = i.strftime("%Y-%m-%dT%H:%M:%S")
                    elif type(i) == timedelta:
                        n = str(i)
                    l.append(n)
                if type(v) is tuple:
                    v = tuple(l)
                else:
                    v = l
            elif type(v) == datetime:
                v = v.strftime("%Y-%m-%dT%H:%M:%S")
            elif type(v) == timedelta:
                v = str(v)
            dp[k] = v
        return dp

    def pprint(self):
        print(json.dumps(self.clean_json, indent=4, sort_keys=True))

    def get_from_string(self, string, variables=None):
        dp_copy = self
        for l in string.split("."):
            if type(dp_copy) == list:
                for i in dp_copy:
                    if i[l.split(":")[0]] == l.split(":")[1]:
                        dp_copy = i
                        break
            else:
                if l[0] == "{" and l[-1] == "}":
                    var = variables[l[1:-1]]
                    dp_copy = dp_copy[var]
                elif dp_copy is None:
                    return None
                else:
                    dp_copy = dp_copy[l]
        return dp_copy

    def mapping(self, other_dp, variables={}):
        dp = DicPlus()
        for k, v in self.items():
            if type(v) == DicPlus:
                v = v.mapping(other_dp, variables)
            else:
                v = other_dp.get_from_string(v, variables)
            dp[k] = v
        return dp

    def format_dates(self):
        dp = DicPlus()
        for k, v in self.items():
            if type(v) == DicPlus:
                v = v.format_dates()
            elif type(v) == str:
                v = get_abs_rel_date(v)
            dp[k] = v
        return dp

    @classmethod
    def from_list(cls, list_dp, group_by):
        if list_dp == []:
            return cls()
        group_by_level = group_by.split(":")[0]
        # adding the missing fields for sort
        for el in list_dp:
            if group_by_level not in el:
                el[group_by_level] = ''
        list_dp.sort(key=itemgetter(group_by_level))
        current_key = list_dp[0][group_by_level]
        dict_response = {current_key: [list_dp[0]]}
        for dp in list_dp[1:]:
            if dp[group_by_level] == current_key:
                dict_response[current_key].append(dp)
            else:
                current_key = dp[group_by_level]
                dict_response[current_key] = [dp]
        dp_local = cls(dict_response)
        if len(group_by.split(":")) > 1:
            dp_response = cls()
            for k, v in dp_local.items():
                dp_response[k] = cls.from_list(
                    v, group_by=":".join(group_by.split(":")[1:]))
            return dp_response
        return dp_local

    @classmethod
    def from_json(cls, filename):
        with open(filename) as json_file:
            config_file = cls(json.load(json_file))
        return config_file


class DicForMap(dict):
    def __missing__(self, key):
        return "{" + key + "}"
