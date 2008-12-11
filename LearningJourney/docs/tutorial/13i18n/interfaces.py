from zope.interface import Interface
from zope.schema import TextLine

from zope.i18n import MessageFactory
_ = MessageFactory('zope3tutorial')

class IBook(Interface):
    "A marker interface for a Book"
    title = TextLine(title=_("The title"))
    author = TextLine(title=_("The author"))
    publisher = TextLine(title=_("The publisher"))

class IRating(Interface):
    rating=TextLine(title=_("Rating"))

    def getRating():
        """Returns a rating"""

    def setRating(value):
        """Sets a rating"""

class IRatingViews(Interface):
    def show_rating():
        """returns the information about a rating"""

    def set_rating(value):
        """sets a rating value"""