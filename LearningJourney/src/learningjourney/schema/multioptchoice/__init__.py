from learningjourney.schema.multioptchoice.interfaces import \
    IMultiOptionalChoice
from zope.app.renderer.interfaces import ISource
from zope.interface import implements
from zope.schema import Field, List, Choice
from zope.schema.interfaces import IContextSourceBinder, IField


class MultiOptionalChoice(List, Choice):
    """A multioptional choice field that takes its values from a vocabulary and keeps 
    them in a list. 
    """
    implements(IMultiOptionalChoice)
    vocabulary = None    #inherit and overwrite this
    #__name__ = None
    
    def __init__(self, value_type, vocabulary, **kw):
        
        # complain if value_type is not a field
        if value_type is not None and not IField.providedBy(value_type):#IGNORE:E1101
            raise ValueError("'value_type' must be field instance.")
        self.value_type = value_type
        self.vocabulary = None
        self.vocabularyName = None

        if isinstance(vocabulary, (unicode, str)):
            self.vocabularyName = vocabulary
        else: 
            assert (ISource.providedBy(vocabulary) or             #IGNORE:E1101
                    IContextSourceBinder.providedBy(vocabulary))  #IGNORE:E1101
            self.vocabulary = vocabulary
        self._init_field = bool(self.vocabularyName)
        Field.__init__(self, **kw)      # initializing List or Choice would mess up 
                                        # the vocabulary 
        self._init_field = False
        
    def _validate(self, value):
        if self._init_field:
            return
        #value should be a list all the time, even if empty
        if not (isinstance(value, list)):
            raise ValueError("""The value for a MultiOptionalChoice should """
                             """be a list, got %s""" % type(value))
        
    #the rest of methods are handled very nicely by List