from zope.interface import Interface

class IBook(Interface):
    "A marker interface for a Book"
    pass

class Book:
    title=u""
    author=u""
    publisher=u""

class BookCreation:

    def __call__(self):
        return self

    def __new_id(self):
        i = 0
        while True:
            if self.context.get(str(i), None) is not None:
                i+=1
                continue
            else:
                return str(i)

    def addBook(self, title, author, publisher):
        b = Book()
        b.title, b.author, b.publisher = title, author, publisher
        self.context[self.__new_id()] = b
        return "asta este"

    def getBooks(self):
        import pdb; pdb.set_trace()

class BookView:

    def showBookInfo(self):
        rez = "Title: %s, Author: %s, Publisher: %s" % (
            self.context.title,
            self.context.author,
            self.context.publisher)
        return rez
    def showBookInfo2(self):
        rez = "Title_: %s, Author_: %s, Publisher_: %s" % (
            self.context.title,
            self.context.author,
            self.context.publisher)
        return rez
