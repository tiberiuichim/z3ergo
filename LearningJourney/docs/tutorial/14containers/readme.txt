Containers
------------

* Added new content class (BookDatabase in bookdatabase.py), derived from BTreeContainer
* Added browser:contentViews for this class (in browser/configure.zcml). This enables
  the container related views for BookDatabase (contents, add menu). There are some permissions
  specified there to enable several views (Add, Contents, Index)
* Changed the class interface implementation for Book to include IBookContained, which defines
  a parent field with a condition on type
