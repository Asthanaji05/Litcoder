import sys

def doSomething(inval):
    #Do Something
    arr = list(map(int, inval.split()))
    n = len(arr)
    
    if n >=10:
        return "Array size must be between 1 and 10"
    
    if any(arr) not in range(-9, 10):
        return "Array elements must be from -10 to 10"
    
    if min(arr) > 0 or max(arr) < 0:
        return "Array elements must be integers"
        
    n_sum = 0
    s = set()
    
    for i in range(n):
        n_sum += arr[i]
        
        if n_sum == 0 or n_sum in s:
            return f"{True}\n{n}"
        
        s.add(n_sum)
        
    return f"{False}\n{n}"

input = input()
#input = int(input())
output = doSomething(input)
print (output)
                                                                                                                            