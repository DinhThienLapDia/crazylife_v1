from django.contrib.admin.widgets import AdminFileWidget
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe
 
class AdminImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None):
        output = []
        if value and getattr(value, "url", None):
            image_url = value.url
            file_name= str(value)
            output.append(u' &lt;div style="float:left; padding:5px"&gt;&lt;a href="%s" target="_blank"&gt;&lt;img src="%s" alt="%s" height=50/&gt;&lt;/a&gt;&lt;/div&gt; %s ' % \
                (image_url, image_url, file_name, _('Change:')))
        output.append(super(AdminFileWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))
