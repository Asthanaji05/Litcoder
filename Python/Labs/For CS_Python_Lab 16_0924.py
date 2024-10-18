"""
cookies
"""

import heapq
def steps_cookies(arr, target):
    heapq.heapify(arr)
    steps = 0
    while arr[0]<=target:
        heapq.heappush(arr, heapq.heappop(arr)+2*heapq.heappop(arr))
        steps+=1
    return steps

target = int(input())
inputVal = list(map(int, input().split()))

print(steps_cookies(inputVal, target))
                                                                                                                            