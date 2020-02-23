from collections import OrderedDict
from pyHydraulic.node_serializable import Serializable
from pyHydraulic.node_graphics_socket import QDMGraphicsSocket


LEFT_TOP = 1
LEFT_BOTTOM = 2
RIGHT_TOP = 3
RIGHT_BOTTOM = 4


DEBUG = False


class Socket(Serializable):
    # def __init__(self, node, index=0, position=LEFT_TOP, socket_type=1, multi_edges=True):
    def __init__(self, node, index=0, socket_type=1, multi_edges=True):
        super().__init__()

        self.node = node
        self.index = index
        # self.position = position
        self.socket_type = socket_type
        self.is_multi_edges = multi_edges

        if DEBUG: print("Socket -- creating with", self.index, "for node", self.node)


        self.grSocket = QDMGraphicsSocket(self, self.socket_type)  # 第一个self是node的对象，也就是说，socket已经为node的子对象了
        # 向上一级Node询问，我的位置放在哪里,並且設置位置
        self.updatePos()
        # 一个socket上可以连接多个edge，下面是edge的统计list
        self.edges = []

    def __str__(self):
        return "<Socket %s %s..%s>" % ("ME" if self.is_multi_edges else "SE", hex(id(self))[2:5], hex(id(self))[-3:])

    def updatePos(self):
        ### 這句話一定要調用，在item形狀和位置發生改變的時候，這句話一定要調用，否則程序可能報錯！！！
        self.grSocket.prepareGeometryChange()  # If you want to change an item's geometry in any way, you must first call prepareGeometryChange() to allow QGraphicsScene to update its bookkeeping.

        self.grSocket.setPos(*self.node.getSocketPosition(self.index))

    def getSocketPosition(self):
        if DEBUG: print("  GSP: ", self.index, "node:", self.node)
        res = self.node.getSocketPosition(self.index)
        if DEBUG: print("  res", res)
        return res


    def addEdge(self, edge):
        self.edges.append(edge)

    def removeEdge(self, edge):
        if edge in self.edges:
            self.edges.remove(edge)
        else:
            print("!W:", "Socket::removeEdge", "wanna remove edge", edge, "from self.edges but it's not in the list!")



    def removeAllEdges(self):
        while self.edges:
            edge = self.edges.pop(0)
            edge.remove()

    def hasEdge(self):
        if len(self.edges)!=0:
            return True
        else:
            return False

    def determineMultiEdges(self, data):
        if 'multi_edges' in data:
            return data['multi_edges']
        else:
            # probably older version of file, make RIGHT socket multiedged by default
            return data['position'] in (RIGHT_BOTTOM, RIGHT_TOP)

    def serialize(self):
        return OrderedDict([
            ('id', self.id),
            ('index', self.index),
            ('multi_edges', self.is_multi_edges),
            # ('position', self.position),
            ('socket_type', self.socket_type),
        ])

    def deserialize(self, data, hashmap={}, restore_id=True):
        if restore_id: self.id = data['id']
        self.is_multi_edges = self.determineMultiEdges(data)
        hashmap[data['id']] = self  # 把socket的id放在hashmap的对象字典中
        return True

