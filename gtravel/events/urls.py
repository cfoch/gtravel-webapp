from django.conf.urls import patterns, url

from events.views import event_view
from applications.views import manage_application

urlpatterns = patterns('',
    url(r'^(?P<event_id>\d+)/$', event_view, name='detail'),
    url(r'^(?P<event_id>\d+)/apply$', manage_application, name='detail'),
)
