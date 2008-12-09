from learningjourney.app.util import get_site_url
from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile
from zope.app.security.interfaces import IUnauthenticatedPrincipal, \
    IAuthentication
from zope.component import getUtility
from zope.publisher.browser import BrowserPage


class LoginPage(BrowserPage):
    template = ViewPageTemplateFile('pt/login.pt')
    
    def __call__(self):
        if not IUnauthenticatedPrincipal.providedBy(self.request.principal):
            url = '%s/@@index.html'
            self.request.response.redirect(url % get_site_url())
            return ""
        return self.template()
    
    
class LogoutPage(BrowserPage):
    
    def __call__(self):
        getUtility(IAuthentication).logout(self.request)
        site_url = get_site_url(self.request)
        self.request.response.redirect("%s/@@index.html" % site_url)
        return ""