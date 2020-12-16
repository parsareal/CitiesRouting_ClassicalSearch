
from collections import defaultdict
import Queue as Q
import copy


class UCSSearch:

    def __init__(self, problem):

        self.problem = problem
        # self.graph = defaultdict(list)
        self.graph = problem.graph

    def setGraph(self, g):
        self.graph = g

    # function to add an edge to graph 
    def addEdge(self, u, v, c):
        self.graph[u].append([v, c])

    # Function to print a BFS of graph 
    def BFS(self, s):

        # Mark all the vertices as not visited 
        # visited = [False] * (len(self.graph)) 
        visitedNodes = 0
        expandedNodes = 0
        queueSize = 0
        bestPath = []
        bestPathCost = 0
        maxStorageCost = 0
        visited = []
        # Create a queue for BFS 
        queue = Q.PriorityQueue()

        
        queue.put((0, s))
        queueSize += 1
        visited.append(s)
        visitedNodes += 1
        maxStorageCost += 1
        self.problem.setParent(s, 0)

        while not queue.empty():

            # Dequeue a vertex from 
            # queue and print it  
            dequeued_item = queue.get()
            queueSize -= 1
            currentNode = dequeued_item[1]
            # print currentNode, '\n'
            if self.problem.checkGoalState(currentNode): break
            
            actions = self.problem.getAvailableActions(currentNode)
            expandedNodes += 1
            for a in actions:
                result = self.problem.getActionResult(currentNode, a)
                cost = self.problem.actionCost(currentNode, a)
                if result not in visited:
                    self.problem.setParent(result, currentNode)
                    queue.put((dequeued_item[0] + cost, result))
                    queueSize += 1
                    visited.append(result)
                    visitedNodes += 1
                    maxStorageCost = max (len(visited) + queueSize, maxStorageCost)
                    

        bestPath = self.problem.findBestPath()
        bestPathCost = self.problem.findBestPathCost(bestPath)
        print 'BEST_PATH:  ', bestPath, '\n'
        print 'BEST_PATH_COST:  ', bestPathCost, '\n'        
        print "MAX_STORAGE: ", maxStorageCost, '\n'
        print "EXPANDED_NODES: ", expandedNodes, '\n'
        print "VISITED_NODES: ", visitedNodes, '\n'

