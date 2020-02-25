# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class MyTree(Component):
    """A MyTree component.
ExampleComponent is an example component.
It takes a property, `label`, and
displays it.
It renders an input with the property `value`
which is editable by the user.

Keyword arguments:
- id (string; optional): The ID used to identify this component in Dash callbacks.
- autoExpandParent (boolean; default True): 是否自动展开父节点 true
- checkedKeys (dict; optional): （受控）选中复选框的树节点（注意：父子节点有关联，如果传入父节点 key，则子节点自动选中；
相应当子节点 key 都传入，父节点也自动选中。当设置checkable和checkStrictly，
它是一个有checked和halfChecked属性的对象，并且父子节点的选中与否不再关联. checkedKeys has the following type: list of strings | dict containing keys 'checked', 'halfChecked'.
Those keys have the following types:
  - checked (list of strings; optional)
  - halfChecked (list of strings; optional)
- checkedChildrenKeys (list of strings; optional): 选择的所有子节点
- allCheckedKeys (dict; optional): 所有选中的节点（即包括半选中的父节点）. allCheckedKeys has the following type: list of strings | dict containing keys 'checkedKeys', 'halfCheckedKeys'.
Those keys have the following types:
  - checkedKeys (dict; optional): checkedKeys has the following type: list of strings | dict containing keys 'checked', 'halfChecked'.
Those keys have the following types:
  - checked (list of strings; optional)
  - halfChecked (list of strings; optional)
  - halfCheckedKeys (list of strings; optional)
- checkStrictly (boolean; optional): checkable 状态下节点选择完全受控（父子节点选中状态不再关联）	false
- checkable (boolean; optional): checkable or not false
- defaultCheckedKeys (list of strings; optional): 默认选中复选框的树节点
- defaultExpandAll (boolean; optional): 默认展开所有树节点 false
- defaultExpandedKeys (list of strings; optional): 默认展开指定的树节点
- defaultExpandParent (boolean; optional): 默认展开父节点 true
- defaultSelectedKeys (list of strings; optional): 默认选中的树节点
- disabled (boolean; optional): 将树禁用 false
- draggable (boolean; optional): 设置节点可拖拽（IE>8） falseloadData
- expandedKeys (list of strings; optional): （受控）展开指定的树节点
- loadedKeys (list of strings; optional): （受控）已经加载的节点，需要配合 loadData 使用
- multiple (boolean; optional): 支持点选多个节点（节点本身） false
当multiple为true时，需要提供初始的selectedKeys，
否则会出现向undefined添加数据而报错的现象
- selectable (boolean; optional): 是否可选中 true
- selectedKeys (list of strings; optional): （受控）设置选中的树节点
- showIcon (boolean; optional): 是否展示 TreeNode title 前的图标，没有默认样式，如设置为 true，需要自行定义图标相关样式	boolean	false
- switcherIcon (dash component; optional): 自定义树节点的展开/折叠图标 React.ReactElement	-	3.12.0
- showLine (boolean; optional): 是否展示连接线	boolean	false
- treeData (string; optional): treeNodes 数据，如果设置则不需要手动构造 TreeNode 节点（key 在整个树范围内唯一）	
python 提供数据时的dict格式：
{
   'title':'title',
   'key':'key',
   'children':[
     {
       'title':'title',
       'key':'key',
       'children':[...]
     }
   ]
}"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, autoExpandParent=Component.UNDEFINED, checkedKeys=Component.UNDEFINED, checkedChildrenKeys=Component.UNDEFINED, allCheckedKeys=Component.UNDEFINED, checkStrictly=Component.UNDEFINED, checkable=Component.UNDEFINED, defaultCheckedKeys=Component.UNDEFINED, defaultExpandAll=Component.UNDEFINED, defaultExpandedKeys=Component.UNDEFINED, defaultExpandParent=Component.UNDEFINED, defaultSelectedKeys=Component.UNDEFINED, disabled=Component.UNDEFINED, draggable=Component.UNDEFINED, expandedKeys=Component.UNDEFINED, filterTreeNode=Component.UNDEFINED, loadData=Component.UNDEFINED, loadedKeys=Component.UNDEFINED, multiple=Component.UNDEFINED, selectable=Component.UNDEFINED, selectedKeys=Component.UNDEFINED, showIcon=Component.UNDEFINED, switcherIcon=Component.UNDEFINED, showLine=Component.UNDEFINED, onCheck=Component.UNDEFINED, onDragEnd=Component.UNDEFINED, onDragEnter=Component.UNDEFINED, onDragLeave=Component.UNDEFINED, onDragOver=Component.UNDEFINED, onDragStart=Component.UNDEFINED, onDrop=Component.UNDEFINED, onExpand=Component.UNDEFINED, onLoad=Component.UNDEFINED, onRightClick=Component.UNDEFINED, onSelect=Component.UNDEFINED, treeData=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'autoExpandParent', 'checkedKeys', 'checkedChildrenKeys', 'allCheckedKeys', 'checkStrictly', 'checkable', 'defaultCheckedKeys', 'defaultExpandAll', 'defaultExpandedKeys', 'defaultExpandParent', 'defaultSelectedKeys', 'disabled', 'draggable', 'expandedKeys', 'loadedKeys', 'multiple', 'selectable', 'selectedKeys', 'showIcon', 'switcherIcon', 'showLine', 'treeData']
        self._type = 'MyTree'
        self._namespace = 'zdc'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'autoExpandParent', 'checkedKeys', 'checkedChildrenKeys', 'allCheckedKeys', 'checkStrictly', 'checkable', 'defaultCheckedKeys', 'defaultExpandAll', 'defaultExpandedKeys', 'defaultExpandParent', 'defaultSelectedKeys', 'disabled', 'draggable', 'expandedKeys', 'loadedKeys', 'multiple', 'selectable', 'selectedKeys', 'showIcon', 'switcherIcon', 'showLine', 'treeData']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(MyTree, self).__init__(**args)
