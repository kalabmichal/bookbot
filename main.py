from stats import get_book_text
from stats import characters

def count_words(text):
    kolik = text.split()
    return kolik

def main():
    kde = "books/frankenstein.txt"
    vypis = get_book_text(kde)
    kolik = count_words(vypis)
    p = len(kolik)
    print (str(p) + " words found in the document")
    ch = characters(vypis)
    print(ch)

main()