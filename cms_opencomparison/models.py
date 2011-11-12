from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _

PATH_GRID = '/api/v1/grid/'
PATH_PACKAGE = '/api/v1/package/'

class Grid(CMSPlugin):
    baseurl = models.URLField(_("Opencomparison base URL"),
        default="http://djangopackages.com")

    slug = models.CharField(_("Grid slug"),
           default='django-cms', max_length=50)

    title = models.CharField(_("Grid title"),
           default='Django CMS extensions', max_length=50)

    subtitle = models.CharField(_("Grid subtitle"),
           default='', max_length=50)

    description = models.CharField(_("Grid description"),
           default='', max_length=70)

    def get_grid_url(self):
        return "%s%s" % (self.baseurl,PATH_GRID)

    def get_package_url(self):
        return "%s%s" % (self.baseurl,PATH_PACKAGE)

    def  is_ssl(self):
        try:
            if self.baseurl.split ("://")[0] == "https":
                return True
            return False
        except Exception:
            return False

    def get_hostname(self):
        try:
            return self.baseurl.split ("://")[1].split("/")[0].split(":")[0]
        except Exception:
            return ""

    def get_port(self):
        try:
            return int(self.baseurl.split ("://")[1].split("/")[0].split(":")[1])
        except Exception:
            if self.is_ssl():
                return 443
            return 80

    def __unicode__(self):
        return "grid (%s - %s)" % (self.baseurl,self.slug)
