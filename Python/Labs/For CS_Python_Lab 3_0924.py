def zero_sum_subarray(input_array):

    # Check for array size constraint
    if len(input_array) < 1 or len(input_array) > 10:
        print("Array size must be between 1 and 10")
        return

    # Convert input to integers and check element constraints
    try:
        arr = list(map(int, input_array))
    except ValueError:
        print("Array elements must be integers")
        return

    if any(num < -10 or num > 10 for num in arr):
        print("Array elements must be from -10 to 10")
        return

    # Check for zero sum subarray using a set to track sums
    cumulative_sum = 0
    seen_sums = set()

    for num in arr:
        cumulative_sum += num
        
        # Check if cumulative sum is zero or already seen
        if cumulative_sum == 0 or cumulative_sum in seen_sums:
            print("True")
            print(len(arr))
            return
        
        seen_sums.add(cumulative_sum)

    print("False")
    print(len(arr))

# Call the function
arr = list(map(int, input().split()))
zero_sum_subarray(arr)