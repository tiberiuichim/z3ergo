from zope.interface import Interface

class IFortuneTeller(Interface):
    """ singleton to get a fortune """
    def getFortune():
        """ returns a fortune """


from zope.viewlet.interfaces import IViewletManager
class IExtraStuffBox(IViewletManager):
    '''Viewlets for the extra stuff box'''
