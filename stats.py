def get_book_text(path_to_file):
    with open(path_to_file) as f:
        content = f.read()
    return content

def characters(text):
    dict = {}
    text2 = text.lower()
    for i in text2:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    return dict

def sortedList(list):
    #hlavicka = "============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------\nFound 75767 total words\n--------- Character Count -------\n"
    sortedL = list.sort()
    #for i in sorted:
        #if i.isalpha() == False:
            #i.remove()
    return sortedL
