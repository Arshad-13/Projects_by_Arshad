#Prototyoe programs to handle library operations
class Library:
    def __init__(self):
        self.categories = {}
        self.members = {}
        self.issued_books = []
        
    def add_books(self, category, books):
        self.categories[category] = books
    
    def display_books(self, category):
        print(f"There are {len(self.categories[category])} books in {category}")
        print(self.categories[category])
    
    def remove_books(self, category, books):
        self.categories[category].remove(books)
        
    def search_books(self, category, book):
        if book in self.categories[category]:
            print(f"{book} is available in __ section")
        else:
            print("Book is not available in the library")
        
    def check_out(self, members,category, book):
        if book in self.categories[category]:
            if book in self.issued_books:
                print("Book is already issued")
            else:
                self.issued_books.append(book)
                print(f"{members} has checked out {book}")
                print("Book should be returned within 7 days or reissued")
        else:
            print("Book is not available in the library")
            
    def return_book(self, members, book):
        if book in self.issued_books:
            self.issued_books.remove(book)
            print(f"{members} has returned {book}")
        else:
            print("Book was not issued from this library")
    
    def display_issued_books(self):
        if len(self.issued_books) == 0:
            print("No books issued")
        else:
            print(f"There are {len(self.issued_books)} books issued")
            print(self.issued_books)
