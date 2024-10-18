"""
Array manipulation:
"""

def perform_operations(n, queries):
    arr = [0]*n
    for q in queries:
        for i in range(q[0]-1, q[1]):
            arr[i] += q[2]
    return max(arr)

arraysize = int(input())
num_queries = int(input())
queries = [list(map(int, input().split())) for _ in range(num_queries)]
result = perform_operations(arraysize, queries)
print(result)
                                                                                                                            