from learningjourney.app.interfaces import ILearningEntry
from learningjourney.app.userhome import LearningEntry
from learningjourney.app.util import get_homefolder, get_site_url
from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile
from zope.app.security.interfaces import IUnauthenticatedPrincipal
from zope.formlib.form import Fields, PageAddForm, PageEditForm, applyChanges
from zope.publisher.browser import BrowserPage
from zope.traversing.browser.absoluteurl import absoluteURL
from zope.app.container.interfaces import INameChooser
from zope.security.management import checkPermission
from learningjourney.ui.homefolder.mixin import EntryDetailMixin


class DashboardRedirect(object):
    def __call__(self):
        if not IUnauthenticatedPrincipal.providedBy(self.request.principal):
            home_url = absoluteURL(get_homefolder(self.request.principal), self.request)
            self.request.response.redirect("%s/@@index.html" % home_url)
        else:
            self.request.response.redirect("%s/@@loginForm.html" % get_site_url())
            return ""
        
        
class Dashboard(BrowserPage):
    template = ViewPageTemplateFile('pt/dashboard.pt')
    
    def can_add_entry(self):
        return checkPermission('lj.AddLearningEntry', self.context)
    
    def __call__(self):
        return self.template()
    
    
class EntryAddPage(PageAddForm):
    form_fields = Fields(ILearningEntry)
    
    def create(self, data):
        ob = LearningEntry()
        applyChanges(ob, self.form_fields, data)
        return ob
    
    def add(self, obj):
        name = INameChooser(self.context).chooseName("Entry", obj)
        self.context[name] = obj
        self._finished_add = True
        return obj
    
    def nextURL(self):
        return "./@@index.html"
    
    
class EntryEditPage(PageEditForm):
    form_fields = Fields(ILearningEntry)
    
    
class EntryViewPage(BrowserPage, EntryDetailMixin):
    template = ViewPageTemplateFile('pt/entry.pt')
    
    def __call__(self):
        return self.template()
    
    
class EntryDeletePage(object):
    def __call__(self):
        name = self.request.form.get('name')
        del self.context[name]
        self.request.response.redirect('./@@index.html')
        return ""