def count_matching_bits(x, y):
    # Convert both numbers to 3-bit binary strings
    x_bin = f'{x:03b}'
    y_bin = f'{y:03b}'
    
    # Count matching bits
    match_count = 0
    for xb, yb in zip(x_bin, y_bin):
        if xb == yb:
            match_count += 1
    
    return match_count

def bit_matching_sum(arr):
    # Check for valid input (all integers must be <= 7)
    if any(x > 7 for x in arr):
        return "Invalid Input"
    
    total_sum = 0
    n = len(arr)
    
    # Iterate over all ordered pairs (i, j)
    for i in range(n):
        for j in range(n):
            total_sum += count_matching_bits(arr[i], arr[j])
    
    return total_sum

# Input
arr = list(map(int, input().split()))

# Output
print(bit_matching_sum(arr))
