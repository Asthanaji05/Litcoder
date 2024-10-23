import sys
def prodltk(a, k):
    n = len(a)
    p = 1
    res = 0
    start, end = 0, 0
    
    while (end < n):
        p *= a[end]
        
        while (start < end and p >= k):
            p = int(p//a[start])
            start += 1
        
        if (p < k):
            l = end-start + 1
            res += l
        
        end += 1
    
    return res

output = prodltk(list(map(int, input().split())), int(input()))
print(output)