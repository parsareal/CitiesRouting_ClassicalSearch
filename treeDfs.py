from collections import defaultdict

class DFSSearch:

    def __init__(self, problem):

        self.problem = problem
        # self.graph = defaultdict(list)
        self.graph = problem.graph

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v):

        # visited.append(v)
        print v, '\n'

        actions = self.problem.getAvailableActions(v)

    # for a in actions:
    #     result = self.problem.getActionResult(v, a)
    #     if result not in visited:
    #       self.DFSUtil(a, visited)

        for a in actions:
            result = self.problem.getActionResult(v, a)
            # if result not in visited:
            self.DFSUtil(result)


    def DFS(self, v):
        # visited = []
        # DFS traversal
        self.DFSUtil(v)

