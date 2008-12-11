Simple annotation of an object. Providing DublinCore information
------------------------------------------------------------------

* changed the implements declaration for the Book class to declare it as
  implementing annotations as attributeannotations
* immediately after declaring that the object implements IAttributeAnnotatable
  there will be information displayed on newly created objects (created/modified)
* created a new function that returns an adaptor implementation for IZopeDublinCore