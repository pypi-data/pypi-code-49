import numpy as np



class Graph(object):
    class Edge:
        def __init__(self,tail,head):
            self.head = head
            self.tail = tail

        def reverse(self):
            temp = self.tail
            self.tail = self.head
            self.head = temp
            return self

        def copy(self):
            return Graph.Edge(self.tail,self.head)

    class Node:
        def __init__(self,id):
            self.id=id
            self.edges={}

        def deg(self):
            return len(self.edges)

        def __str__(self):
            res = str(self.id) + ":\n"
            for head in self.edges:
                res += "\t"+str(head) + "\n"
            return res

    def __str__(self):
        res=""
        for n in self.nodes:
            res+=str(n)+"\n"
        return res

    def __init__(self,n):
        self.n = n
        self.nodes=[Graph.Node(i) for i in range(n)]
        self.edges={}



    def connect(self,id1,id2):
        tail=self.nodes[id1]
        head=self.nodes[id2]
        edge=Graph.Edge(tail, head)
        if id1 not in self.edges:
            self.edges[id1]={}
        self.edges[id1][id2]=edge
        edge.tail.edges[id2]=edge
    def isConnected(self,id1,id2):
        return id1 in self.edges and id2 in self.edges[id1]
    def avgDeg(self):
        return np.min(np.array(list(map(Graph.Node.deg,self.nodes))))


class UndirectedGraph(Graph):
    def connect(self,id1,id2):
        super(UndirectedGraph,self).connect(id1,id2)
        super(UndirectedGraph,self).connect(id2,id1)


