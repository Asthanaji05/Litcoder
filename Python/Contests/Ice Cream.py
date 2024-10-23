import sys
def find_candies(total, prices):
    price_map = {}
    for i, price in enumerate(prices):
        complement = total - price
        if complement in price_map:
            return price_map[complement] + 1, i + 1
        price_map[price] = i
    return None

total = int(input())
prices = list(map(int, input().split()))
result = find_candies(total, prices)
print(" ".join(map(str, result)))
