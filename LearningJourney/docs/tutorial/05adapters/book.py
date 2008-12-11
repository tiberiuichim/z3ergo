from persistent import Persistent
from zope.index.text.interfaces import ISearchableText
from zope.interface import Interface, implements
from zope.size.interfaces import ISized

class IBook(Interface):
    "A marker interface for a Book"
    pass

class Book(Persistent):
    title = u""
    author = u""
    publisher = u""

class BookSize(object):
    """Really dummy implementation of the ISized Interface for books"""
    implements(ISized)
    __used_for__ = IBook
    def __init__(self, context):
        self.context = context

    def sizeForDisplay(self):
        c = self.context
        return "%s chars" % len(c.title + c.author + c.publisher)

    def sizeForSorting(self):
        c = self.context
        return len(c.title + c.author + c.publisher)

class SearchText(object):
    implements(ISearchableText)
    
    __used_for__ = IBook
    
    def __init__ (self, context):
	self.context = context
	
    def getSearchableText(self):
	c = self.context
	return (c.title.split(" ") + c.author.split(" ") + c.publisher.split(" "))

class BookCreation:

    def __call__(self):
        return self

    def __new_id(self):
        i = 0
        while True:
            if self.context.get(str(i), None) is not None:
                i += 1
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