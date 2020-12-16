
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

		visitedNodes = 0
		expandedNodes = 0
		bestPath = []
		bestPathCost = 0
		maxStorageCost = 0
		# visited = []
		queue = []

		# sNum = self.problem.getCityNumber(s) 
		queue.append(s) 
		# visited.append(s)
		self.problem.setParent(s, 0)
		visitedNodes += 1
		maxStorageCost += 1

		while queue: 

			s = queue.pop(0)
			# sNum = self.problem.getCityNumber(s) 
			# print s, '\n'
			if self.problem.checkGoalState(s):
				break
			actions = self.problem.getAvailableActions(s)
			expandedNodes += 1
			for a in actions:
				result = self.problem.getActionResult(s, a)
				self.problem.setParent(result, s)
				queue.append(result)
					# visited.append(result)
				visitedNodes += 1
				maxStorageCost = max (len(queue), maxStorageCost)
				
				# maxStorageCost = len(visited)

		# bestPath = self.problem.findBestPath()
		# print 'BEST_PATH:  ', bestPath, '\n'
		print "MAX_STORAGE: ", maxStorageCost, '\n'
		print "EXPANDED_NODES: ", expandedNodes, '\n'
		print "VISITED_NODES: ", visitedNodes, '\n'

