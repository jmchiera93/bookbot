def main():
    book_file_path = "books/frankenstein.txt"
    book_text = get_book_contents(book_file_path)
    book_word_count = get_word_count(book_text)
    book_char_count = get_char_count(book_text.lower())
    # print(book_text)
    print(f"There are {book_word_count} words in the book.")
    print(book_char_count)


def get_book_contents(book_file_path):
    with open(book_file_path) as f:
        return f.read()


def get_word_count(book_text):
    return len(book_text.split())


def get_char_count(book_text):
    book_text_list = book_text.split()
    char_count_dict = {}
    for word in book_text_list:
        for char in word:
            if char not in char_count_dict.keys():
                char_count_dict[char] = int(1)
            else:
                char_count_dict[char] += 1
    return char_count_dict


if __name__ == "__main__":
    main()
