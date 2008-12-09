from zope.app.catalog.interfaces import ICatalog
from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile
from zope.component import getUtility
from zope.publisher.browser import BrowserPage


class ExplorePage(BrowserPage):
    template = ViewPageTemplateFile('pt/explore.pt')
    
    def __init__(self, context, request):
        super(ExplorePage, self).__init__(context, request)
        self.catalog = getUtility(ICatalog)
    
    def __call__(self):
        return self.template()
    
    def tags(self):
        index = self.catalog['tags']
        return sorted(index._fwd_index)
    
    def get_entries(self, tag):
        results = self.catalog.searchResults(tags=[tag])
        return results