Annotating an object: Providing ratings for books
------------------------------------------------------------------

* restructured the package:
    * browser views are separated in the `browser` package
    * the browser configure.zcml is refering to it parent package using the dotted notation (..)
    * separated interfaces in separate file (interfaces)
* added a new interface, IRating
* added a new class, Rating, which implements rating as annotations for an object
* added view & edit views for ratings for IBook