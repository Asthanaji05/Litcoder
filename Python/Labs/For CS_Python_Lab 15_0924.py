"""
Lego Blocks
"""
MOD = 1000000007

def legoWall(n, m):
    # Step 1: Calculate the number of ways to fill a single row
    # Define ways(m) to store the number of ways to fill a row of width m
    ways = [0] * (m + 1)
    
    # Base cases
    ways[0] = 1  # 1 way to fill an empty row
    for i in range(1, m + 1):
        ways[i] = ways[i - 1]  # Place 1-width block
        if i >= 2:
            ways[i] = (ways[i] + ways[i - 2]) % MOD  # Place 2-width block
        if i >= 3:
            ways[i] = (ways[i] + ways[i - 3]) % MOD  # Place 3-width block
        if i >= 4:
            ways[i] = (ways[i] + ways[i - 4]) % MOD  # Place 4-width block
    
    # Step 2: Calculate the number of ways to fill the entire wall without constraints
    total_ways = [1] * (m + 1)
    for i in range(1, m + 1):
        total_ways[i] = pow(ways[i], n, MOD)
    
    # Step 3: Calculate valid walls by removing invalid splits
    valid_ways = [0] * (m + 1)
    valid_ways[0] = 1
    for i in range(1, m + 1):
        valid_ways[i] = total_ways[i]
        for j in range(1, i):
            valid_ways[i] = (valid_ways[i] - (valid_ways[j] * total_ways[i - j]) % MOD + MOD) % MOD
    
    return valid_ways[m]


m, n = int(input()), int(input())
print(legoWall(m, n))
                                                                                                                            