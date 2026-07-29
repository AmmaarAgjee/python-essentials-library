#Library Management System
#Ammaar Agjee

#Returns (total_copies, copies_available) across the whole library as a tuple 

def library_totals(books):
    total_copies = 0
    copies_available = 0

    for book in books.values():
        total_copies += book["total"]
        copies_available += book["available"]

    return (total_copies, copies_available)

#Returns the book ID of the most-borrowed book, or none if no books
def most_borrowed(books):
    if not books:
        return None

    most_borrowed_book_id = None
    highest = -1

    for book_id, book in books.items():
        if book["times_borrowed"] > highest:
            highest = book["times_borrowed"]
            most_borrowed_book_id = book_id

    return most_borrowed_book_id

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
            print("invalid integer. Please enter a whole number.")

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
    global next_member_number
    print("\n--- register member ---")

    name = input("Enter member name: ")

    if name =="":
        print("Member name cannot be empty.")
        return

    member_id = "M" + str(next_member_number)
    members[member_id] = {
        "name": name,
        "borrowed_books": []
    }

    print(f"registered {member_id}: {name}")

    next_member_number += 1

#One member borrows one book - enforces ALL rules, updates BOTH dicts
def borrowed_books(books, members):
    print("\n--- borrow book ---")

    member_id = input("Enter member ID: ")
    book_id = input("Enter book ID: ")

    if member_id not in members:
        print("Member ID not found.")
        return
    
    if book_id not in books:
        print("Book not found.")
        return
    
    if books [book_id]["available"] <= 0:
        print("No copies available.")
        return

    if book_id in members[member_id]["borrowed_books"]:
        print("Member has already borrowed this book.")
        return

    members[member_id]["borrowed_books"].append(book_id)
    books[book_id]["available"] -= 1
    print(f"{members[member_id]['name']} borrowed {books[book_id]['title']}")

#One member returns one book - updates BOTH dicts
def return_book(books, members):
    print("\n--- return book ---")

    member_id = input("Enter member ID: ")
    book_id = input("Enter book ID: ")

    if member_id not in members:
        print("Member ID not found.")
        return

    if book_id not in books:
        print("Book not found.")
        return

    if book_id not in members[member_id]["borrowed_books"]:
        print("Member has not borrowed this book.")
        return

    members[member_id]["borrowed_books"].remove(book_id)
    books[book_id]["available"] += 1
    books[book_id]["times_borrowed"] -= 1
    print(f"{members[member_id]['name']} returned {books[book_id]['title']}")

#Case-insensitive keyword search over titles 
def search_catalogue(books):
    print("\n--- search catalogue ---")
    keyword = input("Enter search keyword: ")
    keyword_lower = keyword.lower()
    found = False
    for book_id, book in books.items():
        if keyword_lower in book["title"].lower():
            print(f"{book_id}: {book['title']} by {book['author']} ({book['available']}/{book['total']} available)")
            found = True
    
    if not found:
        print(f"No books found containing '{keyword}'.")

#Prints one member with the TITLES of their borrowed books
def member_summary(members, books):
    print("\n--- member summary ---")

    member_id = input("Enter member ID: ")

    if member_id not in members:
        print("Member ID not found.")
        return

    print(f"{member_id}: {members[member_id]['name']}")

    if not members[member_id]["borrowed_books"]:
        print("No borrowed books.")
        return

    print("Borrowed books:")
    for book_id in members[member_id]["borrowed_books"]:
        print(f"- {book_id}: {books[book_id]['title']}")

#Prints the whole-library report
def library_report(books, members):
    print("\n--- library report ---")
    total_copies, copies_available = library_totals(books)
    print(f"Total copies: {total_copies}")
    print(f"Available copies: {copies_available}")
    print(f"Total members: {len(members)}")

    most_borrowed_book_id = most_borrowed(books)
    if most_borrowed_book_id is None:
        print("Most borrowed book: None")
    else:
        most_borrowed_book = books[most_borrowed_book_id]
        print(f"Most borrowed book: {most_borrowed_book_id}: {most_borrowed_book['title']} by {most_borrowed_book['author']} ({most_borrowed_book['times_borrowed']} times)")

#---- Main Program ----

books = {}
members = {}

next_book_number = 1
next_member_number = 1

while True:
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Register Member")
    print("3. Borrow Books")
    print("4. Return Books")
    print("5. Search Catalogue")
    print("6. Member Summary")
    print("7. Library Report")
    print("8. Exit")

    choice = input("choose an option (1-8): ")

    if choice == "1":
        add_book(books)

    elif choice == "2":
        register_member(members)

    elif choice == "3":
       borrowed_books(books, members)

    elif choice == "4":
        return_book(books, members)

    elif choice == "5":
        search_catalogue(books)

    elif choice == "6":
        member_summary(members, books)

    elif choice == "7":
        library_report(books, members)

    elif choice == "8":
        print("Goodbye!")
        break

    else:
        print("I'm sorry, that option is not implemented. Please choose another option.")



