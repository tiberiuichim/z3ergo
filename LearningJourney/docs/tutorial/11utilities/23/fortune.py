import os
from zope.interface import implements
from zope.app.container.contained import Contained
from persistent import Persistent

from interfaces import IFortuneTeller, ILocalFortuneTeller

class LocalFortuneTeller(Persistent, Contained):
    """Implements a local fortune utility """

    implements(IFortuneTeller, ILocalFortuneTeller)
    fortune_path="/usr/games/fortune"

    def getFortune(self):
        ft_pipe = os.popen(self.fortune_path)
        fortune = ft_pipe.read()
        ft_pipe.close(); del(ft_pipe)
        return fortune

class GlobalFortuneTeller(LocalFortuneTeller):
    pass
fortuneteller = GlobalFortuneTeller()