"""
    If a result is present, the netcomp is covered
    If tested is True, then the result compliant defines if the netcomp is compliant or not.
    If tested is False, then the netcomp is covered but a test did not run.
"""
from fnmatch import fnmatchcase
from collections import namedtuple
from .nets import load_nets, first_alias
from .components import net_to_fully_qualified_name

TestResult = namedtuple('CoverageResult', 'name tested compliant')

NetComp = namedtuple('NetComp', 'key results net component')

class CoverageAnalysisError(Exception): pass

def create_netlist_from_component(top_level_component):
    nets = []
    for component in top_level_component.iter_all(include_self=True):
        nets += component.nets
    
    all_nets = load_nets(nets)
    return all_nets

def create_netcomp(key, net, component, netlist):
    net = netlist[first_alias(net)]
    netcomp = NetComp(key=key, results=[], net=net, component=component)
    # net.netcomps.append(netcomp) # back reference
    return netcomp
    

def create_netcomp_map_from_component(top_level_component, netlist):
    netcomps = {}
    for component in top_level_component.iter_all(include_self=True):
        prefix = component.fully_qualified_prefix()
        for net in component.nets:
            key = net_to_fully_qualified_name(prefix, net)
            netcomp = create_netcomp(key=key, net=net, component=component, netlist=netlist)
            netcomps[key] = netcomp
    return netcomps

def filter_netcomp_map(netcomp_map, must_match=None, allowed_nets=None):
    if must_match is None and allowed_nets is None:
        return netcomp_map
    
    def _nets_condition(netcomp_key):
        if netcomp_map[netcomp_key].net in allowed_nets:
            return True
        else:
            return False
    
    def _match_condition(netcomp_key):
        for pattern in must_match:
            if fnmatchcase(netcomp_key, pattern):
                    return True
        # else
        return False
    
    
    condition_fns = []
    if must_match is not None:
        condition_fns.append(_match_condition)
        
    if allowed_nets is not None:
        condition_fns.append(_nets_condition)
    
    def _filter(netcomp_key):
        for cond_fn in condition_fns:
            if not cond_fn(netcomp_key):
                # Return false as soon as one condition fails
                return False
        # else
        return True
        
    return filter(_filter, netcomp_map)

def create_subset_of_dict(_dict, keys):
    return {key:_dict[key] for key in keys if key in _dict}

class CoverageAnalysis(object):
    def __init__(self, top_level_component):
        self._top_level = top_level_component
        self._netlist = create_netlist_from_component(top_level_component)
        self._netcomp_map = create_netcomp_map_from_component(top_level_component, self._netlist)
        self._tests = {}
    
    def add_test(self, fnmatch, name, allow_links_to=[]):
        test = NetCompTestDescriptor(fnmatch, name, allow_links_to=allow_links_to)
        return test.filter_for_coverage(self._netcomp_map)
            

class NetCompTestDescriptor(object):
    def __init__(self, fnmatches, name, allow_links_to=[]):
        self.source_matches = fnmatches
        self.name = name
        self.targets_match_allow = allow_links_to
    
    def filter_for_coverage(self, netcomp_map):
        source_netcomp_keys = self.get_source_netcomp_keys(netcomp_map)
        
        source_nets = [netcomp_map[key].net for key in source_netcomp_keys]
        
        target_netcomp_keys = self.get_target_netcomp_keys(netcomp_map, source_nets)
        
        return set(target_netcomp_keys + source_netcomp_keys)
        
    def get_source_netcomp_keys(self, netcomp_map):
        return list(filter_netcomp_map(netcomp_map, must_match=self.source_matches))
    
    def get_target_netcomp_keys(self, netcomp_map, allowed_nets):
        return list(filter_netcomp_map(netcomp_map, must_match=self.targets_match_allow, allowed_nets=allowed_nets))
        
        
        
    
