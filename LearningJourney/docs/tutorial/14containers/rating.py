from zope.schema import TextLine
from persistent import Persistent
from zope.interface import implements
from interfaces import IRating
from zope.annotation.interfaces import IAnnotations

class Rating(object):
    implements(IRating)
    def __init__(self, context):
        self.context = context
        try:
            rating = IAnnotations(self.context)['zope3tutorial.stage12.book.rating']
        except KeyError:
            IAnnotations(self.context)['zope3tutorial.stage12.book.rating'] = 0

    def getRating(self):
        rating = IAnnotations(self.context)['zope3tutorial.stage12.book.rating']
        return rating

    def setRating(self, value):
        IAnnotations(self.context)['zope3tutorial.stage12.book.rating'] = value


class RatingEdit:
    def setData(self, data):
        rating = IRating(self.context)
        rating.setRating(data['rating'])

    def getData(self):
        rating = IRating(self.context)
        return {'rating':rating.getRating()}