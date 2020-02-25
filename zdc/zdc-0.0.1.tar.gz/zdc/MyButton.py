# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class MyButton(Component):
    """A MyButton component.


Keyword arguments:
- children (a list of or a singular dash component, string or number; optional)
- id (string; optional): The ID used to identify this component in Dash callbacks.
- disabled (boolean; optional): 按钮失效状态
- ghost (boolean; optional): 幽灵属性，使按钮背景透明.
- href (string; optional): 点击跳转的地址，指定此属性 button 的行为和 a 链接一致
- htmlType (string; optional): 设置 button 原生的 type 值，可选值请参考 HTML 标准
- icon (string; optional): 设置按钮的图标类型
- loading (dict; optional): 设置按钮载入状态. loading has the following type: boolean | dict containing keys 'delay'.
Those keys have the following types:
  - delay (number; optional)
- shape (string; optional): 设置按钮形状，可选值为 circle、 round 或者不设
- size (string; optional): 设置按钮大小，可选值为 small large 或者不设
- target (string; optional): 相当于 a 链接的 target 属性，href 存在时生效
- type (string; optional): 设置按钮类型，可选值为 primary dashed danger link(3.17 中增加) 或者不设
- block (boolean; optional): 将按钮宽度调整为其父宽度的选项
- n_clicks (number; default 0): 点击次数
- n_clicks_timestamp (number; default -1): 点击的时间戳，从1970年起
可以用于在多个按钮中，判断点击的是哪个
- className (string; optional)"""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, disabled=Component.UNDEFINED, ghost=Component.UNDEFINED, href=Component.UNDEFINED, htmlType=Component.UNDEFINED, icon=Component.UNDEFINED, loading=Component.UNDEFINED, shape=Component.UNDEFINED, size=Component.UNDEFINED, target=Component.UNDEFINED, type=Component.UNDEFINED, onClick=Component.UNDEFINED, block=Component.UNDEFINED, n_clicks=Component.UNDEFINED, n_clicks_timestamp=Component.UNDEFINED, className=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'disabled', 'ghost', 'href', 'htmlType', 'icon', 'loading', 'shape', 'size', 'target', 'type', 'block', 'n_clicks', 'n_clicks_timestamp', 'className']
        self._type = 'MyButton'
        self._namespace = 'zdc'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'disabled', 'ghost', 'href', 'htmlType', 'icon', 'loading', 'shape', 'size', 'target', 'type', 'block', 'n_clicks', 'n_clicks_timestamp', 'className']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(MyButton, self).__init__(children=children, **args)
