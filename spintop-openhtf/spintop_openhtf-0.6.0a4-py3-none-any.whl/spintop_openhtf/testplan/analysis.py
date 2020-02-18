import itertools
import os

from jsonschema.validators import validator_for
from collections import Sequence

from ..util import yaml_loader
from ..util.compat import isstr

from .base import TestPlanError

HERE = os.path.abspath(os.path.dirname(__file__))

class AnalysisError(TestPlanError): pass

def flatten_string_list(array):
    new_array = []
    for item in array:
        if isinstance(item, Sequence) and not isinstance(item, str):
            new_array += item
        else:
            new_array.append(item)
            
    return new_array

def get_schema(filename=os.path.join(HERE, 'analysis_schema.yml')):
    return yaml_loader.load_yml_file(filename)

def compile_schema():
    schema = get_schema()
    Validator = validator_for(schema)
    Validator.check_schema(schema)
    return Validator(schema)

class DomainNodeInterface(object):
    def __init__(self, obj):
        self._dict = obj
    
    @property
    def name(self):
        return self._dict.get('name', '')
    
    @property
    def description(self):
        return self._dict.get('description', '')
    
    @property
    def nodes(self):
        return self._dict.get('nodes', [])
    
    @property
    def edges(self):
        return self._dict.get('edges', [])
    
    @property
    def required(self):
        return self._dict.get('required', False)
    
    @property
    def implies(self):
        return self._dict.get('implies', [])
    
    @property
    def testable(self):
        return self._dict.get('testable', False)

    @property
    def data(self):
        """ Domain specific data. """
        return {}
    
    def hook_node_attach_to(self, this_node, parent_node):
        """ Called when the node created from this interface, this_node, is attached
        to a parent_node """
        
    def hook_child_attach(self, this_node, child_node):
        """ Called when a child attached to the node created from this interface. """
    
    def as_node(self, context):
        
        node_objects = [context.to_node(child_node) for child_node in self.nodes]
        
        node = Node(
            name=self.name,
            description=self.description,
            nodes=node_objects,
            edges=self.edges,
            required=self.required,
            implies=self.implies,
            testable=self.testable,
            data=self.data
        )
        
        return node
    
class ElectricalDomainInterface(DomainNodeInterface):
    
    @property
    def nodes(self):
        return self._dict.get('components', []) + self._dict.get('subcomponents', [])
    
    @property
    def edges(self):
        return self._dict.get('testpoints', [])
    
    @property
    def testable(self):
        return False
    
    # def hook_node_attach_to(self, this_node, parent_node):

def ElectricalAnalysisContext():
    return AnalysisContext(domain_interface=ElectricalDomainInterface)

