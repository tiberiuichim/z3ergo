"""
The addremove widget implementation
"""
from learningjourney.widget.addremove.interfaces import IAddRemoveInputWidget
from zope.app.form.browser.widget import SimpleInputWidget, renderTag
from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile
from zope.interface import implements
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary

class AddRemoveInputWidget(SimpleInputWidget):
    """A multiple choice string input widget with the option to add choices"""
    implements(IAddRemoveInputWidget)

    template = ViewPageTemplateFile('widget.pt')
    _missing = []
    
    def __call__(self):
        return self.template()
    
    def _getFormInput(self):
        """Extracts the input value from the submited form. This typically 
        just accesses the right form field from the request - WCDwZ3"""
        value = self.request.form.get(self.name, [])
        if not isinstance(value, list):
            value = [value]
        return value
    
    def hasInput(self):
        """Was this widget present in the form?"""
        if ("%s.marker" % self.name) in self.request.form.keys():
            return True
        else:
            return False
    
    def hidden(self):
        """Returns the widget rendered as hidden field"""
        widgets = ""
        for v in self._data:
            widgets += renderTag("input", type="hidden", 
                                          name=self.name, 
                                          value=v
                             )
        return widgets
    
    def choices(self):
        return self.context.vocabulary
    
    def _toFormValue(self, value):
        """Converts a field value to a string used as an HTML form value.

        This method is used in the default rendering of widgets that can
        represent their values in a single HTML form value. Widgets whose
        fields have more complex data structures should disregard this
        method and override the default rendering method (__call__).
        """
        if value == self.context.missing_value:
            return self._missing
        else:
            terms = []
            for v in value:
                term = SimpleTerm(v, v)
                terms.append(term)
            vocab = SimpleVocabulary(terms)
            return vocab