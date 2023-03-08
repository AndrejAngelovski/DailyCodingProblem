# Find the minimum number of coins required to make n cents.

# You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.

# For example, given n = 16, return 3 since we can make it with a 10¢, a 5¢, and a 1¢.

def min_coins(n):
    denominations = [25, 10, 5, 1]
    num_coins = 0

    for coin in denominations:
        num_coins += n // coin
        n %= coin

    return num_coins

n = int(input("Enter a value for n: "))
num_coins = min_coins(n)
print(num_coins)
