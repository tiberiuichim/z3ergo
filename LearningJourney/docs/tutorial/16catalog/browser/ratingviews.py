from zope.interface import Interface, implements
from zope3tutorial.stage22.interfaces import IRating, IRatingViews

from zope.i18n import MessageFactory
_ = MessageFactory('zope3tutorial')

class RatingViews(object):

    def show_rating(self):
        rating = IRating(self.context)
        return rating.getRating()

    def set_rating(self):
        rating = IRating(self.context)
        value = self.request['rating_value']
        rating.setRating(value)
        return _("Rating set")