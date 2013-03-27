from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', 'tvsr.tvsrapp.views.index'),
    url(r'^a$', 'tvsr.tvsrapp.views.boot'),
    url(r'^subject/(\d+)/$', 'tvsr.tvsrapp.views.show'),
    url(r'image/(?P<path>.*)$','django.views.static.serve', 
        {'document_root': settings.IMG_DIR }), 


    # Examples:
    # url(r'^$', 'tvsr.views.home', name='home'),
    # url(r'^tvsr/', include('tvsr.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
