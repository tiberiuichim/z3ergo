Indexes and cataloguing. Using locale formatting
-------------------------------------------------

* Catalogues are a fast way of indexing objects and interogating them
* Objects are indexed based on defined indexes

* Catalogs use a unique-id utility to assign short integers ids to objects. This utility
  needs to be added in the ZMI before the catalog is created (1) (2)

* added a new adapter for IBook that returns ISearchableText information type, with an attribute
  of getSearchableText (in the textindex package)

* Inside the search.pt obj/@@absolute_url view is used to get the absolute url of an object (3)

* Inside the search view (search.py), the locale information (modification date for the object) is
displayed using the dateTime locale formatter. Other date and time formatters are: dateTime, date, time (look at zope/i18n/locales/__init__.py)


(1) Create a IntId utility
  * Navigate to ++etc++site/default, add a new IntId utility, no name, hit the register button,
    register without any name

(2) Create the catalog utility
  * Navigate to ++etc++site/default, add a Catalog, no name, hit the register button with
    default settings
  * Add a new Text Index in the catalog for interface zope.index.interfaces.ISearchableText,
    name getSearchableText, callable
  * Add a few ZPT Pages, check the Advanced tab of the Catalog, you should see the number changing

(3) From python, use:
    >>> from zope.app.traversing.browser import absoluteURL
    >>> url = absoluteURL(obj, request)

Tasks
--------
* Finish the i18n for this package (strings, template, etc)