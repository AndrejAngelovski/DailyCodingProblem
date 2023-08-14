# Given a string of words delimited by spaces, reverse the words in string. For example, given "hello world here", return "here world hello"
# Follow-up: given a mutable string representation, can you perform this operation in-place?

def reverse_words(s: str) -> str:
    words = s.split()
    reverse_words = ' '.join(reversed(words))
    return reverse_words

def main_reverse_words():
    s = input("Enter a string: ")
    print(reverse_words(s))

def reverse_words_in_list(lst: list) -> None:
    lst[:] = ' '.join(reversed(''.join(lst).split()))

def main_reverse_words_in_list():
    lst = list(input("Enter a string: "))
    reverse_words_in_list(lst)
    print(''.join(lst))

if __name__ == "__main__":
    main_reverse_words()
    main_reverse_words_in_list()
