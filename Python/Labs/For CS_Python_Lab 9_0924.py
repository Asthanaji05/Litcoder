"""
Compare triplets:
Given the scores of Charlie's project (c) and Dave's project (d), determine 
their respective comparison points.

"""

def compare_scores(charlie, dave):
    """
    To compare and assign each to person
    """
    cp, dp = 0, 0
    for c, d in zip(charlie, dave):
        if c > d:
            cp+=1
        elif d > c:
            dp += 1
    return cp, dp

charlie = list(map(int, input().split()))
dave = list(map(int, input().split()))
result = compare_scores(charlie, dave)
print(result[0], result[1])
                                                                                                                            