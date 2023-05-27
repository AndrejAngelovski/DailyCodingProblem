# The transitive closure of a graph is a measure of which vertices are reachable from other vertices. It can be represented as a matrix M, where M[i][j] == 1 if there is a path between vertices i and j, and otherwise 0.

# For example, suppose we are given the following graph in adjacency list form:

# graph = [
#     [0, 1, 3],
#     [1, 2],
#     [2],
#     [3]
# ]
# The transitive closure of this graph would be:

# [1, 1, 1, 1]
# [0, 1, 1, 0]
# [0, 0, 1, 0]
# [0, 0, 0, 1]
# Given a graph, find its transitive closure.



def transitive_closure(graph):
    n = len(graph)
    closure = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in graph[i]:
            closure[i][j] = 1

    for k in range(n):
        for i in range(n):
            for j in range(n):
                closure[i][j] = closure[i][j] or (closure[i][k] and closure[k][j])
            
    return closure

def main():
    n = int(input("Enter the number of vertices in the graph: "))
    graph = []
    for i in range(n):
        adjacent_vertices = list(map(int, input(f"Enter the vertices adjacent to vertex {i}, separated by spaces: ").split()))
        graph.append(adjacent_vertices)
    
    print("Transitive closure of the graph:")
    closure = transitive_closure(graph)
    for row in closure:
        print(row)

if __name__ == "__main__":
    main()