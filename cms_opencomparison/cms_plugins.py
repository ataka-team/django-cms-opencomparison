from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms_opencomparison import models

class GridPlugin(CMSPluginBase):
    model = models.Grid
    name = 'Opencomparison Grid Plugin'
    render_template = 'cms_opencomparison/grid.html'

    def render(self, context, instance, placeholder):
        context.update({
            'grid': instance,
            'placeholder': placeholder,
            'name': self.name
        })
        return context

plugin_pool.register_plugin(GridPlugin)
