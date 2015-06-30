from django.conf.urls import patterns, url
from management.views import test_image_upload

urlpatterns = patterns(
    "",
    url(r'^imageupload/$', test_image_upload),
    )