#Library Management System
#Ammaar Agjee

#Returns (total_copies, copies_available) across the whole library as a tuple 
def library_totals(books):
    pass

#Returns the book ID of the most-borrowed book, or none if no books
def most_borrowed(books):
    pass

#Asks for a number of copies, validates with try-except, returns int or none 
def read_valid_copies():
    pass    

#Adds a new book or adds copies to an existing title by the same author
def add_book(books):
    pass

#Register a new member with an empty borrowed list
def register_member(members):
    pass

#One member borrows one book - enforces ALL rules, updates BOTH dicts
def borrow_book(books, members):
    pass

#One member returns one book - updates BOTH dicts
def return_book(books, members):
    pass

#Case-insensitive keyword search over titles 
def search_catalogue(books):
    pass

#Prints one member with the TITLES of their borrowed books
def member_summary(members, books):
    pass

#Prints the whole-library report
def library_report(books, members):
    pass

#---- Main Program ----

books = {}
members = {}

next_book_number = 1
next_member_number = 1

while True:
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Register Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Search Catalogue")
    print("6. Member Summary")
    print("7. Library Report")
    print("8. Exit")

    choice = input("choose an option (1-8): ")

    if choice == "8":
        print("Goodbye!")
        break
    else:
        print("I'm sorry, that option is not implemented. Please choose another option.")

