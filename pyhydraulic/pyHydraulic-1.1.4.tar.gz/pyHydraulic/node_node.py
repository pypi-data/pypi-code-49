from pyHydraulic.node_graphics_node import *
from pyHydraulic.node_content_widget import QDMNodeContentWidget
from pyHydraulic.node_socket import *
from pyHydraulic.utils import dumpException

DEBUG = False


class Node(Serializable):
    # def __init__(self, scene, node_type="pressure sensor", inputs=[], outputs=[]):
    def __init__(self, scene, node_type="pressure sensor"):
        super().__init__()
        self.scene = scene
        self._node_type = node_type
        #  根据类型，实例化控件的类型
        self.grNode = self.create_grNode(self._node_type)
        # 本node的当前比例系数
        self.scaleFactor = 1
        self.title = self._node_type
        # 下面scence注册一个Node,下一句是显示出Node
        self.scene.addNode(self)
        self.scene.grScene.addItem(self.grNode)

        # self.socket_spacing = 10

        # 在Node中根据socket信息添加socket到node中，self.sockets存放的是socket对象，统计用
        self.sockets = []
        counter = 0
        for item in self.grNode.socketInfo:  # inputs存放的是socket样式索引，item[1]为socket坐标
            socket = Socket(node=self, index=counter, socket_type=item[1], multi_edges=True)  # 这行就是把socket添加到了node中了
            counter += 1
            self.sockets.append(socket)

    def create_grNode(self,name):
        grNode = None
        if name in componentsLib.getSecondList():
            if name == "pressure sensor":
                grNode = GraphicsNode_pressure_sensor(self)
            elif name == "flow meter":
                grNode = GraphicsNode_flow_meter(self)
            elif name == "tank":
                grNode = GraphicsNode_tank(self)
            elif name == "gauge":
                grNode = GraphicsNode_gauge(self)
            elif name == "simple tank":
                grNode = GraphicsNode_simple_tank(self)
            elif name == "servo valve":
                grNode = GraphicsNode_servo_valve(self)
            elif name == "piston dual" or name == "piston right" or name == "piston left":
                grNode = GraphicsNode_pistion(self)
            elif name == "pump":
                grNode = GraphicsNode_pump(self)
            elif name == "filter":
                grNode = GraphicsNode_filter(self)
            elif name == "accumulator":
                grNode = GraphicsNode_accumulator(self)
            elif name == "one-way valve":
                grNode = GraphicsNode_oneway_valve(self)
            elif name == "relief valve":
                grNode = GraphicsNode_relief_valve(self)
            elif name == "text":
                grNode = GraphicsNode_text(self)
            elif name == "picture":
                grNode = GraphicsNode_picture(self)
            else:
                grNode = QAbstractGraphicsNode(self) # 啥也没有的对象
        return grNode

    def __str__(self):
        return "<Node %s..%s>" % (hex(id(self))[2:5], hex(id(self))[-3:])

    @property
    def grItem(self):
        return self.grNode

    # 1. 返回和设置item在父项或scene中的坐标
    @property
    def pos(self):
        return self.grNode.pos()        # QPointF

    def setPos(self, x, y):
        ### 這句話一定要調用，在item形狀和位置發生改變的時候，這句話一定要調用，否則程序可能報錯！！！
        self.grNode.prepareGeometryChange()  # If you want to change an item's geometry in any way, you must first call prepareGeometryChange() to allow QGraphicsScene to update its bookkeeping.

        self.grNode.setPos(x, y)

    # 2. 返回和设置item的名称
    @property
    def title(self): return self._node_type

    @title.setter
    def title(self, value):
        self._node_type = value
        # self.grNode.title = self._node_type

    @property
    def name(self):
        return self.grNode.name
    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self.grNode.name = value


    # 3. 返回和设置item中socket在父项item 的局部坐标，index为索引
    # 进到每个grNode里的socketInfo里去查每个socket的位置信息，返回的基于node的局部坐标，并不是scene坐标
    def getSocketPosition(self, index):
        if index < len(self.grNode.socketInfo):
            postion = self.grNode.socketInfo[index][0]
            return [postion.x(), postion.y()]
        else: return None

    # 4.更新socket中线Edge的坐标
    def updateConnectedEdges(self):
        for socket in self.sockets:
            # if socket.hasEdge():
            for edge in socket.edges:
                edge.updatePositions()

    # 5.删除Node，要删除所有的socket，还有edge
    def remove(self):
        if DEBUG: print("> Removing Node", self)
        if DEBUG: print(" - remove all edges from sockets")
        # 1.删除所有的socket
        for socket in self.sockets:
            if socket.hasEdge():
            # 2.删除所有的edges
            #     if DEBUG:
            #         print("    - removing all edges from socket:", socket)
            #         socket.removeAllEdges()
                for edge in socket.edges:
                    if DEBUG: print("    - removing from socket:", socket, "edge:", edge)
                    edge.remove()



        if DEBUG: print(" - remove grNode")
        # 3.移除自身node
        self.scene.grScene.removeItem(self.grNode)
        self.grNode = None
        if DEBUG: print(" - remove node from the scene")
        # 4.删除scene统计中的node
        self.scene.removeNode(self)
        if DEBUG: print(" - everything was done.")

    # 6.顺时针旋转增量angel，单位为度,
    def rotate(self, angle):
        self.setRotation(self.grNode.rotation() + angle)
        # 顺时针旋转到绝对角度angel，单位为度,

    # 返回绝对位置角度
    def rotation(self):
        return self.grNode.rotation()

    # 设置绝对位置
    def setRotation(self, angle):
        # 1.设置旋转中心为操作图元的中心
        self.grNode.setTransformOriginPoint(self.grNode.boundingRect().center().x(),
                                            self.grNode.boundingRect().center().y())
        # 2.每次调用，在原先的旋转角度上，加上新的旋转角度
        self.grNode.setRotation(angle)
        # 3.旋转之后将scene中的所有edge更新一遍
        for edge in self.scene.edges:
            edge.updatePositions()

    # 获取绝对缩放因子
    def scale(self):
        return self.grNode.scale()

    # 设置绝对缩放因子
    def setAbsoluteScale(self, factor):
        # 1.设置旋转中心为操作图元的中心
        self.grNode.setTransformOriginPoint(self.grNode.boundingRect().center().x(),
                                            self.grNode.boundingRect().center().y())
        # 2.每次调用，在原先的旋转角度上，加上新的旋转角度
        self.grNode.setScale(factor)
        # 3.旋转之后将scene中的所有edge更新一遍
        for edge in self.scene.edges:
            edge.updatePositions()


    def setRelativeScale(self, deltaScale):
        self.scaleFactor = self.scaleFactor + deltaScale
        self.setAbsoluteScale(self.scaleFactor)





    # 将node的属性信息进行串行化，便于存储
    def serialize(self):
        # 虽然每个node中的socket是固定死的，但是，主要是想记录socket的id，所以socket对象还是要序列化，
        sockets = [] # 存放sockets的序列化数据，主要是想记录socket的id
        for socket in self.sockets:
            sockets.append(socket.serialize())
        tupleListForDict = list(self.grItem.getProperty().items()) #list 类型
        tupleForSocket= ('sockets', sockets) # 后面追加socket信息
        tupleListForDict.append(tupleForSocket)

        return OrderedDict(tupleListForDict)# 返回属性：值字典

        # return OrderedDict([
        #     ('id', self.id),
        #     ("name",self.name),
        #     ('node_type', self._node_type),
        #     ('pos_x', self.grNode.scenePos().x()),
        #     ('pos_y', self.grNode.scenePos().y()),
        #     ('rotation', self.rotation()),  # 添加当前的角度位置
        #     ('scale', self.scale()),  # 当前缩放因子
        #     ('value', self.grNode.value),  #
        #     ('unit', self.grNode.unit),  #
        #     ('maxValue', self.grNode.maxValue),  #
        #     ('minValue', self.grNode.minValue),  #
        #     ('text', self.grNode.text),  #
        #     ('sockets', sockets),
        # ])

    # 反序列化单个node的数据data，一个node里面含有多个socket数据
    def deserialize(self, data, hashmap={}, restore_id=True):
        try:
            # 解析单个node数据，并遍历对应的"sockets"，将对应的属性赋值给socket对象
            for index in range(len(self.sockets)):
                if restore_id:
                    self.sockets[index].id = data["sockets"][index]["id"]
                self.sockets[index].index = data["sockets"][index]["index"]
                self.sockets[index].is_multi_edges = data["sockets"][index]["multi_edges"]
                self.sockets[index].socket_type = data["sockets"][index]["socket_type"]
                hashmap[data["sockets"][index]["id"]] = self.sockets[index]  # 在对象字典添加单个socket的对象和id
        except Exception as e:
            dumpException(e)
        return True

