from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', "about.views.about"),
    (r'acknowledgements/$', "about.views.acknowledgements"),
    (r'acknowledgements/(?P<name>[\w,._-]+)/$', "about.views.person_acknowledged"),
    (r'people/$', "about.views.our_people"),
)
