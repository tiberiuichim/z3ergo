from zope.interface import Interface, implements

from zope.formlib.form import EditForm, Fields, AddForm, applyChanges
from zope3tutorial.stage22.interfaces import IBook
from zope.component import createObject

from zope.traversing.browser.absoluteurl import absoluteURL

class BookEditForm(EditForm):
    form_fields = Fields(IBook)

class BookAddForm(AddForm):
    form_fields = Fields(IBook)

    def create(self, data):
        book = createObject(u'tutorial.Book')
        applyChanges(book, self.form_fields, data)
        return book
