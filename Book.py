class Book:
    def __init__(self, name, year, n_page, author):
        self.name = name
        self.year = year
        self.n_page = n_page
        self.author = author
        self.availability = True

    def __str__(self):
        return 'Name\t:\t{}\nAuthor\t:\t{}\nYear\t:\t{}\nPages\t:\t{}\nAvail\t:\t{}'.format(self.name,
                                                                                                   self.author,
                                                                                                   self.year,
                                                                                                   self.n_page,
                                                                                                   self.availability)

    def setAvailability(self, availability):
        self.availability = availability


if __name__ == '__main__':
    test_book = Book('Bülbülü Öldürmek', 1960, 357, 'Harper Lee')
    print(test_book)
    test_book.setAvailability(False)
    print(test_book)