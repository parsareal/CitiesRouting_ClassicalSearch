from bfs import Graph
from cityProblem import Problem

cityProblem = Problem()
bfs = Graph(cityProblem)
cityProblem.setEdges()
# bfs.setGraph(cityProblem.graph)
cityProblem.setInitialState("Arad")
cityProblem.setGoalState("Bucharest")
bfs.BFS(cityProblem.initialState)