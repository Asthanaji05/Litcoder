import sys
from collections import deque

def is_bipartite(graph):
    n = len(graph)
    color = [-1] * n  # -1 means uncolored, 0 and 1 are the two colors

    for start in range(n):
        if color[start] == -1:  # not yet colored
            queue = deque([start])
            color[start] = 0  # start coloring with color 0

            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if color[neighbor] == -1:  # if the neighbor is not colored
                        color[neighbor] = 1 - color[node]  # color with opposite color
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:  # if the neighbor has the same color
                        return False
    return True

# Taking input for the graph
n = int(input())
graph = []
for _ in range(n):
    edges = list(map(int, input().split()))
    graph.append(edges)

print(is_bipartite(graph))

