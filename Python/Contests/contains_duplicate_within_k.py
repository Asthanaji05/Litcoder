def contains_duplicates_within_k(arr, k):
    # Dictionary to store the last seen index of each element
    element_indices = {}

    # Iterate through the array
    for i, value in enumerate(arr):
        # Check if the element is already in the dictionary
        if value in element_indices:
            # Check if the current index and the last seen index of the element are within distance k
            if i - element_indices[value] <= k:
                return "Yes"
        
        # Update the dictionary with the current index of the element
        element_indices[value] = i
    
    # If no duplicates are found within distance k
    return "No"

# Example usage
arr1 = [1, 2, 3, 4, 1]
k1 = 4
print(contains_duplicates_within_k(arr1, k1))  # Output: Yes

arr2 = [9, 5, 2, 4, 2, 5, 7]
k2 = 2
print(contains_duplicates_within_k(arr2, k2))  # Output: No