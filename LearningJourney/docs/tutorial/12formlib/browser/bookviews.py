from zope.interface import Interface, implements

from zope.formlib.form import EditForm, Fields, AddForm, applyChanges, setUpWidgets
from zope3tutorial.stage18.interfaces import IBook
from zope.component import createObject

class BookEditForm (EditForm):
    form_fields = Fields (IBook)

#    def setUpWidgets(self, ignore_request = False):
#	self.widgets  = setUpWidgets(self.form_fields, self.prefix, self.context, self.request, ignore_request = ignore_request)
#	import pdb; pdb.set_trace()
	

#    form_fields = form_fields.omit ('title')
#    form_fields['title'].field.read_only = True
    
class BookAddForm (AddForm):
    form_fields = Fields (IBook)
    
    def create(self, data):
	book = createObject (u'tutorial.Book')
	applyChanges(book, self.form_fields, data)
	return book