def get_book_text(path_to_file):
    with open(path_to_file, encoding='utf-8') as f:
        book_text = f.read()
    return book_text

def main():
    path_to_file= 'books/frankenstein.txt'
    print(get_book_text(path_to_file))
main()