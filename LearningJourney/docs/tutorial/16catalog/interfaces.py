from zope.interface import Interface
from zope.schema import TextLine, Field

from zope.app.container.interfaces import IContainer, IContained
from zope.app.container.constraints import ContainerTypesConstraint
from zope.app.container.constraints import ItemTypePrecondition

from zope.i18n import MessageFactory
_ = MessageFactory('zope3tutorial')

class IBook(Interface):
    "A marker interface for a Book"
    title = TextLine(title=_("The title"))
    author = TextLine(title=_("The author"))
    publisher = TextLine(title=_("The publisher"))


class IBookDatabase(IContainer):
    """A book database holds books"""

    def __setitem__():
        """ Add a book """

    __setitem__.precondition = ItemTypePrecondition(IBook)

class IBookContained(IContained):
    __parent__ = Field(
            constraint = ContainerTypesConstraint(IBookDatabase)
        )

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