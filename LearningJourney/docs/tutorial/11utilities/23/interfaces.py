from zope.interface import Interface
from zope.schema import TextLine
from zope.viewlet.interfaces import IViewletManager
from zope.i18n import MessageFactory
_ = MessageFactory('zope3tutorial')

class ILocalFortuneTeller(Interface):
    fortune_path = TextLine(
        title=_(u"Path to fortune binary"),
        description=_(u"Point to a disk location"),
        )

class IFortuneTeller(Interface):
    """ singleton to get a fortune """

    def getFortune():
        """ returns a fortune """

class IExtraStuffBox(IViewletManager):
    '''Viewlets for the extra stuff box'''
