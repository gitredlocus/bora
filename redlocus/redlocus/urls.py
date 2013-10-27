from django.conf.urls import patterns, include, url, handler404
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

handler404 = 'perfect404.views.page_not_found'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'redlocus.views.home', name='home'),
    # url(r'^redlocus/', include('redlocus.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^demo/', include('demo.urls')),
)
