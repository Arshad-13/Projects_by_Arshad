import Libops as los
import liblogin as llg


def main():
    library = los.Library()
    print("Welcome to the library")
    
    while True:
        print("Enter Exit to terminate ")
        Lnm = input("Enter the name: ")
        if Lnm == "Exit":
            break
        LID = input("Enter the ID: ")
        IDps = input("Enter the password: ")
        
        login = llg.LoginID(Lnm, LID, IDps)
        if login.verify_member(Lnm, LID, IDps):
            print("Welcome", Lnm)
            while True:
                print("1. Add books to the library")
                print("2. Remove books from the library")
                print("3. Display books in the library")
                print("4. Search for a book in the library")
                print("5. Check out a book")
                print("6. Return a book")
                print("7. Display issued books")
                print("8. Exit")
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    x = int(input("Enter the number of categories: "))
                    for i in range(x):
                        category = input("Enter the category name: ")
                        y = int(input("Enter the number of books in the category: "))
                        books = []
                        for j in range(y):
                            book = input("Enter the book name: ")
                            books.append(book)
                        library.add_books(category, books)
                elif choice == 2:
                    category = input("Enter the category: ")
                    book = input("Enter the book: ")
                    library.remove_books(category, book)
                elif choice == 3:
                    category = input("Enter the category: ")
                    library.display_books(category)
                elif choice == 4:
                    category = input("Enter the category: ")
                    book = input("Enter the book: ")
                    library.search_books(category, book)
                elif choice == 5:
                    members = input("Enter the name of the member: ")
                    category = input("Enter the category: ")
                    book = input("Enter the book: ")
                    library.check_out(members,category, book)
                elif choice == 6:
                    members = input("Enter the name of the member: ")
                    book = input("Enter the book: ")
                    library.return_book(members, book)
                elif choice == 7:
                    library.display_issued_books()
                elif choice == 8:
                    break
        else:
            print("Incorrect ID or password\nTry again")
    
    
if __name__ == '__main__':
    main()