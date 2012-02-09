from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.views import login, logout
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
        ('', include('contact.urls')),
        (r'^requests/', include('requests_log.urls')),
        url(r'^accounts/login/$', login, name='login'),
        url(r'^accounts/logout/$', logout, name='logout'),

        # Examples:
        # url(r'^src/', include('src.foo.urls')),

        # Uncomment the admin/doc line below to enable admin documentation:
        # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

        # Uncomment the next line to enable the admin:
        # url(r'^admin/', include(admin.site.urls)),
        )


# ... the rest of your URLconf goes here ...

if settings.DEBUG:
    urlpatterns += patterns('',
            url(r'^media/(?P<path>.*)$', 'django.views.static.serve', 
                {
                'document_root': settings.MEDIA_ROOT,
                }),
            )
