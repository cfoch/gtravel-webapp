from django.conf.urls import patterns, url

from events import views

urlpatterns = patterns('',
    url(r'^(?P<event_id>\d+)/$', views.event_view, name='detail'),
)
