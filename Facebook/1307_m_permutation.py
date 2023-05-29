# Given a function that generates perfectly random numbers between 1 and k (inclusive), where k is an input, write a function that shuffles a deck of cards represented as an array using only swaps.
# It should run in O(N) time.
# Hint: Make sure each one of the 52! permutations of the deck is equally likely.

import random

def shuffle(deck):
    n = len(deck)
    for i in range(n):
        r = random.randint(i, n-1)
        deck[i], deck[r] = deck[r], deck[i]

def main():
    deck = list(range(1, 53))  # Let's say the deck is represented by numbers 1 through 52
    print("Original deck: ", deck)
    shuffle(deck)
    print("Shuffled deck: ", deck)

if __name__ == "__main__":
    main()
