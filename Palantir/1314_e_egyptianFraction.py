# The ancient Egyptians used to express fractions as a sum of several terms where each numerator is one. For example, 4 / 13 can be represented as 1 / 4 + 1 / 18 + 1 / 468.
# Create an algorithm to turn an ordinary fraction a / b, where a < b, into an Egyptian fraction.
import math

def egyptianFraction(nr, dr):
    ef = []
    while nr != 0:
        x = math.ceil(dr / nr)
        ef.append(x)
        nr = x * nr - dr
        dr = dr * x
    for i in range(len(ef)):
        if i != len(ef) - 1:
            print(f"1/{ef[i]} + ", end = "")
        else:
            print(f"1/{ef[i]}")

def main():
    nr = int(input("Enter the first number: "))
    dr = int(input("Enter the second number: "))
    print("Egyptian Fraction Representation of {0}/{1} is ".format(nr, dr))
    egyptianFraction(nr, dr)

if __name__ == "__main__":
    main()