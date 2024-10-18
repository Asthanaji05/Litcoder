"""
Common elements
"""

def get_common_elements(a, b, c):
    return a.intersection(b).intersection(c)
    

a = set(map(int, input().split()))
b = set(map(int, input().split()))
c = set(map(int, input().split()))
result = get_common_elements(a, b, c)
if result:
    print(*(result), sep=' ')
else:
    print("No Elements")
                                                                                                                            