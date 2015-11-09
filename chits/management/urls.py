from django.conf.urls import patterns, url
from management.views import dashboard, view_members, \
    create_new_member, view_chits, create_chit, view_payments, \
    auction, delete_user, download_url_for_local, \
    download_url_for_AWS_S3

urlpatterns = patterns(
    "",
    url(r'^dashboard/$', dashboard, name='dashboard'),
    url(r'^members/view/$', view_members, name='view_members'),
    url(r'^members/create/$', create_new_member, name='create_new_member'),
    url(r'^chits/view/$', view_chits, name='view_chits'),
    url(r'^chits/create/$', create_chit, name='create_chit'),
    url(r'^record/payments/$', view_payments, name='view_payments'),
    url(r'^record/auctions/$', auction, name='auction'),
    url(r'^delete/user/$', delete_user, name='delete_user'),
    # url(r'^report/url/$', download_url_for_local, name='download_url_for_local'),
    url(r'^report/url/$', download_url_for_AWS_S3, name='download_url_for_AWS_S3'),
    )