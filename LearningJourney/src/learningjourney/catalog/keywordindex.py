from learningjourney.catalog.interfaces import IKeywordIndex
from zope.app.catalog.attribute import AttributeIndex
from zope.app.container.contained import Contained
from zope.index.keyword.index import KeywordIndex as BaseKeywordIndex
from zope.interface.declarations import implements

class KeywordIndex(AttributeIndex, BaseKeywordIndex, Contained):
    implements(IKeywordIndex)
    
    def apply(self, *args, **kwds):
        return self.search(*args, **kwds)