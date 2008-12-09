from learningjourney.i18n import _
from zope.app.catalog.interfaces import ICatalogIndex, IAttributeIndex
from zope.schema import Bool, BytesLine, Choice

class IKeywordIndex(IAttributeIndex, ICatalogIndex):
    """Interface-based catalog text index
    """

    interface = Choice(
        title=_(u"Interface"),
        description=_(u"Objects will be adapted to this interface"),
        vocabulary=_("Interfaces"),
        required=False,
        )

    field_name = BytesLine(
        title=_(u"Field Name"),
        description=_(u"Name of the field to index"),
        )

    field_callable = Bool(
        title=_(u"Field Callable"),
        description=_(u"If true, then the field should be called to get the "
                      u"value to be indexed"),
        default=True,
        )
    
    def unique_values():
        """Return unique values stored in this index"""