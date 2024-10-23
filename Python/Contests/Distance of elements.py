"""
Distance of elements
"""

def is_duplicate_present(arr, k):
    n = len(arr)
    window = set()
    for i in range(k+1):
        if arr[i] in window:
            return "Yes"
        window.add(arr[i])
        
    for i in range(k+1, n):
        print(window ,i)
        window.remove(arr[i-(k+1)])
        if arr[i] in window:
            return "Yes"
        window.add(arr[i])
    return "No"
    
    
inputVal = list(map(int, input().split()))
k = int(input())
print(is_duplicate_present(inputVal, k))
