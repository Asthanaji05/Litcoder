"""
Egg drop with eggs and n floors
"""
def eggDrop(k, n):
    # Create a DP table to store the results
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    
    # Base case initialization:
    # If there are no floors, 0 moves are needed. If there is 1 floor, 1 move is needed.
    for i in range(1, k + 1):
        dp[i][0] = 0  # No floors, no moves needed
        dp[i][1] = 1  # One floor, one move needed
    
    # If we have 1 egg, we need 'n' moves to check each floor sequentially
    for j in range(1, n + 1):
        dp[1][j] = j
    
    # Fill the rest of the DP table
    for i in range(2, k + 1):
        for j in range(2, n + 1):
            dp[i][j] = float('inf')  # Initialize with a large number
            for x in range(1, j + 1):
                # Worst case: we take the max of the egg breaking and not breaking cases
                res = 1 + max(dp[i-1][x-1], dp[i][j-x])
                dp[i][j] = min(dp[i][j], res)
    
    return dp[k][n]

# Sample input
k = int(input())
n = int(input())
print(eggDrop(k, n))