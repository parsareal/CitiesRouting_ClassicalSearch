from collections import defaultdict
import copy
import time

class DFSSearch:

    def __init__(self, problem):

        self.problem = problem
        # self.graph = defaultdict(list)
        self.graph = problem.graph


    def DFS(self, v, depth):
        visited = []
        stack = []
        stack.append([v, 0])
        self.problem.setParent(v, 0)
        maxStorage = 0
        visitedNodes = 0
        expandedNodes = 0
        foundGoalState = False

        while len(stack) != 0:
            s = stack.pop(len(stack)-1)
            # print s
            # print 'sdf'
            if s[0] not in visited:
                # print s
                visited.append(s[0])

            expandedNodes += 1
            visitedNodes += 1
            if self.problem.checkGoalState(s[0]):
                foundGoalState = True
                break

            print s[0]
            # print actions
            # time.sleep(5)
            
            if (s[1] < depth):
                actions = self.problem.getAvailableActions(s[0])
                for a in actions:
                    result = self.problem.getActionResult(s[0], a)
                    if result not in visited:
                        self.problem.setParent(result, s[0])
                        visitedNodes += 1
                        stack.append([result, s[1] + 1])
                        maxStorage = max(len(visited) + len(stack), maxStorage)
            # else:
            #     # print 'PAr: ' , self.problem.getParent(s[0])
            #     visited.remove(s[0])
        if foundGoalState == False: print 'NOT FOUND GOAL'
                # print stack
        if foundGoalState == True:
            bestPath = self.problem.findBestPath()
            bestPathCost = self.problem.findBestPathCost(bestPath)
            print 'BEST_PATH:  ', bestPath, '\n'
            print 'BEST_PATH_COST:  ', bestPathCost, '\n'
        print "MAX_STORAGE: ", maxStorage, '\n'
        print "EXPANDED_NODES: ", expandedNodes, '\n'
        print "VISITED_NODES: ", visitedNodes, '\n'

