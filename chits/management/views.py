from django.shortcuts import render
from django.template import loader, RequestContext
from django.http import JsonResponse
from django.contrib.auth import authenticate, login as dj_login, \
    logout as dj_logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from base.models import ChitUser
from management.models import Member 


@csrf_exempt
def test_image_upload(request):
    if request.method == 'POST':
        user = ChitUser.objects.all()
        _file = request.FILES['file']
        m = Member(user=user[0], first_name='fell', last_name='bkjh',
                username='bubul',address='INia', phone_number='8121356', 
                photo=_file)
        m.save()
        return JsonResponse({'message': 'success'})


@login_required
def dashboard(request)