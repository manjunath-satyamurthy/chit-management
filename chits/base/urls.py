from django.conf.urls import patterns, url
from base.views import login

urlpatterns = patterns(
    "",
    url(r'^login/$', login),
    )