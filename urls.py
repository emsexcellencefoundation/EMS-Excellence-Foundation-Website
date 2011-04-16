from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', "about.views.index"),
    (r'^about/', include("about.urls")),
    (r'^admin/', include(admin.site.urls)),
    (r'^delete_position/(?P<position_id>\d+)/$', 'about.views.delete_position'),
    (r'^login/$', 'about.views.login_user'),
    (r'^logout/$', 'about.views.logout_user'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.SITE_ROOT + '/media', 'show_indexes': True}),
    )
