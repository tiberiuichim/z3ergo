from zope.app.rotterdam import Rotterdam
from zope.publisher.interfaces.browser import IBrowserRequest

class IMySkinLayer(IBrowserRequest):
    """ A layer for MySkin """

class IMySkin(IMySkinLayer, Rotterdam):
    """ Class inheriting the rotterdam layers and mylayer """

#a basic skin declaration would look like:
'''
class rotterdam(IBrowserRequest):
    """Layer for registering Rotterdam-specific macros."""

class Rotterdam(rotterdam, IDefaultBrowserLayer):
    """The ``Rotterdam`` skin.

    It is available via ``++skin++Rotterdam``.
    """
'''