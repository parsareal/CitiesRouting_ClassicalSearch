from collections import defaultdict
import copy
import time

class DFSSearch:

    def __init__(self, problem):

        self.problem = problem
        # self.graph = defaultdict(list)
        self.graph = problem.graph


    def DFS(self, v):
        visited = []
        stack = []
        stack.append(v)
        self.problem.setParent(v, 0)
        maxStorage = 0
        visitedNodes = 0
        expandedNodes = 0

        while len(stack) != 0:
            s = stack.pop(len(stack)-1)
            # print s
            # print 'sdf'
            if s not in visited:
                # print s
                visited.append(s)

            expandedNodes += 1
            visitedNodes += 1
            if self.problem.checkGoalState(s):
                break

            actions = self.problem.getAvailableActions(s)
            # print actions
            # time.sleep(5)
            for a in actions:
                result = self.problem.getActionResult(s, a)
                if result not in visited:
                    self.problem.setParent(result, s)
                    visitedNodes += 1
                    stack.append(result)
                    maxStorage = max(len(visited) + len(stack), maxStorage)
            # print stack
        
        bestPath = self.problem.findBestPath()
        bestPathCost = self.problem.findBestPathCost(bestPath)
        print 'BEST_PATH:  ', bestPath, '\n'
        print 'BEST_PATH_COST:  ', bestPathCost, '\n'
        print "MAX_STORAGE: ", maxStorage, '\n'
        print "EXPANDED_NODES: ", expandedNodes, '\n'
        print "VISITED_NODES: ", visitedNodes, '\n'