from Book import Book


class Library:
    def __init__(self):
        self.books = []

    def addBook(self, newBook):
        for book in self.books:
            if book.name == newBook.name:
                return False
        self.books.append(newBook)
        return True

    def removeBook(self, deleted_book_name):
        for book in self.books:
            if deleted_book_name == book.name:
                self.books.remove(book)
                return True
        return False

    def borrowbook(self, borrowed_book_name):
        for book in self.books:
            if borrowed_book_name == book.name:
                if book.availability == True:
                    book.availability = False
                    return True
                else:
                    return False
        return False

    def bringbook(self, borrowed_book_name):
        for book in self.books:
            if borrowed_book_name == book.name:
                if book.availability == False:
                    book.availability = True
                    return True
                else:
                    return False
        return False

    def getList(self):
        str = ''
        for book in self.books:
            str = str + book.name + ","
        return str.removesuffix(',')

    def __str__(self):
        return 'Number Of Books\t:\t{}\n' \
               'Books\t:\t{}'.format(len(self.books), self.getList())


if __name__ == '__main__':
    test_book = Book('Bülbülü Öldürmek', 1960, 357, 'Harper Lee')
    test_book2 = Book('Aşk-ı Memnu', 1968, 856, 'Halit Ziya Uşaklıgil')

    test_library = Library()
    print(test_library)

    result = test_library.addBook(test_book)
    print(result)
    print(test_library)

    result = test_library.addBook(test_book)
    print(result)
    print(test_library)

    result = test_library.addBook(test_book2)
    print(result)
    print(test_library)

    result = test_library.removeBook('Bülbülü Öldürmek')
    print(result)
    print(test_library)

    result = test_library.removeBook('Bülbülü Öldürmek')
    print(result)
    print(test_library)

    result = test_library.borrowbook("Aşk-ı Memnu")
    print(result)
    print(test_library)

    result = test_library.borrowbook("Aşk-ı Memnu")
    print(result)
    print(test_library)

    result = test_library.bringbook("Aşk-ı Memnu")
    print(result)
    print(test_library)

    result = test_library.bringbook("Aşk-ı Memnu")
    print(result)
    print(test_library)
