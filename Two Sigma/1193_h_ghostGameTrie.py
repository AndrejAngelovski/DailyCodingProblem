# Ghost is a two-person word game where players alternate appending letters to a word. The first person who spells out a word, or creates a prefix for which there is no possible continuation, loses. Here is a sample game:

# Player 1: g
# Player 2: h
# Player 1: o
# Player 2: s
# Player 1: t [loses]
# Given a dictionary of words, determine the letters the first player should start with, such that with optimal play they cannot lose.

# For example, if the dictionary is ["cat", "calf", "dog", "bear"], the only winning start letter would be b.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
    
class GhostGame:
    def __init__(self, dictionary):
        self.root = TrieNode()
        for word in dictionary:
            self.add_word(word)

    def add_word(self, word):
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]
        node.is_word = True
    
    def first_player_winning_letters(self):
        return [letter for letter in self.root.children if self.can_win(self.root.children[letter])]
    
    def can_win(self, node, is_first_player = True):
        if not node.children:
            return not is_first_player
        if node.is_word and not is_first_player:
            return False
        if any(self.can_win(node.children[letter], not is_first_player) for letter in node.children):
            return True
        return False

def main():
    string_dictionary = []
    n = int(input("How many words the dictionary will have: "))
    for i in range(0, n):
        s = input(f"Input word #{i + 1}: ")
        string_dictionary.append(s)
    game = GhostGame(string_dictionary)
    print(game.first_player_winning_letters())

if __name__ == "__main__":
    main()