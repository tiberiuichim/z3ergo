An automatic view page
-----------------------------------------------

* zope.app.form provides a way to automatically create views based on schema
* so we declare a new "browser:schemadisplay" and specify that it should
  appear in the zmi_views menu
* because I've changed the view name for the view action to bookview.html,
  the browser:defaultView needs to be updated
* the view class with its utilities is no longer needed
