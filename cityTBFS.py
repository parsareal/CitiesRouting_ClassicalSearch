from treeBfs import Graph
from cityProblem import Problem

cityProblem = Problem()
bfs = Graph(cityProblem)
cityProblem.setEdges()
cityProblem.setInitialState("Arad")
cityProblem.setGoalState("Bucharest")
bfs.BFS(cityProblem.initialState)