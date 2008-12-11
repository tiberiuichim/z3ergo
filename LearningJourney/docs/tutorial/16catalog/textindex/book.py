from zope.index.text.interfaces import ISearchableText
from zope.interface import implements

class BookSearchableText(object):
    implements(ISearchableText)

    def __init__(self, book):
        self.book = book

    def getSearchableText(self):
        return [self.book.title, self.book.author, self.book.publisher]