def find_candies(total, prices):
    price_map = {}  # to store the price and its 1-based index
    
    for i, price in enumerate(prices):
        difference = total - price
        if difference in price_map:
            # Return the 1-based indices
            return price_map[difference], i + 1
        price_map[price] = i + 1  # store the 1-based index

# Example 1
total1 = 10
prices1 = [2, 3, 4, 5, 5]
result1 = find_candies(total1, prices1)
print(result1)  # Output: (4, 5)

# Example 2
total2 = 8
prices2 = [1, 4, 7, 6, 8]
result2 = find_candies(total2, prices2)
print(result2)  # Output: (1, 3)