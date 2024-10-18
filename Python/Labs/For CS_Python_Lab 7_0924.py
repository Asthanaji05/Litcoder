"""
Divisble sum pairs
find the number of pairs of integers in an array whose sum is divisible by a 
given number.
"""


import sys

def divisible_pairs(arr, n):
    """
    To check for all possible pairs sum upto a divisible by n
    """
    l = len(arr)
    count = 0
    for i in range(l):
        for j in range(i+1, l):
            if (arr[i] + arr[j]) % n == 0:
                count += 1
                
    return count
            
n = int(input())
arr = list(map(int, input().split()))
result = divisible_pairs(arr, n)
print(result)
                                                                                                                            