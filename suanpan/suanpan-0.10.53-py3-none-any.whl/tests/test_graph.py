import pdb

from suanpan import graph

info = graph.Graph(appId="8885")
info.addConnection(
    sourceNodeId=info.getNodeByName("VS Code - Python (Service)").id,
    sourcePortId="out1",
    targetNodeId=info.getNodeByName("web output").id,
    targetPortId="in1",
)
info.update()
pdb.set_trace()
info.revert()
pdb.set_trace()
info.revert()
