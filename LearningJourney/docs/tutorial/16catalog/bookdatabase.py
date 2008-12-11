from zope.interface import implements
from interfaces import IBookDatabase

from zope.app.container.btree import BTreeContainer
#from zope.app.container.contained import NameChooser
#from zope.exceptions.interfaces import UserError

from zope.i18nmessageid import MessageFactory
_ = MessageFactory('zope3tutorial')

class BookDatabase(BTreeContainer):
    implements(IBookDatabase)