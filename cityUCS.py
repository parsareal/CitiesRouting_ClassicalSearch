# from dfs import Graph
from cityProblem import Problem
from ucs import UCSSearch

cityProblem = Problem()
ucs = UCSSearch(cityProblem)
cityProblem.setEdges()
# bfs.setGraph(cityProblem.graph)
cityProblem.setInitialState("Arad")
cityProblem.setGoalState("Bucharest")
ucs.BFS(cityProblem.initialState)