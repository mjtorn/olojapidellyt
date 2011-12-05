# vim: tabstop=4 expandtab autoindent shiftwidth=4 fileencoding=utf-8

from django.conf.urls.defaults import *
from dagny.urls import resources

urlpatterns = patterns('',
    url(r'^tarinat/', resources('web.resources.Story', name='Story', id=('slug', r'[\w\-\d]+'))),
)

# EOF

