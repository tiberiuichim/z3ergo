from interfaces import IFortuneTeller
from zope.interface import implements

import os

class FortuneTeller(object):
    """Implements a fortune utility """

    implements(IFortuneTeller)
    fortune_path="/usr/games/fortune"

    def getFortune(self):
        ft_pipe = os.popen(self.fortune_path)
        fortune = ft_pipe.read()
        ft_pipe.close(); del(ft_pipe)
        return fortune

fortuneteller = FortuneTeller()