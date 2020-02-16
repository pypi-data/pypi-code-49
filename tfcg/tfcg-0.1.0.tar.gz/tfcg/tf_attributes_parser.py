import typing

import networkx as nx


def parse_attributes(G: nx.DiGraph, tf_graph_def: dict) -> nx.DiGraph:
    nodes = tf_graph_def['node']
    name_to_idx = {name: idx for idx, name in G.nodes(data="name")}
    attrs = {idx: {} for idx in name_to_idx.values()}
    for ele in nodes:
        names = ele['name'].split('/')
        name = ele['name'].split('/')[0]
        if name == 'sequential':
            continue
        if names[-1] in ['kernel', 'Variable']:
            name = ele['name'].split('/')[0]
            idx = name_to_idx[name]
            attr = _register_channels(G, ele)
            attrs[idx] = {**attrs[idx], **attr}
        if names[-1] == 'Conv2D':
            name = ele['name'].split('/')[0]
            idx = name_to_idx[name]
            attr = _parse_Conv2D(G, ele)
            attrs[idx] = {**attrs[idx], **attr}

    nx.set_node_attributes(G, attrs)
    return G

def _register_channels(G: nx.DiGraph, info: dict) -> typing.Dict[str, int]:
    try:
        kernel = [int(d['size'])for d in info['attr']['shape']['shape']['dim'][:-2]]
    except:
        kernel = None
    input_channel = info['attr']['shape']['shape']['dim'][-2]['size']
    output_channel = info['attr']['shape']['shape']['dim'][-1]['size']
    return {'input_channel': int(input_channel), 'output_channel': int(output_channel), 'kernel': kernel}

def _parse_Conv2D(G: nx.DiGraph, info: dict) -> typing.Dict[str, int]:
    strides = [int(i) for i in info['attr']['strides']['list']['i']]
    dilations = [int(i) for i in info['attr']['dilations']['list']['i']]
    return {'strides': strides, 'dilations': dilations}
