from zope.app.basicskin.standardmacros import StandardMacros as BaseMacros
from zope.component import getMultiAdapter

class StandardMacros(BaseMacros):
    aliases = {
               'error':'page',
               'dialog':'page',
#               'view':'page',
               } 
    macro_pages = (
                   'view_macros',
                   'login_macros',
                   'search_macros',
                   'sidebar_macros',
                   )
    
    def __getitem__(self, key):
        key = self.aliases.get(key, key)
        context = self.context
        request = self.request
        for name in self.macro_pages:
            page = getMultiAdapter((context, request), name=name)
            try:
                v = page[key]
            except KeyError:
                pass
            else:
                return v
        raise KeyError(key)