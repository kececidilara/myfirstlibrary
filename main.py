from Library import Library
from Book import Book

library = Library()
test_book = Book('Bülbülü Öldürmek', 1960, 357, 'Harper Lee')
test_book2 = Book('Aşk-ı Memnu', 1968, 856, 'Halit Ziya Uşaklıgil')
library.addBook(test_book)
library.addBook(test_book2)

print('Hello Reader!')
questions = "1: If you want to add a new book:\n" \
            "2: If you want to remove a book:\n" \
            "3: If you want to borrow a new book: \n" \
            "4: If you want to bring your old book:\n" \
            "5: If you want to see our library book list:\n" \
            "6: If you want to quit:"
isQuit = False

while not isQuit:
    print(questions)
    selection = input("Please select a number from above: ")
    if int(selection) == 1:
        name = input("Please write your new book's name: ")
        year = input("Please write your new book's publish year: ")
        n_page = input("Please write your new book's number of page: ")
        author = input("Please write your new book's author: ")
        new_book = Book(name, year, n_page, author)
        result = library.addBook(new_book)
        if result:
            print("Thanks for your addition")
        else:
            print("This book is already in our library")
    elif int(selection) == 2:
        name = input("Please write your book's name: ")
        result = library.removeBook(name)
        if result:
            print("Successfully Removed")
        else:
            print('This book is not found')
    elif int(selection) == 3:
        print(library)
        name = input("Please write your requested book's name: ")
        result = library.borrowbook(name)
        if result:
            print('Have nice readings')
        else:
            print('Sorry, this book is already taken')
    elif int(selection) == 4:
        name = input("Please write your book name: ")
        result = library.bringbook(name)
        if result:
            print('Thanks, successfully received')
        else:
            print('Where did you find this book?')
    elif int(selection) == 5:
        print(library)
    elif int(selection) == 6:
        print("Have a nice day :)\n")
        isQuit = True
