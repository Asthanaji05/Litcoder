"""
Transform and compare
"""

def can_transform(start, end):
    if str(start.replace("X", "")) != str(end.replace("X", "")):
        return False
    
    n = len(start)
    i, j = 0, 0
    while i<n and j<n:
        while i < n and start[i]=='X':
            i+=1
        while j < n and end[j]=='X':
            j+=1
        
        if i==n or j==n:
            break
    
        if start[i]!=end[j] or (start[i]=='R' and i>j) or (start[i]=='L' and j>i):
            return False

        i+=1
        j+=1
    return True

start = input().strip()
end = input().strip()
print(can_transform(start, end))
                                                                                                                            