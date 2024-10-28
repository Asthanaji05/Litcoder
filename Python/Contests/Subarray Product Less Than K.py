def count_subarrays_with_product_less_than_k(nums, k):
    if k <= 1:  # If k <= 1, no positive product can be less than k
        return 0
    
    left = 0
    product = 1
    count = 0
    
    for right in range(len(nums)):
        product *= nums[right]
        
        while product >= k and left <= right:
            product //= nums[left]
            left += 1
            
        # Number of valid subarrays ending at `right`
        count += (right - left + 1)
    
    return count

arr = list(map(int, input().split()))
k = int(input())
print(count_subarrays_with_product_less_than_k(arr, k))
