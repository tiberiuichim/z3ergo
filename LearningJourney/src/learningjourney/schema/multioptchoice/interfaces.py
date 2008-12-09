from zope.schema.interfaces import IChoice, IList

class IMultiOptionalChoice(IChoice, IList):
    """Fields implementing this interface hold a list of multiple values, chosen 
    from a vocabulary or at random, from the user's choice"""
    
    """
    vocabulary - source for testing the containment of terms
    value_type - the field type for values
    unique - bool if the value should be unique
    """