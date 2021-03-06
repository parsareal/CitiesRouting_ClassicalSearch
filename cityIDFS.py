# from dfs import Graph
from cityProblem import Problem
from ldfs import DFSSearch

cityProblem = Problem()
dfs = DFSSearch(cityProblem)
cityProblem.setEdges()
# bfs.setGraph(cityProblem.graph)
cityProblem.setInitialState("Arad")
cityProblem.setGoalState("Bucharest")
dfs.DFS(cityProblem.initialState, 6)