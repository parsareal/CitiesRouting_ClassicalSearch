
from collections import defaultdict

class Graph: 

	def __init__(self, problem): 

		self.problem = problem
		# self.graph = defaultdict(list)
		self.graph = problem.graph

	def setGraph(self, g):
		self.graph = g

	def addEdge(self,u,v,c): 
		self.graph[u].append([v, c]) 

	def BFS(self, s): 

		# Mark all the vertices as not visited 
		# visited = [False] * (len(self.graph)) 
		visitedNodes = 0
		expandedNodes = 0
		bestPath = []
		bestPathCost = 0
		maxStorageCost = 0
		visited = []
		queue = []

		# sNum = self.problem.getCityNumber(s) 
		queue.append(s) 
		visited.append(s)
		self.problem.setParent(s, 0)
		visitedNodes += 1
		maxStorageCost += 1

		while queue: 

			s = queue.pop(0)
			# sNum = self.problem.getCityNumber(s) 
			# print s, '\n'                                 this is tracker
			if self.problem.checkGoalState(s):
				break
			
			actions = self.problem.getAvailableActions(s)
			expandedNodes += 1
			for a in actions:
				result = self.problem.getActionResult(s, a)
				if result not in visited:
					self.problem.setParent(result, s)
					queue.append(result)
					visited.append(result)
					visitedNodes += 1
					maxStorageCost = max (len(visited) + len(queue), maxStorageCost)
		
		bestPath = self.problem.findBestPath()
		bestPathCost = self.problem.findBestPathCost(bestPath)
		print 'BEST_PATH:  ', bestPath, '\n'
		print 'BEST_PATH_COST:  ', bestPathCost, '\n'
		print "MAX_STORAGE: ", maxStorageCost, '\n'
		print "EXPANDED_NODES: ", expandedNodes, '\n'
		print "VISITED_NODES: ", visitedNodes, '\n'



