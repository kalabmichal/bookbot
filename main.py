from stats import get_book_text
from stats import characters
from stats import sortedList
import sys

def count_words(text):
    kolik = text.split()
    return kolik

def print_report(path, word_count, char_counts):
    # Print the header
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    
    # Print word count section
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    
    # Print character count section
    print("--------- Character Count -------")

    sorted_chars = sortedList(char_counts)
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    
    # Print footer
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        kde = str(sys.argv[1])
        vypis = get_book_text(kde)
        kolik = count_words(vypis)
        ch = characters(vypis)
        print_report(kde, len(kolik), ch)

main()