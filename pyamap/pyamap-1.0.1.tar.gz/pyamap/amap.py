# coding: utf-8


class Amap:
    """
    pyamap旨在提供一个可以在notebook中方便绘制简单地理信息的python库，功能简单，易于使用
    
    Examples:
        >>> amap = from pyamap.amap import Amap
        >>> amap = Amap()
        >>> amap.set_zoom_level(15)
        >>> amap.width = "70%"
        >>> amap.height = "300px"
        >>> amap.add_marker(116.397428,39.90923)
        >>> amap.show()
    """

    def __init__(self, show_html=True, width="70%", height=300):
        """

        Args:
            show_html:
            width: 宽度，百分比，默认"70%"
            height: 高度，px，默认300
        """

        self.showHtml = show_html
        self.width = "70%"
        self.height = "{}px".format(height)
        self.zoomLevel = 10
        self.js = ""
        self.html = ""
        self.__prepare_html()
        self.isUsingRuler = False

    def add_circle(self, lng, lat, psize=100,
                   color="blue", opacity=3, stroke_weight=3):
        """添加一个圆点

        Args:
            lng: 经度
            lat: 维度
            psize: 点大小
            color: 颜色
            opacity: 透明度
            stroke_weight:

        Returns:

        """

        code = 'addCircle({},{},{},"{}",{},{},"{}",{});'.format(lng, lat, psize, color, opacity, stroke_weight, color,
                                                                opacity)
        self.__append_js_code(code)

    def add_polygon(self, polygon_arr, stroke_color="blue", stroke_opacity=0.2,
                    stroke_weight=3, fill_color="blue", fill_opacity=0.35):
        """添加一个多边形

        Args:
            polygon_arr: 多边形数组，为一堆点的集合，形如: [[lng1, lat1], [lng2, lat2], [lng3, lat3]]
            stroke_color: 边的颜色
            stroke_opacity: 边的透明度
            stroke_weight: 边的粗细
            fill_color: 填充颜色
            fill_opacity: 填充透明度

        Returns:

        """
        code = 'addPolygon({},"{}",{},{},"{}",{});'.format(polygon_arr, stroke_color, stroke_opacity, stroke_weight,
                                                           fill_color, fill_opacity)
        self.__append_js_code(code)

    def add_marker(self, lng, lat, icon="http://webapi.amap.com/images/marker_sprite.png"):
        """添加一个覆盖物

        Args:
            lng: 经度
            lat: 维度
            icon: 覆盖物样式（提供一个png文件的网络地址，默认有一个）

        Returns:

        """
        code = 'addMarker({}, {}, "{}");'.format(lng, lat, icon)
        self.__append_js_code(code)

    def use_ruler(self):
        """添加测距

        Returns:

        """

        if not self.isUsingRuler:
            code = '''
            var ruler;
            map.plugin(["AMap.RangingTool"],function(){ 
                 ruler = new AMap.RangingTool(map); 
                 ruler.turnOn(); 
            });
            '''
            self.__append_js_code(code)
            self.isUsingRuler = True
        else:
            pass

    def remove_ruler(self):
        """移除测距功能

        Returns:

        """

        if self.isUsingRuler:
            code = "ruler.turnOff();"
            self.__append_js_code(code)
            self.isUsingRuler = False
        else:
            pass

    def __set_js_code(self, js):
        self.js = js

    def __append_js_code(self, js):
        self.js += js

    def set_zoom_level(self, zoomLevel):
        self.zoomLevel = zoomLevel

    def __prepare_html(self):
        import time
        from pyamap.template import html
        with open("/tmp/pyamap_tmp.html", "w") as f:
            html = html.replace("//for PyAmap//", self.js)
            html = html.replace("//ZOOM_LEVEL//", str(self.zoomLevel))
            html = html.replace("map-height", self.height)
            html = html.replace("map-width", self.width)
            self.html = html
            f.write(html)

    def show(self):
        from IPython.display import display
        display(self)

    def _repr_html_(self):
        self.__prepare_html()
        if self.showHtml:
            return self.html
        else:
            return '<img src="amap.png" width="{}" height="{}">'.format(self.width, self.height)


def main():
    pass


if __name__ == '__main__':
    main()
