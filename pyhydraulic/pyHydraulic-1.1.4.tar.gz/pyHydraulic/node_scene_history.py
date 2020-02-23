from pyHydraulic.node_graphics_edge import QDMGraphicsEdge


DEBUG = True

# 为了防止出错，下面注释掉了选中元素状态的恢复
class SceneHistory():
    def __init__(self, scene):
        self.scene = scene

        self.history_stack = []
        self.history_current_step = -1
        self.history_limit = 32

    def clear(self):
        self.history_stack = []
        self.history_current_step = -1

    def undo(self):
        if DEBUG: print("UNDO")

        if self.history_current_step > 0:
            self.history_current_step -= 1
            self.restoreHistory()

    def redo(self):
        if DEBUG: print("REDO")
        if self.history_current_step + 1 < len(self.history_stack):
            self.history_current_step += 1
            self.restoreHistory()


    def restoreHistory(self):
        if DEBUG: print("Restoring history",
                        ".... current_step: @%d" % self.history_current_step,
                        "(%d)" % len(self.history_stack))
        self.restoreHistoryStamp(self.history_stack[self.history_current_step])


    # 外部经常调用这个函数，用来在历史库中增加一个shot,desc为一个操作描述符，可以为任何字符串
    def storeHistory(self, desc, setModified=False):
        if setModified:
            self.scene.has_been_modified = True

        if DEBUG: print("Storing history", '"%s"' % desc,
                        ".... current_step: @%d" % self.history_current_step,
                        "(%d)" % len(self.history_stack))

        # if the pointer (history_current_step) is not at the end of history_stack
        if self.history_current_step+1 < len(self.history_stack):
            self.history_stack = self.history_stack[0:self.history_current_step+1]

        # history is outside of the limits
        if self.history_current_step+1 >= self.history_limit:
            self.history_stack = self.history_stack[1:]
            self.history_current_step -= 1

        hs = self.createHistoryStamp(desc) # hs为history_stamp数据，类型为字典，对当前shot进行描述

        self.history_stack.append(hs)  # 在stack中添加此shot
        self.history_current_step += 1 # 指针加一
        if DEBUG: print("  -- setting step to:", self.history_current_step)

    # 创建一张“照片”
    def createHistoryStamp(self, desc):
        sel_obj = {
            'nodes': [],
            'edges': [],
        } # 上面[]为被选中的元素的id,用来恢复被选中的状态用
        # 把选中的控件状态id也存储一下
        # for item in self.scene.grScene.selectedItems():
        #     if hasattr(item, 'node'):
        #         sel_obj['nodes'].append(item.node.id)
        #     elif isinstance(item, QDMGraphicsEdge):
        #         sel_obj['edges'].append(item.edge.id)
        # 把整个界面存状态存在在stamp里面，包括选中的控件状态
        history_stamp = {
            'desc': desc,
            'snapshot': self.scene.serialize(), #这一行其实就对整个界面拍照，shot
            'selection': sel_obj, # 选中的item的id
        }

        return history_stamp

    # 给一张照片数据history_stamp，恢复整个界面
    def restoreHistoryStamp(self, history_stamp):
        if DEBUG: print("RHS: ", history_stamp['desc'])

        self.scene.deserialize(history_stamp['snapshot']) # 主要是恢复元素

        # # restore selection ，恢复选中的状态
        # for edge_id in history_stamp['selection']['edges']:
        #     for edge in self.scene.edges:
        #         if edge.id == edge_id:
        #             edge.grEdge.setSelected(True)
        #             break
        #
        # for node_id in history_stamp['selection']['nodes']:
        #     for node in self.scene.nodes:
        #         if node.id == node_id:
        #             node.grNode.setSelected(True)
        #             break