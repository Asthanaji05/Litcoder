from itertools import product

def find_stock_combinations(target_budget, stocks):
    # Check for invalid inputs: target budget or stock prices
    if target_budget <= 0:
        return "Invalid input"
    
    for stock in stocks:
        if stock[1] <= 0:
            return "The stock prices should be at least greater than 0"
        if stock[1] > target_budget:
            return "One of the stock prices is higher than the target price"
    
    # Prepare variables for combinations
    valid_combinations = []
    prices = [stock[1] for stock in stocks]
    num_stocks = len(stocks)
    
    # Generate combinations using product with quantities 0 to 5 for each stock
    for quantities in product(range(6), repeat=num_stocks):
        total_cost = sum(q * p for q, p in zip(quantities, prices))
        
        # Check if total cost matches the target budget
        if total_cost == target_budget:
            valid_combinations.append(list(quantities))
    
    # Sort combinations in ascending order
    valid_combinations.sort()
    
    # Prepare the output
    if valid_combinations:
        output = "\n".join(" ".join(map(str, comb)) for comb in valid_combinations)
        return f"{output}\n{len(valid_combinations)}"
    else:
        return "No valid combinations found"

# Input handling function
def main():
    try:
        # Input maximum budget
        target_budget = int(input())
        
        # Input number of stocks
        num_stocks = int(input())
        stocks = []
        
        # Input each stock's name and price
        for _ in range(num_stocks):
            stock_input = input().split()
            stock_name = stock_input[0]
            stock_price = int(stock_input[1])
            stocks.append((stock_name, stock_price))
        
        # Find valid combinations
        result = find_stock_combinations(target_budget, stocks)
        print(result)
    
    except ValueError:
        print("Invalid Input")

# Run the program
main()
