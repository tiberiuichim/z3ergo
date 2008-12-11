Enhancing the add object with automatic forms
-----------------------------------------------

* zope.app.form provides a way to automatically create add forms based on schemas
* so the interface needs to be enhanced to declare fields
* browser:addItemMenu gets a new attribute, specifying the view to be used when adding
* declared a new view, automatically generated from a form (browser:addform)