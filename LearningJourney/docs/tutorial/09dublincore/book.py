from zope.interface import Interface, implements
from persistent import Persistent
from zope.size.interfaces import ISized
from zope.schema import TextLine
from zope.dublincore.interfaces import IZopeDublinCore
#from zope.dublincore.zopedublincore import ZopeDublinCore
from zope.dublincore.annotatableadapter import partialAnnotatableAdapterFactory

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

def BookDCImplementation(context):
    """this returns an adapter class"""
    map = {'title':'title',}
    adapter = partialAnnotatableAdapterFactory(map)(context)
    #import pdb; pdb.set_trace()
    return adapter