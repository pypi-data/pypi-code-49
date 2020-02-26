#coding: utf-8
html = """
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>Show Pos</title>   
    <style type="text/css">
      body{
        margin:0;
        height:100%;
        width:100%;
        position:absolute;
      }
      #mapContainer{
        width: map-width;
        height: map-height;
      }
    </style>
  </head>
  <body>
    <div id="mapContainer"></div>
    <script type="text/javascript" src="https://webapi.amap.com/maps?v=1.3&key=820afe3932ebea15d73cd05b2a28e606";></script>
    <script type="text/javascript">
        var zoomLevel = //ZOOM_LEVEL//;

        var map, marker;
        //初始化地图对象，加载地图
        map = new AMap.Map("mapContainer",{
          resizeEnable: true,
          //二维地图显示视口
          view: new AMap.View2D({
            center:new AMap.LngLat(116.397428,39.90923),//地图中心点
            zoom: zoomLevel //地图显示的缩放级别
          })
        }); 

        map.plugin(["AMap.ToolBar"], function() {
                        toolBar = new AMap.ToolBar();
                        map.addControl(toolBar);
                });
        
        //实例化点标记
        function addMarker(x, y, icon="http://webapi.amap.com/images/marker_sprite.png"){
          var marker = new AMap.Marker({          
            icon: icon,
            position:new AMap.LngLat(x, y)
          });
          marker.setMap(map);  //在地图上添加点
          map.setZoomAndCenter(zoomLevel, [x,y]);
        }
        // 添加多边形
        function addPolygon(polygonArr,
                          strokeColor="blue", strokeOpacity=0.2,
                          strokeWeight=3, fillColor="blue", fillOpacity=0.35) {
          polygon = new AMap.Polygon({
              path: polygonArr,//设置多边形边界路径
              strokeColor: strokeColor, //线颜色
              strokeOpacity: strokeOpacity, //线透明度
              strokeWeight: strokeWeight,    //线宽
              fillColor: fillColor, //填充色
              fillOpacity: fillOpacity//填充透明度
          });
          polygon.setMap(map);
          map.setZoomAndCenter(zoomLevel, polygonArr[0])     
        }
        //添加圆点  
        function addCircle(x, y, psize=100,
                          strokeColor="blue", strokeOpacity=1,
                          strokeWeight=3, fillColor="blue", fillOpacity=3) {  
           circle = new AMap.Circle({   
           center:new AMap.LngLat(x, y),// 圆心位置  
           radius: psize, //半径  
           strokeColor: strokeColor, //线颜色  
           strokeOpacity: strokeOpacity, //线透明度  
           strokeWeight: strokeWeight, //线粗细度  
           fillColor: fillColor, //填充颜色  
           fillOpacity: 3//填充透明度  
           });   
           circle.setMap(map);
           map.setZoomAndCenter(zoomLevel, [x,y])     
        }
    </script>
    <script type="text/javascript">
      //for PyAmap//
    </script>
  </body>
</html>

"""