# Implement division of two positive integers without using the division, multiplication, or modulus operators. Return the quotient as an integer, ignoring the remainder.
def divide(dividend, divisor):
    quotient = 0
    while dividend >= divisor:
        dividend -= divisor
        quotient += 1
    return quotient

def main():
    dividend = 15
    divisor = 2
    print(divide(dividend, divisor))

if __name__ == "__main__":
    main()