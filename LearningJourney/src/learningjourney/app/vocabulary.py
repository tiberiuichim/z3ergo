from zope.component import getUtility
from zope.app.catalog.interfaces import ICatalog
from zope.schema.vocabulary import SimpleVocabulary

def getTagsVocabulary(context):
    catalog = getUtility(ICatalog)
    index = catalog['tags']
    keys = list(index._fwd_index)
    return SimpleVocabulary.fromValues(keys)