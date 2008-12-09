from learningjourney.ui.homefolder.mixin import EntryDetailMixin
from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile
from zope.publisher.browser import BrowserView


class EntryDetail(BrowserView, EntryDetailMixin):
    template = ViewPageTemplateFile('pt/entry_detail.pt')
    
    def __call__(self):
        return self.template()
    

class EntryFullDetail(BrowserView, EntryDetailMixin):
    template = ViewPageTemplateFile('pt/entry_full_detail.pt')
    
    def __call__(self):
        return self.template()
    
    
class EntryAdmin(BrowserView, EntryDetailMixin):
    template = ViewPageTemplateFile('pt/entry_admin.pt')
    
    def __call__(self):
        return self.template()