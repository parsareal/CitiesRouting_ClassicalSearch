
from collections import defaultdict 
from bfs import Graph

class Problem:

    def __init__(self):
        self.graph = defaultdict(list)
        self.huristics = defaultdict(list) 
        self.parents = defaultdict(list)   
        # self.graphToInteger = {
        #     "Oradea": 0,
        #     "Zerind": 1,
        #     "Arad": 2,
        #     "Sibiu": 3,
        #     "Timisoara": 4,
        #     "Fagaras": 5,
        #     "Rimnicu Vilcea": 6,
        #     "Lugoj": 7,
        #     "Pitesti": 8,
        #     "Mehadia": 9,
        #     "Dobreta": 10,
        #     "Craiova": 11,
        #     "Giurgiu": 12,
        #     "Bucharest": 13,
        #     "Urziceni": 14,
        #     "Hirsova": 15,
        #     "Eforie": 16,
        #     "Vaslui": 17,
        #     "Iasi": 18,
        #     "Neamt": 19
        # }    

    def setEdges(self):
        self.addEdge("Oradea", "Zerind", 71)
        self.addEdge("Oradea", "Sibiu", 151)

        self.addEdge("Zerind", "Arad", 75)
        self.addEdge("Arad", "Sibiu", 140)
        self.addEdge("Arad", "Timisoara", 118)
        self.addEdge("Timisoara", "Lugoj", 111)
        self.addEdge("Lugoj", "Mehadia", 70)
        self.addEdge("Mehadia", "Dobreta", 75)
        self.addEdge("Dobreta", "Craiova", 120)

        self.addEdge("Sibiu", "Fagaras", 99)
        self.addEdge("Sibiu", "Rimnicu Vilcea", 80)
        self.addEdge("Fagaras", "Bucharest", 211)
        self.addEdge("Rimnicu Vilcea", "Pitesti", 97)
        self.addEdge("Rimnicu Vilcea", "Craiova", 146)
        self.addEdge("Craiova", "Pitesti", 138)
        self.addEdge("Pitesti", "Bucharest", 101)

        self.addEdge("Bucharest", "Giurgiu", 90)
        self.addEdge("Bucharest", "Urziceni", 85)
        self.addEdge("Urziceni", "Hirsova", 98)
        self.addEdge("Hirsova", "Eforie", 86)

        self.addEdge("Urziceni", "Vaslui", 142)
        self.addEdge("Vaslui", "Iasi", 92)
        self.addEdge("Iasi", "Neamt", 87)


    def setHuristics(self): 
        self.huristics['Arad'].append(366)
        self.huristics['Bucharest'].append(0)
        self.huristics['Craiova'].append(160)
        self.huristics['Dobreta'].append(242)
        self.huristics['Eforie'].append(161)
        self.huristics['Fagaras'].append(178)
        self.huristics['Giurgiu'].append(77)
        self.huristics['Hirsova'].append(151)
        self.huristics['Iasi'].append(226)
        self.huristics['Lugoj'].append(244)
        self.huristics['Mehadia'].append(241)
        self.huristics['Neamt'].append(234)
        self.huristics['Oradea'].append(380)
        self.huristics['Pitesti'].append(98)
        self.huristics['Rimnicu Vilcea'].append(193)
        self.huristics['Sibiu'].append(253)
        self.huristics['Timisoara'].append(329)
        self.huristics['Urziceni'].append(80)
        self.huristics['Vaslui'].append(199)
        self.huristics['Zerind'].append(374)

        


    def setParent(self, v, parent):
        self.parents[v] = parent

    def getParent(self, v):
        return self.parents[v]

    def addEdge(self, u, v, c):
		self.graph[u].append([v, c]) 
		self.graph[v].append([u, c]) 


    def setInitialState(self, s):
        # self.initialState = self.graphToInteger.get(s)
        self.initialState = s
    
    def setGoalState(self, g):
        self.goalState = g

    def getAvailableActions(self, v):
        return self.graph[v]
    
    def getActionResult(self, v, a):
        return a[0]
    
    def getStateHuristic(self, v):
        return self.huristics[v]

    def checkGoalState(self, g):
        if g == self.goalState:
            return True
        else:
            return False
    
    def actionCost(self, v, a):
        for i in self.graph[v] :
            if i[0] == a[0] :
                tmp = i[1]
        return tmp

    def findBestPath(self):
        bestPath = []
        start = self.goalState
        bestPath.append(start)
        while self.getParent(start) != 0:
            bestPath.append(self.getParent(start))
            start = self.getParent(start)
        return bestPath
    

    def findBestPathCost(self, bestPath):
        cost = 0
        for i in range(0, len(bestPath)-1):
            for j in self.graph[bestPath[i]]:
                if j[0] == bestPath[i+1]:
                    cost += j[1]
        return cost
# cityProblem = Problem()
# bfs = Graph(cityProblem)
# cityProblem.setEdges()
# # bfs.setGraph(cityProblem.graph)
# cityProblem.setInitialState("Arad")
# cityProblem.setGoalState("Bucharest")
# bfs.BFS(cityProblem.initialState)