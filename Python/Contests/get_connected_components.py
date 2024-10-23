"""
Number of provinces
"""


def get_connected_components(graph, n):
    count = 0
    visited = [False] * n
    
    def dfs(i):
        visited[i] = True
        for j in range(n):
            if graph[i][j] == 1 and not visited[j]:
                dfs(j)
            
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            count+=1
    return count
    
n = int(input())
inputVal = [list(map(int, input().split())) for _ in range(n)]
print(get_connected_components(inputVal, n))