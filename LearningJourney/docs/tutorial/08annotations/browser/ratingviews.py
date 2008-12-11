from zope.interface import Interface, implements
from zope3tutorial.stage12.interfaces import IRating, IRatingViews

class RatingViews(object):
    #implements(IRatingViews)
    def show_rating(self):
        rating = IRating(self.context)
        return rating.getRating()

    def set_rating(self):
        rating = IRating(self.context)
        value = self.request['rating_value']
        rating.setRating(value)
        return "Rating set"