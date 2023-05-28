# Given an undirected graph, determine if it contains a cycle.
# The problem of detecting a cycle in an undirected graph can be solved
# using Depth First Search (DFS). In DFS, for every visited vertex v, 
# if there is an adjacent u such that u is already visited and u is not
# parent of v, then there is a cycle in graph.
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, v, w):
        self.graph[v].append(w)
        self.graph[w].append(v)
    
    def isCyclicUtil(self, v, visited, parent):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                if self.isCyclicUtil(i, visited, v):
                    return True
            elif parent != i:
                return True
        return False
    
    def isCyclic(self):
        visited = [False] * (self.V)
        for i in range(self.V):
            if visited[i] == False:
                if self.isCyclicUtil(i, visited, -1) == True:
                    return True
        return False

def main():
    g1 = Graph(5)
    g1.addEdge(1, 0)
    g1.addEdge(1, 2)
    g1.addEdge(2, 0)
    g1.addEdge(0, 3)
    g1.addEdge(3, 4)
    print("Graph contains cycle" if g1.isCyclic() else "Graph doesn't contain cycle")

if __name__ == "__main__":
    main()