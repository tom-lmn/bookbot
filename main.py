import sys
from stats import get_num_words
from stats import get_char_nums
from stats import sort_char_dict 

def main():
    if not len(sys.argv) == 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]
    text = get_book_text(path)
    word_count = get_num_words(text)
    char_nums = get_char_nums(text)
    sorted_dict = sort_char_dict(char_nums)
    #print(f"{word_count} words found in the document")
    #print(char_nums)
    print("============ BOOKBOT ============")
    print("Analyzing book found at " + path)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")    
    print_sorted_list(sorted_dict)
    print("============= END ===============")
    
def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_sorted_list(list):
    for d in list:
        if d["char"].isalpha():
            print(f"{d["char"]}: {d["num"]}")
main()
