from learningjourney.widget.tinymce.interfaces import IRichTextWidget
from zope.app.component.hooks import getSite
from zope.app.form.browser.textwidgets import TextWidget
from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile
from zope.interface.declarations import implements
from zope.traversing.browser.absoluteurl import absoluteURL
from zope.traversing.namespace import getResource

TPL = """
%(widget)s
<script type="text/javascript" src="%(scriptpath)s"></script>
<script type="text/javascript">
  tinyMCE.init({
      mode : "exact",
      elements : "%(name)s",
      auto_resize:true,
      width:"400px",
      height:"300px"
  }
  );
</script>
"""

class RichTextWidget(TextWidget):
    implements(IRichTextWidget)
    
    def __call__(self, *args, **kw):
        widget_html = super(RichTextWidget, self).__call__(*args, **kw)
        site = getSite()
        site_url = absoluteURL(site, self.request)
        return TPL % {
                      'widget':widget_html,
                      'scriptpath':'%s/@@/tinymce/tiny_mce.js' % site_url,
                      'name':self.name
                      }