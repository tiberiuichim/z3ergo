from zope.interface import Interface, implements
from persistent import Persistent
from zope.size.interfaces import ISized
from zope.publisher.interfaces.http import IHTTPApplicationResponse
from zope.traversing.interfaces import IPhysicallyLocatable
from zope.traversing.api import getParent, getName
from zope.app.container.interfaces import IWriteContainer

from zope.copypastemove import IContainerItemRenamer

class IBook(Interface):
    "A marker interface for a Book"
    pass

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
	IHTTPApplicationResponse (self.request.response).redirect ("../..")

    def rename(self):
	IContainerItemRenamer(getParent(self.context)).renameItem (getName(self.context), self.request['new_name'])
	IHTTPApplicationResponse (self.request.response).redirect ("../..")
	
    def deleteBook(self):
	parent = getParent (self.context)
	name = getName (self.context)
	del(parent[name])
    	IHTTPApplicationResponse (self.request.response).redirect ("../..")

    def getId (self):
	return IPhysicallyLocatable(self.context).getName()
	
class myContainer(object):
    implements(IWriteContainer)
    def __delitem__ (self, name):
	import pdb; pbd_settrace()

    def __setitem__ (self, name, value):
	pass
	
	
class mySize(object):
    implements (ISized)
    def __init__ (self, container):
	self.container = container

    def sizeForSorting (self):
	return ('ZZZZ', len(self.container))

    def sizeForDisplay (self):
	ni = len (self.container)
	if ni == 1:
	    return ('1 ZZZZ')
	return (str(ni)+' ZZZZZ')