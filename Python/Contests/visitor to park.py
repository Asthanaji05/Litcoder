def preprocess_visitors(visitors):
    # Handle non-integer or invalid input
    try:
        visitors = list(map(int, visitors))
    except ValueError:
        return "Input is not in correct format or missing"
    
    # Initialize prefix sum array
    prefix_sum = [0] * (len(visitors) + 1)
    
    # Compute prefix sum array
    for i in range(1, len(visitors) + 1):
        prefix_sum[i] = prefix_sum[i - 1] + visitors[i - 1]
    
    return prefix_sum

def total_visitors_in_range(prefix_sum, start, end):
    # Check if query indices are valid
    if start < 0 or end >= len(prefix_sum) - 1 or start > end:
        return 0
    
    if start == 0:
        return prefix_sum[end + 1]
    else:
        return prefix_sum[end + 1] - prefix_sum[start]

# Input reading and processing
def process_input():
    try:
        # Reading visitors array
        visitors = input().split()
        prefix_sum = preprocess_visitors(visitors)
        
        if isinstance(prefix_sum, str):  # In case of an error message
            print(prefix_sum)
            return
        
        # Reading number of queries
        num_queries = int(input())
        queries = []
        for _ in range(num_queries):
            query = tuple(map(int, input().split()))
            queries.append(query)
        
        # Processing each query and printing results
        for query in queries:
            start, end = query
            print(total_visitors_in_range(prefix_sum, start, end))
    
    except Exception as e:
        print("Input is not in correct format or missing")

# Run the input processing function
process_input()
