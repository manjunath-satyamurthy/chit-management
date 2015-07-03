from django.conf.urls import patterns, url
from management.views import test_image_upload, dashboard, view_members, \
    create_new_member

urlpatterns = patterns(
    "",
    url(r'^imageupload/$', test_image_upload),
    url(r'^dashboard/$', dashboard, name='dashboard'),
    url(r'^members/$', view_members, name='view_members'),
    url(r'^members/create/$', create_new_member, name='create_new_member'),
    )