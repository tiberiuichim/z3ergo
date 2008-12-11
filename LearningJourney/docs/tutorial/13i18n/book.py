from zope.interface import implements
from persistent import Persistent
from zope.size.interfaces import ISized
from zope.dublincore.interfaces import IZopeDublinCore
from zope.dublincore.annotatableadapter import partialAnnotatableAdapterFactory
from interfaces import IBook
from zope.component.factory import Factory

from zope.i18n import MessageFactory
_ = MessageFactory('zope3tutorial')

class Book(Persistent):
    title=u""
    author=u""
    publisher=u""


class BookSize(object):
    """Really dummy implementation of the ISized Interface for books"""
    implements(ISized)
    __used_for__ = IBook
    def __init__(self, context):
        self.context=context

    def sizeForDisplay(self):
        c  = self.context
        msg = _("${nr} chars", mapping= {'nr': len(c.title + c.author + c.publisher)})
	
        return msg

    def sizeForSorting(self):
        c  = self.context
        return len(c.title + c.author + c.publisher)

def BookDCImplementation(context):
    """this returns an adapter class. The component """
    map = {'title':'title',}
    adapter = partialAnnotatableAdapterFactory(map)(context)
    #import pdb; pdb.set_trace()
    return adapter


BookFactory = Factory(Book)
