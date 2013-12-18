from django.conf.urls import patterns, url

from applications import views


urlpatterns = patterns('',

    #manage_application
    url(r'^$', views.manage_application, name='application'),

)
