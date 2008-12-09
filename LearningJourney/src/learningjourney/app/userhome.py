from learningjourney.app.interfaces import ILearningEntry, IUserHome, \
    IPortalContent
from persistent import Persistent
from zope.app.container.btree import BTreeContainer
from zope.interface import implements
from zope.schema.fieldproperty import FieldProperty
from zope.component import adapts


class UserHome(BTreeContainer):
    implements(IUserHome)
    __doc__ = IUserHome.__doc__
    

class UserHomeMetadata(object):
    adapts(IUserHome)
    implements(IPortalContent)
    
    def __init__(self, context):
        self.context = context
        
    @property
    def name(self):
        return self.context.__name__


class LearningEntry(Persistent):
    implements(ILearningEntry)
    __doc__ = ILearningEntry.__doc__
    
    text = FieldProperty(ILearningEntry['text'])
    tags = FieldProperty(ILearningEntry['tags'])
    
    def getSearchableText(self):
        return self.text