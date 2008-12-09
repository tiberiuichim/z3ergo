from learningjourney.app.util import get_site_url


class SiteUrl(object):
    def __call__(self):
        return get_site_url(self.request)
    
    
class DebugPage(object):
    
    def __call__(self):
        import pdb;pdb.set_trace()
        return "Debug finished"