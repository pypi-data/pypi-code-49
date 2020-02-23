from hamilton_sdk.search import SearchProblem
from hamilton_sdk.util import *
from hamilton_sdk.graphTheory import *
from random import randint

def createRandomUndirectedGraph(n,avgD):
    g=UndirectedGraph(n)
    while g.avgDeg()<avgD:
        id1=randint(0, n-1)
        id2=randint(0, n-1)
        if id1!=id2:
            g.connect(id1,id2)
    return g


def connectedNeighboursCount(g,state):
    connections=[g.isConnected(state[i], state[(i + 1) % g.n]) for i in range(g.n)]
    return sum(connections)

class HamiltonCycleProblem(SearchProblem):

    def __init__(self,graph):
        self.graph=graph
        self.explored=set()


    def getStartState(self):
        nextState=list(range(self.graph.n))
        return (nextState,_hamiltonHeuristics(self.graph.n,self.graph,nextState),0,'_'.join(str(x) for x in nextState))

    def isGoalState(self, state):
        return connectedNeighboursCount(self.graph,state[0])==self.graph.n

    def explore(self,state):
        # print len(self.explored),state[2],state[1]
        self.explored.add(state[3])

    def isExplored(self,state):
        return state[3] in self.explored


    def getSuccessors(self,actionsHistory, state):
        state,h,g,_=state
        size=self.graph.n
        if h+g > size / 2:
            return []
        moves = list(range(1, size - 1))
        nodes = list(range(1,size))
        def createSuccessor(state,n, m,size):
            nextState=startWithZero(move(state, n, m, size))
            return ((n, m),(nextState,_hamiltonHeuristics(size,self.graph,nextState),g+1,'_'.join(str(x) for x in nextState)))

        successors=[createSuccessor(state, n, m, size) for n in nodes for m in moves]
        def filterMoves(s):
            action,state=s
            state,hnext,gnext,_=state
            i=state.index(action[0])
            return not self.isExplored(state) and hnext<h and hnext+gnext <= size / 2 and self.graph.isConnected(state[i],state[(i+1)%size]) and self.graph.isConnected(state[i],state[(i-1)%size])

        flitered=list(filter(filterMoves, successors))
        return flitered

    def getCostOfActions(self, actions):
        return len(actions)

def _hamiltonHeuristics(size,graph,state):
    return (size-connectedNeighboursCount(graph,state))/2

def hamiltonHeuristics(state,problem):
    return state[1]
#
# size=15
# hcp=HamiltonCycleProblem(createRandomUndirectedGraph(size, 3))
#
# actions=aStarSearch(hcp,hamiltonHeuristics)
# if actions is not None:
#     state = list(range(size))
#     for a in actions:
#         state = move(state, a[0], a[1], size)
#
#     print(hcp.graph)
#
#     print("Explored : " + str(len(hcp.explored)))
#     print("Actions : " + str(len(actions)))
#
#     print(state)
#
#     print(connectedNeighboursCount(hcp.graph, state))
# else:
#     print("Explored : " + str(len(hcp.explored)))
#     print("None")

