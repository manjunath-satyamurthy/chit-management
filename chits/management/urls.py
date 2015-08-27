from django.conf.urls import patterns, url
from management.views import dashboard, view_members, \
    create_new_member, view_chits, create_chit, view_payments, \
    auction

urlpatterns = patterns(
    "",
    url(r'^dashboard/$', dashboard, name='dashboard'),
    url(r'^members/view/$', view_members, name='view_members'),
    url(r'^members/create/$', create_new_member, name='create_new_member'),
    url(r'^chits/view/$', view_chits, name='view_chits'),
    url(r'^chits/create/$', create_chit, name='create_chit'),
    url(r'^record/payments/$', view_payments, name='view_payments'),
    url(r'^record/auctions/$', auction, name='auction'),
    )