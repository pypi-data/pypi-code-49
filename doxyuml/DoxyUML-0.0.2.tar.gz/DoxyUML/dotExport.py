from graphviz import Digraph
from .classObj import ObjClass
from .namespaceObj import Namespace


class DotExport:

    def __init__(self,name: str):
        """
        constructor
        :param name: the name of the graph
        """
        self.dot = Digraph(name=name)

        self.name = name

        self.classes = dict()
        self.namespaces = []

    def add_class(self, clss: ObjClass):
        """
        Add a class to the class list
        :param clss: the class
        :return:
        """
        self.classes[clss.refid] = clss

    def add_namespace(self, ns: Namespace):
        self.namespaces.append(ns)

    def update(self):
        """
        Add all the classes to the graphiz graph and create the edges
        :return:
        """
        self.dot.clear()
        self.dot.attr("node", shape="record")
        self.dot.attr("edge", arrowtail="empty", dir="back")

        # print(self.classes)

        class_to_draw = self.classes.copy()

        for ns in self.namespaces:
            # print(ns)
            with self.dot.subgraph(name='cluster_'+ns.refid) as c:
                c.attr(style='filled')
                c.attr(color='orange')
                c.attr(label=ns.name)
                for clss in ns.classes:
                    print(clss)
                    print(self.classes[clss].to_graphviz_node())
                    c.node(clss, label=self.classes[clss].to_graphviz_node())
                    del class_to_draw[clss]

                func = r"\n".join([f.to_graphviz() for f in ns.functions])
                c.node(ns.name+"_func", func, shape="record", style="dashed", penwidth="0")

        for clss in class_to_draw:
            self.dot.node(clss, self.classes[clss].to_graphviz_node())

        for cls in self.classes:
            clss = self.classes[cls]
            # self.dot.node(clss.refid, clss.to_graphviz_node())
            for gen in clss.generalization:
                self.dot.edge(gen, clss.refid, arrowtail="empty")
            for agg in clss.aggregation:
                self.dot.edge(agg, clss.refid, arrowtail="diamond,empty")
            for comp in clss.composition:
                self.dot.edge(comp, clss.refid,arrowtail="diamond")

    def __str__(self):
        self.update()
        return self.dot.source

    def render(self):
        self.update()

        # self.dot.render(self.name+".dot", view=True)
        self.dot.view()
