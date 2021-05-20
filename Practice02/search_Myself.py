# 아래에 있는 aStarSearch 함수를 직접 짜 보았습니다.
# 코드 출처 -> http://ai.berkeley.edu/search.html
# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())

    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def yhk_manhattanHeuristic(position, problem, info={}):
    "The Manhattan distance heuristic for a PositionSearchProblem"
    xy1 = position
    xy2 = problem.goal
    return abs(xy1[0] - xy2[0]) + abs(xy1[1] - xy2[1])

def yhk_euclideanHeuristic(position, problem, info={}):
    "The Euclidean distance heuristic for a PositionSearchProblem"
    xy1 = position
    xy2 = problem.goal

	#"*** SANGMYUNG UNIV. YOUR CODE HERE ***"
    return 0

def aStarSearch(problem):
    """Search the node that has the lowest combined cost and heuristic first."""
    # 내가 짠 코드
    #"*** SANGMYUNG UNIV. YOUR CODE HERE ***"

    # 결과 확인하기
    print “Start:”, problem.getStartState() # 시작 좌표
    print “Is the start a goal?”, problem.isGoalState(problem.getStartState()) # 시작위치가 도착위치인가?
    print “Goal:”, problem.goal # 도착(타겟) 위치
    print “Start’s successors:”, problem.getSuccessors(problem.getStartState()) # 시작노드의 자식노드들
    # 수도 코드

    # --- Initialization ---
    # n0 <- source node
    # OPEN <- OPEN U {n0}
    # CLOSED <- empty

    # --- Excusion ---
    """
    while (OPEN is not empty){
      n <- OPEN
      if ( problem.isGoalstate(n)) # 타겟노드를 찾으면 끝
        return actions
      CLOSED <- n
      M <- child nodes of n
      +) if ( m is in CLOSED ) -> continue
      +) f^ = g + h^
      OPEN <- OPEN U M
      sort OPEN according to f^
    }
    return FAIL
    """

    # --- Initialization ---
    n0 = problem.getStartState() # 시작 위치
    OPEN = util.PriorityQueue() # Open list, PRiorityQueue로 만들기 (알아서 정렬이 됨)
    OPEN.push((n0, [], 0), 0) # ((Coordinate of node, action to current node, cost to current node), priority) , ((현재좌표, 액션, 코스트), f값)
    CLOSED = [] # CLOSED List

    # --- Excusion ---
    while(!Open.isEmpty()){ # OPEN리스트가 비었으면
        n = OPEN.pop() # n = OPEN리스트의 가장 앞 값

        if(problem.isGoalState(n)): # 타겟에 도착했다면
            return n_actions # 타겟노드까지 온 경로

        CLOSED.append(n) # 이미 거쳐간 노드
        M = problem.getSuccessors(n) # M = n의 자식 노드
        for m, m_action, m_g in M:
            if(m in CLOSED): # m 값이 CLOSED에 있다면
                continue
            g = n_g + m_g # 부모의 g + 자식의 초기값
            h = yhk_manhattanHeuristic(m, problem) # h^, heuristic cost
            f = g + h
            actions = [n_actions] + [m_action] # n의 action + m의 action
            OPEN.push((m, actions, g), f) # OPEN리스트에 자식노드 추가, 정렬은 알아서 됨
    }

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
