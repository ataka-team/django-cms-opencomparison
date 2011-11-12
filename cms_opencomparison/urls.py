from django.conf.urls.defaults import *

urlpatterns = patterns('cms_opencomparison.views',
    (r'^api/grid/(?P<grid_id>\d+)$', 'get_grid',
       None, 'cms-opencomparison-api-grid'),
    (r'^api/grid/(?P<grid_id>\d+)/(?P<package_slug>[\w-]+)', 'get_package',
       None, 'cms-opencomparison-api-package'),

)
