# vim: tabstop=4 expandtab autoindent shiftwidth=4 fileencoding=utf-8

from django.views.generic.simple import direct_to_template

from django.conf.urls.defaults import *
from django.contrib.auth import views as auth_views

from dagny.urls import resources

from olojapidellyt.web import views

urlpatterns = patterns('',
    url(r'^tarinat/', resources('web.resources.Story', name='Story', id=('slug', r'[\w\-\d]+'))),
    url(r'^profiili/', resources('web.resources.UserProfile', name='UserProfile', id=('username', r'[\w\-_@\d]+'))),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^poista/$', views.clear, name='clear'),
    url(r'^ehdot/$', direct_to_template, {
        'template': 'terms.html',
    }, name='terms'),
    url(r'^$', views.index, name='index'),
)

# EOF

