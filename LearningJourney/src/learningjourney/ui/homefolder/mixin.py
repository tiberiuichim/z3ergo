from zope.dublincore.interfaces import IZopeDublinCore
import HTMLParser


class MLStripper(HTMLParser.HTMLParser):
    """An html parser that strips all tags and only outputs text"""
    
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_fed_data(self):
        return ''.join(self.fed)
    
    
class EntryDetailMixin(object):
    @property
    def dc(self):
        return IZopeDublinCore(self.context)
    
    def title(self):
        parser = MLStripper()
        parser.feed(self.context.text)
        text = parser.get_fed_data()
        if len(text) > 27:
            text = text[:27] + u'...'
        return text