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
    while True:
        try:
            copies = int(input("enter number of copies: "))   

            if copies > 0:
                return copies
            else:
                print("please enter a number greater than 0.")
        except ValueError:
            print("Valid integer. Please enter a whole number.")

#Adds a new book or adds copies to an existing title by the same author
def add_book(books):
    global next_book_number
    print("\n--- add book ---")
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    copies = read_valid_copies()

    if title == "" or author == "":
        print("Title and author cannot be empty.")
        return

    # check for existing book by same title and author (case-insensitive)
    for book_id, book in books.items():
        if (book["title"].lower() == title.lower() and
            book["author"].lower() == author.lower()):
            book["total"] += copies
            book["available"] += copies
            print(f"added {copies} more copies of {book_id}: {title} (now {book['total']})")
            return

    # add new book
    book_id = "B" + str(next_book_number)
    books[book_id] = {
        "title": title,
        "author": author,
        "total": copies,
        "available": copies,
        "times_borrowed": 0
    }

    print(f"added {book_id}: {title} by {author} ({copies} copies)")
    next_book_number += 1

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

    if choice == "1":
        add_book(books)

    elif choice == "8":
        print("Goodbye!")
        break

    else:
        print("I'm sorry, that option is not implemented. Please choose another option.")

