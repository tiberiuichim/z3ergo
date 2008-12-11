from zope.app.rotterdam import Rotterdam
from zope.publisher.interfaces.browser import IBrowserRequest

class IMySkinLayer(IBrowserRequest):
    """ A layer for MySkin """

class IMySkin(IMySkinLayer, Rotterdam):
    """ Class inheriting the rotterdam layers and mylayer """
'''