# Ghost is a two-person word game where players alternate appending letters to a word. The first person who spells out a word, or creates a prefix for which there is no possible continuation, loses. Here is a sample game:

# Player 1: g
# Player 2: h
# Player 1: o
# Player 2: s
# Player 1: t [loses]
# Given a dictionary of words, determine the letters the first player should start with, such that with optimal play they cannot lose.

# For example, if the dictionary is ["cat", "calf", "dog", "bear"], the only winning start letter would be b.

def winning_game(s):
    if s[-1] == "t":
        print("You lose")
    elif [s.len() % 2 == 0]:
        print("You lose")
    else:
        print("You win")

def main():
    n = int(input("How many words the dictionary will have: "))
    string_dict = {}
    for i in range(0, n):
        s = input(f"Input word #{i}: ")
        string_dict[i] = s

    for i in range(0, n):
        winning_game(string_dict[i])

if __name__ == "__main__":
    main()