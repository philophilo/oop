from abc import ABCMeta, abstractmethod

class Validation(object):
    def add_data(self, instance, data):
        self.instance = instance
        self.data = data

    def valid_data(self):
        if self.not_empty():
            return isinstance(self.data, self.instance)

    def not_empty(self):
        if self.data is not "":
            return True
        return False


class Book(object):
    __metaclass__ = ABCMeta
    def __init__(self):
        self.count = 0
        self.books = {}

    def add_book(self, author, title, year, publisher):
        self.author = None
        self.title = None
        self.year = None
        self.publisher = None

        self.valid = Validation()
        self.valid.add_data(str, author)
        if self.valid.valid_data():
            self.author = author

        self.valid.add_data(str, title)
        if self.valid.valid_data():
            self.title = title

        self.valid.add_data(int, year)
        if self.valid.valid_data():
            self.year = year

        self.valid.add_data(str, publisher)
        if self.valid.valid_data():
            self.publisher = publisher

        self.set_book()


    def book_feature(self, key):
        return self.set_book[key]

    def set_book(self):
        self.count += 1
        self.books[self.count] = {"author":self.author,
                                    "title":self.title,
                                    "year":self.year,
                                    "publisher":self.publisher}
    def see_all_books(self):
        for key, values in self.books.items():
            print "book number =>", key
            for k, v in values.items():
                print "\t ", k, "-", v

    def book_type(self):
        pass


class Novel(Book):
    valid = Validation()
    def book_type(self):
        print "You are currently in novels"
        print "---------------------------"

    def review(self, text):
        Novel.valid.add_data(str, text)
        if Novel.valid.valid_data():
            self.books[self.count]["review"] = text
        else:
            print "The input is not valid"

class TextBook(Book):
    valid = Validation()
    def book_type(self):
        print "you are currently in text books"
        print "-------------------------------"

    def interest_area(self, text):
        TextBook.valid.add_data(str, text)
        if TextBook.valid.valid_data():
            self.books[self.count]["area"] = text
        else:
            print "The input is not valid"

if __name__ == "__main__":
    novels = Novel()
    novels.add_book("Barbara Kingsolver", "The poisonwood bible", 2005, "HarperPerennial")
    novels.book_type()
    novels.review("it was kawa")
    novels.see_all_books()

    tbooks = TextBook()
    tbooks.add_book("Alasdair Maclntyre", "A short history of ethics", 1996, "Macmillan")
    tbooks.book_type()
    tbooks.interest_area("History")

    tbooks.add_book("Roger Owen, Bob Sutcliffe", "Studies in the theory of imperialisam", "1980", "Longman")
    tbooks.interest_area("Political Science")

    tbooks.add_book("Steven Bird, Ewan Klein, and Edward Loper", "Natural Language Processing with Python", 2009, "O\'Reilly")
    tbooks.interest_area(1)
    tbooks.see_all_books()
