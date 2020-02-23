# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""
from hamilton_sdk import util as u


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        u.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        u.raiseNotDefined()

    def getSuccessors(self,actionHistory, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        u.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        u.raiseNotDefined()



def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first [p 74].

    Last successor node that has been expanded is the first node to be explored

    """
    s=u.Stack()
    return search(problem, lambda :s.pop() if s else False, lambda history,state: s.push((history,state)))


def breadthFirstSearch(problem):
    """
    "Search the shallowest nodes in the search tree first. [p 74]"
    First successor node that has been expanded is the first node to be explored
    """
    q=u.Queue()
    return search(problem, lambda :q.pop() if q else False, lambda history,state: q.push((history,state)))


def search(problem, pop, push):
    """
    a generic solution for searching for a goal state in a problem given the frontier strategy implemented in pop and push functions
    :param problem: the problem
    :param pop: a function to get and remove next state from frontier
    :param push: a function to push a state to the frontier
    :return: list of actions to get to a goal state
    """
    state = problem.getStartState()
    if problem.isGoalState(state):
        return []
    # actions log
    actions = []
    # the explored set, a node becomes explored when all its successors has been expended
    problem.explore(state)
    # just an helper to not enter same node to the frontier twice, this will make sure only the first path to a node is saved
    while True:
        successors = problem.getSuccessors(actions,state)
        for a,s in successors:
            actionsHistory=actions + [a]
            push(actionsHistory, s)
        # search an unexplored node in the frontier
        while problem.isExplored(state):
            next=pop()
            if not next:
                # explored all nodes and didnt find a solution
                return None

            actions, state = next

        # did we get to a goal state?
        # this is important that we dont check this while a node is being expended
        # since we would possibly miss another node (a sister node) that is considered a cheaper goal
        if problem.isGoalState(state):
            return actions
        #  finally the node is considered explored
        problem.explore(state)

    return None


def uniformCostSearch(problem):
    "Search the node of least total cost first. Pushing a priority of g(n)"
    pq = u.PriorityQueue()
    return search(problem, lambda: pq.pop() if pq else False,lambda history, state: pq.push((history, state), problem.getCostOfActions(history)))


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """
     "Search the node that has the lowest combined cost and heuristic first."
     Pushing a priority of g(n)+h(n)

    """

    pq=u.PriorityQueue()

    return search(problem, lambda : pq.pop() if pq.heap else None,lambda history,state: pq.push((history,state),problem.getCostOfActions(history)+heuristic(state,problem)))


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch