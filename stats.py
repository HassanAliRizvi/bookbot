import sys
def get_each_word():
    word_count_dict = {}
    text = get_book_text(sys.argv[1])
    words = text.split() # class <list>
    print("--------- Character Count -------")
    for word in words:
        for letter in word:
            lower_case_word = letter.lower()
            if lower_case_word not in word_count_dict:
                word_count_dict[lower_case_word] = 0
            word_count_dict[lower_case_word] += 1
    #print(word_count_dict)

    for key,value in word_count_dict.items():
        print(f"{key}: {value}")

    #print(word.lower())

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def num_words():
    text = get_book_text(sys.argv[1]) # "./books/frankenstein.txt"
    num_words = len(text.split())
    print("----------- Word Count ----------")
    return f"Found {num_words} total words"
