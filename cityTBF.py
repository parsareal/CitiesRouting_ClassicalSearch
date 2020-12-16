# from dfs import Graph
from cityProblem import Problem
from treeBf import bestFirstSearch

cityProblem = Problem()
bf = bestFirstSearch(cityProblem)
cityProblem.setEdges()
cityProblem.setHuristics()
# bfs.setGraph(cityProblem.graph)
cityProblem.setInitialState("Arad")
cityProblem.setGoalState("Bucharest")
bf.BFS(cityProblem.initialState)