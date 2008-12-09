from learningjourney.app.util import get_site_url
from learningjourney.ui.registration.interfaces import IRegistrationSchema
from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile
from zope.component import getUtility
from zope.formlib.form import PageForm, action, Fields
from zope.publisher.browser import BrowserPage
from learningjourney.app.interfaces import IRegistrations


class RegistrationPage(PageForm):
    
    form_fields = Fields(IRegistrationSchema)
    _registration_done = False
    
    def nextUrl(self):
        return ("%s/@@index.html?status_message=You were registered. "
                "Please check your email" % get_site_url(self.request))

    @action(label=u"Register")
    def register(self, action, data):
        registrations = getUtility(IRegistrations)
        registrations.register(data['email'], data)
        self._registration_done = True
        
    def __call__(self):
        self.update()
        if self._registration_done:
            self.request.response.redirect(self.nextUrl())
            return ""
        return self.render()
        
        
class ConfirmationPage(BrowserPage):
    """Confirm a user's registration."""

    template = ViewPageTemplateFile('pt/confirmation_success.pt')
    error_template = ViewPageTemplateFile('pt/confirmation_error.pt')

    def __call__(self):
        registrations = getUtility(IRegistrations)
        hash = self.request.form.get('hash')
        try:
            self.reginfo = registrations[hash]
            registrations.confirm(hash)
        except KeyError:
            return self.error_template()
        return self.template()