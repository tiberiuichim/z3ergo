from zope.schema import Text
from zope.interface import implements
from learningjourney.schema.html.interfaces import IHtml


class Html(Text):
    implements(IHtml)