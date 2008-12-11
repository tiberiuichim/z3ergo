from zope.interface import Interface

class IFortuneTeller(Interface):
    """ singleton to get a fortune """
    def getFortune():
        """ returns a fortune """