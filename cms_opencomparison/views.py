from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404

from cms_opencomparison import models

import httplib

def get_grid(request, grid_id):
    grid = None
    try:
      grid = models.Grid.objects.get(pk=grid_id)

      h = None
      if grid.is_ssl():
        h = httplib.HTTPSConnection(grid.get_hostname(),grid.get_port())
      else:
        h = httplib.HTTPConnection(grid.get_hostname(),grid.get_port())

      headers = {
        'User-Agent': 'django_cms_opencomparison',
      }
      print grid.get_grid_url() + grid.slug
      h.request('GET', grid.get_grid_url() + grid.slug + "/", "", headers)
      res = h.getresponse()
      res = res.read()

    except Exception, e:
      print e
      res = ''

    return HttpResponse(
            res,
            mimetype='application/json')

def get_package(request, grid_id, package_slug):
    grid = None
    try:
      grid = models.Grid.objects.get(pk=grid_id)

      h = None
      if grid.is_ssl():
        h = httplib.HTTPSConnection(grid.get_hostname(),grid.get_port())
      else:
        h = httplib.HTTPConnection(grid.get_hostname(),grid.get_port())

      headers = {
        'User-Agent': 'django_cms_opencomparison',
      }
      h.request('GET', grid.get_package_url() + package_slug + "/", "", headers)
      res = h.getresponse()
      res = res.read()

    except Exception, e:
      res = ''

    return HttpResponse(
            res,
            mimetype='application/json')

