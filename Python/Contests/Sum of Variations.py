def find_combinations(m, r, target):
    # Helper function for backtracking
    def backtrack(item_index, current_sum):
        # Base case: when all items are considered
        if item_index == m:
            if current_sum == target:
                return 1
            else:
                return 0
        
        # Try all variations for the current item (values from 1 to r)
        count = 0
        for variation in range(1, r + 1):
            # Recursively try the next item
            if current_sum + variation <= target:
                count += backtrack(item_index + 1, current_sum + variation)
        
        return count
    
    # Call the backtracking function starting from the first item
    return backtrack(0, 0)

# Input
m = int(input())        # Number of items
r = int(input())        # Number of variations per item
target = int(input())   # Target sum

# Output
print(find_combinations(m, r, target))
