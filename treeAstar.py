
from collections import defaultdict
import Queue as Q



class AstarSearch:

    def __init__(self, problem):

        self.problem = problem
        # self.graph = defaultdict(list)
        self.graph = problem.graph

    def setGraph(self, g):
        self.graph = g

    def addEdge(self, u, v, c):
        self.graph[u].append([v, c])

    def BFS(self, s):

        # visited = [False] * (len(self.graph)) 
        visitedNodes = 0
        expandedNodes = 0
        bestPath = []
        bestPathCost = 0
        maxStorageCost = 0
        queueSize = 0
        # visited = []
        queue = Q.PriorityQueue()

        # sNum = self.problem.getCityNumber(s) 
        queue.put((0, s, 0))
        queueSize += 1
        # visited.append(s)
        visitedNodes += 1
        maxStorageCost += 1

        while not queue.empty():

            dequeued_item = queue.get()
            queueSize -= 1
            currentNode = dequeued_item[1]
            print currentNode, '\n'
            print dequeued_item[0]
            if self.problem.checkGoalState(currentNode): break
            
            actions = self.problem.getAvailableActions(currentNode)
            expandedNodes += 1
            for a in actions:
                result = self.problem.getActionResult(currentNode, a)
                cost = self.problem.actionCost(currentNode, a)
                huristic = self.problem.getStateHuristic(a[0])
                # if result not in visited:
                queue.put((dequeued_item[2] + cost + huristic[0], result, dequeued_item[2] + cost))
                queueSize += 1
                    # visited.append(result)
                visitedNodes += 1
                maxStorageCost = max(queueSize, maxStorageCost)
                    # maxStorageCost = len(visited)
    
        print("MAX_STORAGE: ", maxStorageCost, '\n')
        print("EXPANDED_NODES: ", expandedNodes, '\n')
        print("VISITED_NODES: ", visitedNodes, '\n')
