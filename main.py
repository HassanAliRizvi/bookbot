from stats import get_book_text, num_words, get_each_word
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")

    print(num_words())
    print(get_each_word())
    print("============= END ===============")
main()

