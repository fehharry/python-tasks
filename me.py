class book:
    def __init__(self, titlie, author, book_id):
        self.title = titlie
        self.author = author
        self.book_id = book_id
        self.is_borrowed = False

    def __str__(self):
        print(f"'{self.title}' by {self.author} (ID: {self.book_id})") 
z1 = book ("Geography", "Hamilton", 1)
z2 = book ("Computer Science", "Branly", 2)
z3 = book ("mathematics", "Newton", 3)




class student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.borrowed_books = []

    def borrow_book(self, book, library):
        if library.borrow_book(self, book):
            self.borrowed_books.append(book) 
            print(f"{self.name} has borrowed '{book.title}'")
        else:
            print(f"'{book.title}' is not available for borrowing.")  

def return_book(self, book, library):
    if book in self.borrowed_books:
        library.return_book(self, book)
        self.borrowed_books.remove(book)
        print(f"{self.name} has returned '{book.title}'.")                        
    else:
        print(f"{self.name} did not borrow '{book.title}'")



class library:
    def __init__(self):
        self.book = []
        self.borrowed_books = {}

    def add_book(self, book):
        self.book.append(book)
        print(f"Added '{book.title}' to the library.")

    def display_available_books(self):
        available_books = [book for book in self.book if not book.is_borrowed]
        if available_books:
            print("Available books in liabary:")
            for book in available_books:
                print(book) 
            else:
                print("No books are currently avilable.")


    def borrow_books(self, student, book):
        if book in self.book and not book.is_borrowed:
            book.is_borrowed = True
            self.borrowed_books[book] = student
            return True
        return False
    
    def return_book(self, student, book):
        if book in self.borrowed_books and self.borrowed_books[book] == student:
            book.is_borrowed = False
            del self.borrow_books[book]
            return True
        return False
    
    def display_borrowed_books(self):
        if self.borrow_books:
            print("Books currently borrwed:")
            for book, student in self.borrowed_books.items():
                print(f"'{book.title}' borrowed by {student.name}")
            else:
                print("No books are currently borrowed.")