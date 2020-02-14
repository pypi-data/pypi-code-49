class node:
  def __init__(self,actual_cost,total_cost,node_no,obj):
    self.actual_cost = actual_cost
    self.total_cost = total_cost
    self.node_no = node_no
    self.obj = obj

class feed:
  def __init__(self,h_val,adj_node,nodeDict,Q):
    self.h_val = h_val
    self.adj_node = adj_node
    self.nodeDict = nodeDict
    self.Q=Q

  def path(self):
    #A* Search Algorithm
    minQ = self.Q.PriorityQueue() #Used priority class function
    node1 = node(0,0,0,None) #Start Node
    minQ.insert(node1)
    while minQ.size():
      fetched = minQ.delete()
      i=0
      if fetched.node_no == (len(self.h_val)-1): #Goal Test
        break
      #print(f"Parent: {fetched.node_no}")
      for adj in self.adj_node[fetched.node_no]:
        if(adj!=-1):
          fn = self.h_val[i]+adj+fetched.actual_cost #Heuristic Cost Check
          cost = adj+fetched.actual_cost #Actual Cost Calculation
          #print(f"Child node:{i} - cost:{adj} - actual_cost:{fn} and previous cost:{fetched.actual_cost}")
          nodeN = node(cost,fn,i,fetched)
          minQ.insert(nodeN)
        i+=1
        #print(f"Parent:{fetched.node_no} - Adj {i}")
    print(f"Cost of trverse: {fetched.actual_cost}")
    #Path finding Start
    path = [];
    while True:
      if fetched.obj!=None:
          path.append(self.nodeDict[fetched.node_no])
          fetched = fetched.obj
      else:
        path.append(self.nodeDict[fetched.node_no])
        break
    path.reverse()
    return path
