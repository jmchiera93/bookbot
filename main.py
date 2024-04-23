def main():
    book_file_path = "books/frankenstein.txt"
    book_text = get_book_contents(book_file_path)
    book_word_count = get_word_count(book_text)
    char_count_dict = get_char_count(book_text)
    char_count_list = char_dict_to_list(char_count_dict)
    print_report(book_file_path, book_word_count, char_count_list)


def get_book_contents(book_file_path):
    with open(book_file_path) as f:
        return f.read()


def get_word_count(book_text):
    return len(book_text.split())


def get_char_count(book_text):
    book_text_lower = book_text.lower()
    char_count_dict = {}
    for char in book_text_lower:
        if char in char_count_dict:
            char_count_dict[char] += 1
        else:
            char_count_dict[char] = 1
    return char_count_dict


def print_report(book_file_path, book_word_count, char_count_list):
    print(f"--- Begin report of {book_file_path} ---")
    print(f"{book_word_count} words found in the document\n")
    for i in char_count_list:
        print(f"The '{i["char"]}' character was found {i["total"]} times")
    print("--- End report ---")


def char_dict_to_list(char_count_dict):
    char_list = []
    for k, v in char_count_dict.items():
        if k.isalpha():
            char_list.append({"char": k, "total": v})
    char_list.sort(reverse=True, key=sort_on)
    return char_list


def sort_on(dict):
    return dict["total"]


if __name__ == "__main__":
    main()
