def main():
    book_path = "books/frankenstein.txt"
    print(read_book(book_path))


def read_book(file_path):
    with open(file_path) as f:
        return f.read()


if __name__ == "__main__":
    main()
