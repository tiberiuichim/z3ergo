Basic formlib
---------------

* NOTE: need to change ratingviews to contain the path to the proper interface
* Manually implemented a content factory for Book (needed for createObject, but
  this can be automatically created from the <class><factory /></class> configuration
* in the `browser` package, changed the add and edit views to use their formlib counterparts
* created the formlib classes necessary for the add/edit views (in browser/bookviews.py)

Extra documentation
---------------------
read zope/formlib/form.txt


Formlib is a general toolkit and API for doing intelligent web form development in Python. It's not a widget library - most of those are provided by the widgets in zope.app.form.browser, but could come from anywhere. It's not a validation framework - that's provided by zope.schema based fields (which work with Zope Interfaces). It does use both of those, and provides a lot of extra features to collect all of the input, apply the validation or collect errors, do invariant based validation ('end date must be later than start date'), dispatch to different responsive actions, and more.

It's a toolkit capable of building powerful base classes and individual uses for forms that are simple (just a few fields) or very complex. There were some form views provided in Zope 3.0 and 3.1 that do similar, but they weren't so easy to use and understand and didn't handle complex forms. Custom field and widget combinations required a lot of custom work, and so did dispatching to multiple actions based on success, failure, and so on. Lastly, the older (non-formlib) techniques seemed to prefer being built via the Zope 3 component configuration language when it really required Python to get the kind of flexibility that form development requires.

In wrap-up, formlib is promising because it shows a preference for using Python and some of the recent features such as decorators over giving everything over to configuration based automation. Content Providers are a simple specification for modularizing web pages into manageable components, with viewlets and viewlet managers providing a reasonable base implementation to work with. The dual layers provide a boundary between a basic spec and small set of tools (the content provider interface, a TALES expression for use in zope page templates) that have broad usage and more specialized providers, built from real-world usage and previous art and examples like JSR 168.


applyChanges explained
----------------------------

Marius Gedminas shows us how to create a simple add form for Zope3 using formlib, but he then assumes the object in question accepts keywords in the __init__ method. Here's how you can use an additional formlib trick if you don't have such a handy __init__ method:

# This is the mypackage.browser module
from zope.formlib import form

from mypackage.interfaces import IFruit
from mypackage.fruit import Fruit

class FruitAdd(form.AddForm):

    form_fields = form.Fields(IFruit)

    def create(self, data):
         # applyChanges applies all changed fields named in form_fields
         # to the object, taking the field values from data.
         # In a new object, that's *all* fields.
         fruit = Fruit()
         form.applyChanges(fruit, self.form_fields, data)
         return fruit

applyChanges is also very handy if you use multiple interfaces to build your form_fields variable, e.g. adding IZopeDublinCore fields into the mix. This handy utility method will adapt your object to the correct interface for each and every field to accomplish it's task!