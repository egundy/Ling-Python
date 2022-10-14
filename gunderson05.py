# functions
def display_menu():
    print('The Book List Program\n')
    print('''
        Command Menu
        list -- List all books
        add -- Add a book
        del -- Delete a book
        exit -- exit program''')

def read_books():
    with open('books.txt','r') as file_in:
        books = file_in.read().splitlines()
        counter = 0
        for i in books:
            counter += 1
            print(counter, i)

def write_books():
    with open('books.txt', 'r+') as file_in:
        books = file_in.read().splitlines()

    
def add_book():
    book = input('Book: ')
    write_books(book)
    
    
def list_books():
    read_books()


# main
def main():
    flag = 0
    while flag == 0:
        display_menu()
        print('\n')
        command = input('Command: ')
        if command == 'list':
            print(read_books())
        if command == 'add':
            add_book()
        if command == 'del':
            pass
        if command == 'exit':
            break
main()