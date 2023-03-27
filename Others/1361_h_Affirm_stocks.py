# Given a array of numbers representing the stock prices of a company in 
# chronological order, write a function that calculates the maximum profit 
# you could have made from buying and selling that stock. You're also given 
# a number fee that represents a transaction fee for each buy and sell transaction.
# You must buy before you can sell the stock, but you can make as many transactions as you like.
# For example, given [1, 3, 2, 8, 4, 10] and fee = 2, you should return 9, since you
# could buy the stock at 1 dollar, and sell at 8 dollars, and then buy it at 4 dollars 
# and sell it at 10 dollars. Since we did two transactions, there is a 4 dollar fee, 
# so we have 7 + 6 = 13 profit minus 4 dollars of fees.

def max_profit(prices, fee):
    if len(prices) < 2:
        return 0
    
    # Initialize variables
    max_profit = 0
    min_price = prices[0]

    # Loop through prices, keeping track of min_price and max_profit
    for price in prices:
        if price < min_price:
            min_price = price
        elif price > min_price + fee:
            profit = price - min_price - fee
            max_profit += profit
            min_price = price - fee
        
    return max_profit

# Get input from user
n = int(input("Enter the number of stock prices: "))
prices = []
for i in range(n):
    price = int(input(f"Enter price {i+1}: "))
    prices.append(price)
fee = int(input("Enter the transaction fee: "))

# Call the function and print the result
result = max_profit(prices, fee)
print(result)