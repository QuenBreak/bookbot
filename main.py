def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    alpha_dict = get_alpha_dict(text)
    sorted_na = get_sort(alpha_dict)
    print ((f"--- Begin report of {book_path} ---"))
    print (f"{num_words} words found in the document")
    print ("")
    get_print_sort(sorted_na)
    print ("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_alpha_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if str.isalpha(c):
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
    return chars

def get_sort(alpha_dict):
    return dict(reversed(sorted(alpha_dict.items(), key=lambda key_val: key_val[1])))

def get_print_sort(sorted_na):
    w = sorted_na.items()
    for i in w:
        print(f"The '{i[0]}' character was found {i[1]} times")

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()