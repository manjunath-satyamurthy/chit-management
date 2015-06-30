from django.shortcuts import render
from django.template import loader, RequestContext
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login as dj_login, \
    logout as dj_logout
from django.views.decorators.csrf import csrf_exempt

from base.models import ChitUser
from management.models import Member 


@csrf_exempt
def test_image_upload(HttpRequest):
    if HttpRequest.method == 'POST':
        user = ChitUser.objects.all()
        _file = HttpRequest.FILES['file']
        m = Member(uid=user[0], first_name='fgfell', last_name='bulkjh',
                username='bulkbul',address='INdia', phone_number='81213356', 
                photo=_file)

        m.save()
        return JsonResponse({'message': 'success'})