from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gtravel.views.home', name='home'),
    # url(r'^gtravel/', include('gtravel.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^application/', 'applications.views.manage_application'),
    url(r'^home/', 'home.views.index'),
    url(r'^signup/', 'userprofile.views.signup'),
    url(r'^login/$', 'home.views.login_view'),
    url(r'^logout/$', 'home.views.logout_view'),
    #Urls from EVENTS
    url(r'^events/', include('events.urls', namespace="events")),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
