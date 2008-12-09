from zope.app.catalog.interfaces import ICatalog
from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile
from zope.component import getUtility
from zope.publisher.browser import BrowserPage
from zope.app.security.interfaces import IUnauthenticatedPrincipal
from learningjourney.app.util import get_homefolder


class SearchPage(BrowserPage):
    template = ViewPageTemplateFile('pt/search.pt')
    
    def __call__(self):
        return self.template()
    
    def results(self):
        s = self.request.form.get('s', '')
        catalog = getUtility(ICatalog)
        query = {
                 'searchableText':s,
                 }
        if 'owned' in self.request.form:
            if not IUnauthenticatedPrincipal.providedBy(self.request.principal):
                hf = get_homefolder(self.request.principal)
                query['name'] = hf.__name__
                
        res = catalog.searchResults(**query)
        return res