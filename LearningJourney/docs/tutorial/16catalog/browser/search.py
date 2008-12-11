from zope.app.catalog.interfaces import ICatalog
from zope.component import getUtility
from zope.dublincore.interfaces import IZopeDublinCore

class SearchResults(object):
    def getResults(self):
        query=self.request.get('query', '')
        catalog = getUtility(ICatalog)
        results = catalog.searchResults(TextIndex=query)
        #import pdb; pdb.set_trace()
        return results

    def getObjectModified(self, obj):
        dc = IZopeDublinCore(obj)
        #return dc.ModificationDate()
        return dc.modified