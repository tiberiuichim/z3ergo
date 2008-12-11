from zope.component import getUtility
from interfaces import IFortuneTeller
from zope.interface import Interface, implements
from zope.publisher.interfaces.browser import IBrowserRequest, IBrowserView
from zope.component import adapts
from zope.contentprovider.interfaces import IContentProvider

from zope.app.pagetemplate import ViewPageTemplateFile
import datetime

class FortuneView(object):
    def __call__(self):
        futil = getUtility(IFortuneTeller)
        return futil.getFortune()

class FortuneProvider(object):
    implements(IContentProvider)
    adapts(Interface, IBrowserRequest, IBrowserView)

    def __init__(self, context, request, view):
        self.context, self.request, self.view = context, request, view

    def update(self):
        pass

    #render = ViewPageTemplate('fortuneprovider.pt')
    def render(self):
        futil = getUtility(IFortuneTeller)
        return str(futil.getFortune())

from zope.formlib.form import EditForm, Fields
from interfaces import ILocalFortuneTeller
class EditFortuneTeller(EditForm):
    form_fields = Fields(ILocalFortuneTeller)

class DateProvider(object):
    implements(IContentProvider)
    adapts(Interface, IBrowserRequest, IBrowserView)

    def __init__(self, context, request, view):
        self.context, self.request, self.view = context, request, view

    def update(self):
        pass

    def _getDateTime(self):
        return str(datetime.datetime.now())

    render = ViewPageTemplateFile('dateprovider.pt')
