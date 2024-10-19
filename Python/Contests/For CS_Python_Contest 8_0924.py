"""
merge two linked list
"""
def merge(n1, a, n2, b):
    res = []
    i, j = 0, 0
    while i < n1 and j < n2:
        res.append(a[i])
        res.append(b[j])
        i+=1
        j+=1
    while i < n1:
        res.append(a[i])
        i+=1
    while j < n2:
        res.append(b[j])
        j+=1
    
    return res

n1 = int(input())
a = [str(input()) for _ in range(n1)]
n2 = int(input())
b = [str(input()) for _ in range(n2)]
print(*(merge(n1, a, n2, b)), sep='\n')