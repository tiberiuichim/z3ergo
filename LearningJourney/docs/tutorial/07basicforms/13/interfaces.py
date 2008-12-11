from zope.interface import Interface
from zope.schema import TextLine

class IBook(Interface):
    "A marker interface for a Book"
    title = TextLine(title=u"The title")
    author = TextLine(title=u"The author")
    publisher = TextLine(title=u"The publisher")

class IRating(Interface):
    rating=TextLine(title=u"Rating")

    def getRating():
        """Returns a rating"""

    def setRating(value):
        """Sets a rating"""

class IRatingViews(Interface):
    def show_rating():
        """returns the information about a rating"""

    def set_rating(value):
        """sets a rating value"""