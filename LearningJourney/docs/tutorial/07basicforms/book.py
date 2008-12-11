from zope.interface import Interface, implements
from persistent import Persistent
from zope.size.interfaces import ISized
from zope.schema import TextLine

class IBook(Interface):
    "A marker interface for a Book"
    title = TextLine(title=u"The title")
    author = TextLine(title=u"The author")
    publisher = TextLine(title=u"The publisher")

class Book(Persistent):
    title=""
    author=""
    publisher=""

class BookSize(object):
    """Really dummy implementation of the ISized Interface for books"""
    implements(ISized)
    __used_for__ = IBook
    def __init__(self, context):
        self.context=context

    def sizeForDisplay(self):
        c  = self.context
        return "%s chars" % len(c.title + c.author + c.publisher)

    def sizeForSorting(self):
        c  = self.context
        return len(c.title + c.author + c.publisher)

class BookViews:

    def showBookInfo(self):
        rez = "Title: %s, Author: %s, Publisher: %s" % (
            self.context.title,
            self.context.author,
            self.context.publisher)
        return rez

    def getBookInfo(self):
        c = self.context
        res = {'title':c.title, 'author':c.author, 'publisher':c.publisher}
        return res

    def changeBook(self):
        c = self.context
        req = self.request
        (c.title, c.author, c.publisher) = (req['title'], req['author'], req['publisher'])
        return "Book changed"