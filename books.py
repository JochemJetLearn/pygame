books = {
    "physics book": {
        "author": "Dr. Darshan Asad",
        "stock": 12,
        "price": 250
    },
    "another one": {
        "author": "Dr. Me",
        "stock": 12,
        "price": 300
    },
    "new book": {
        "author": "Dr. Darshan Asad",
        "stock": 12,
        "price": 150
    },
    "wow": {
        "author": "Dr. Me",
        "stock": 12,
        "price": 500
    }
}

def editor(book, name="new book"):
    print(f"Opening editor for book: {name}")
    while True:
        print("\nChoose an option to add/edit:\n 0. Show book info\n 1. Author\n 2. Price\n 3. Stock\n 4. Exit editor")
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            author = input("\nEnter author name: ")
            book["author"] = author
        elif choice == "2":
            try:
                price = int(input("\nEnter book price: "))
                book["price"] = price
            except ValueError:
                print("Invalid price")
        elif choice == "3":
            try:
                stock = int(input("\nEnter book stock: "))
                book["stock"] = stock
            except ValueError:
                print("Invalid stock")
        elif choice == "0":
            print(f"\nName: {name}, Author: {book["author"]}, Price: {book["price"]}, Stock: {book["stock"]}")
        elif choice == "4":
            break

while True:
    print("\nChoose an opion:\n 1. Show all books info\n 2. Get book info\n 3. Edit book\n 4. Buy book\n 5. Add book\n 6. Delete book\n 7. Edit stock\n 8. Exit")
    choice = input("Enter your choice (1-7): ")
    if choice == "1":
        print(f"\n All books ({len(books)}):")
        for i in books:
            print(f"\nBook: {i}, Author: {books[i]['author']}, Price: {books[i]['price']}, Stock: {books[i]['stock']}")
    elif choice == "2":
        book_name = input("\nEnter book name: ")
        if book_name in books:
            print(f"\nBook: {book_name}, Author: {books[book_name]['author']}, Price: {books[book_name]['price']}, Stock: {books[book_name]['stock']}")
        else:
            print("No book found")
    elif choice == "3":
        name = input("\nEnter book to edit: ")
        if name in books:
            editor(books[name], name)
        else:
            print("No book found")
    elif choice == "4":
        name = input("\nEnter book to buy: ")
        if name in books:
            if books[name]["stock"] <= 0:
                print("Book cannot be bought: out of stock")
            else:
                books[name]["stock"] -= 1
                if books[name]["stock"] <= 0:
                    print("Book is bought out of stock: no stock left")
                else:
                    print(f"Book bought successfully, remaining stock: {books[name]['stock']}")
        else:
            print("No book found")
    elif choice == "5":
        name = input("\nEnter book to add: ")
        if not (name in books):
            books[name] = {"author": "Unknown", "stock": 0, "price": 0}
            editor(books[name], name)
        else:
            print("Book already exists: use 3. Edit book option")
    elif choice == "6":
        name = input("\nEnter book to delete: ")
        if name in books:
            del books[name]
            print("Book deleted.")
        else:
            print("No book found")
    elif choice == "7":
        name = input("\nEnter book to change stock: ")
        if name in books:
            while True:
                try:
                    books[name]["stock"] = int(input(f"old stock: {books[name]["stock"]}. Enter new stock: "))
                    break
                except ValueError:
                    print("Only numbers please.")
        else:
            print(f"Book {name} does not exist.")
    elif choice == "8":
        break