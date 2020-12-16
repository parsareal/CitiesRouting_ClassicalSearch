from treeAstar import AstarSearch
from cityProblem import Problem

cityProblem = Problem()
astar = AstarSearch(cityProblem)
cityProblem.setEdges()
cityProblem.setHuristics()
# bfs.setGraph(cityProblem.graph)
cityProblem.setInitialState("Arad")
cityProblem.setGoalState("Bucharest")
astar.BFS(cityProblem.initialState)