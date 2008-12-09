from learningjourney.app.interfaces import ILearningJourneyApplication
from zope.app.folder.folder import Folder
from zope.interface import implements

class Application(Folder):
    implements(ILearningJourneyApplication)
    __doc__ = ILearningJourneyApplication.__doc__