class AnalysisContext(object):
    def __init__(self, domain_interface=DomainNodeInterface):
        self.domain_interface = domain_interface
        self.root = Node(description="Root node")
        self.graph = None
        self.validator = compile_schema()
        
    def parse(self, node_dict):
        try:
            self.validator.validate(node_dict)
        except Exception as e:
            print(e)
        
        sub_root = self.to_node(node_dict)
        sub_root.attach_to(self.root)
        return sub_root
    
    def to_node(self, node_dict):
        return self.domain_interface(node_dict).as_node(self)
    
    def build_graph(self):
        """ Builds the dependency graph.
        
        The build is separated into two steps:
        1. Implied dependencies.
            These are dependencies specified by the shape of the tree and the parent/child
            relationships. When the 'required' node property is false, a compliant child
            adds an inbound test edge. When required is true, the the relationship is 
            inversed and the test coverage flows from the parent to the child.
        2. Direct dependencies.
            These are dependencies linked accross the tree using the defined edges.
        """
        import networkx as nx
        
        self.graph = nx.DiGraph()
        edges_map = {}
        self.nodes_map = {}
        
        if self.root is None:
            raise RuntimeError('self.parse must be called before build_connectivity_graph')
        
        # Step 1: Link nodes implied dependencies
        for node in self.root.iter_children():
            qualname = self._add_node(node)
            
            # Add nodes and edges to temporary maps
            for edge in node.edges:
                linked_nodes = edges_map.get(edge, set())
                linked_nodes.add(qualname)
                edges_map[edge] = linked_nodes
                
            # Create the implied dependencies
            if node.parent:
                if node.required:
                    self._add_edge(node.parent.qualname, qualname)
                else:
                    self._add_edge(qualname, node.parent.qualname)
            elif node.required:
                raise RuntimeError('Cannot have required property without a parent node.')
            
            for implied_qualname in node.implies:
                implied_ref = self.resolve_node_ref(node, implied_qualname)
                self._add_edge(qualname, implied_ref)
        
        # Step 2
        for linkname, nodes in edges_map.items():
            for u,v in itertools.combinations(nodes, 2):
                self._add_testable_edge(linkname, u, v)
        
        return self.graph
    
    def resolve_node_ref(self, node, ref, graph=None):
        if graph is None: graph = self.graph
        orig_ref = ref
        possible_refs = node.get_ref_qualname_possibilities(orig_ref)
        for ref in possible_refs:
            if ref in self.graph.nodes:
                return ref
        else:
            raise AnalysisError(
                'Unale to resolve ref "{ref}" from node "{node_qualname}". Tested possibilities: {possible_refs}'.format(
                    ref=orig_ref,
                    node_qualname=node.qualname,
                    possible_refs=possible_refs
                )
            )
        
    
    def _add_testable_edge(self, linkname, qualname_u, qualname_v):
        new_node = Node(
            name=qualname_u + '/' + linkname + '/' + qualname_v,
            testable=True
        )
        self._add_node(new_node)
        
        source = new_node.qualname
        self._add_edge(source, qualname_u)
        self._add_edge(source, qualname_v)
        
    
    def _add_node(self, node):
        qualname = node.qualname
        print('Add node %s' % qualname)
        self.graph.add_node(qualname, qualname=qualname, node=node)
        self.nodes_map[qualname] = node
        return qualname
        
    def _add_edge(self, u, v):
        print('Add edge %s to %s' % (u, v))
        self.graph.add_edge(u, v)
        

class Node(object):
    def __init__(self, name="", description="", nodes=[], edges=[], required=False, implies=[], testable=False, data={}, creator_interface=None):
        self._parent = None
        self._creator_interface = creator_interface
        
        self.name = name
        self.description = description
        self.edges = flatten_string_list(edges)
        self.required = required
        self.implies = implies
        self.testable = testable
        
        self.data = data
        
        self.nodes = []
        for node in nodes:
            node.attach_to(self)
            
    @property
    def parent(self):
        return self._parent
            
    def __contains__(self, name_or_node):
        
        if isstr(name_or_node):
            for node in self.nodes:
                if name_or_node == node.name:
                    return True
            else:
                return False
        else:
            return name_or_node in self.nodes
    
    @property
    def qualname(self):
        if not self.name:
            return self._passthrough_qualname()
        
        if self._parent:
            parent_qualname = self._parent.qualname
            if parent_qualname:
                return parent_qualname + '.' + self.name
            else:
                return self.name
        else:
            return self.name
        
    def _passthrough_qualname(self):
        if self._parent:
            return self._parent.qualname
        else:
            return ''
        
    def get_ref_qualname_possibilities(self, ref):
        """ Returns a list of possible qualname references the user might be
        trying to reach. They will be tested in order and the first match 
        will be used. """
        if ref.startswith('.'):
            return [self._parent.qualname + '.' + ref] # sibling ref
        else:
            return [ref] # absolute ref
        
    def attach_to(self, parent):
        self._parent = parent
        parent.nodes.append(self)
        
        if self._creator_interface:
            self._creator_interface.hook_node_attach_to(self, parent) 
            self._creator_interface.hook_child_attach(parent, self) 
        
    def iter_children(self):
        yield self
        for topnode in self.nodes:
            for subnode in topnode.iter_children():
                yield subnode
         
