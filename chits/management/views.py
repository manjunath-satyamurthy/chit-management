from django.shortcuts import render, redirect
from django.template import loader, RequestContext
from django.http import JsonResponse
from django.contrib.auth import authenticate, login as dj_login, \
    logout as dj_logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from base.models import ChitUser
from management.models import Member, create_member


@csrf_exempt
def test_image_upload(request):
    if request.method == 'POST':
        user = ChitUser.objects.all()
        _file = request.FILES['file']
        print _file
        m = Member(user=user[0], first_name='fell', last_name='bkjh',
                username='bubul',address='INia', phone_number='8121356', 
                photo=_file)
        m.save()
        return JsonResponse({'message': 'success'})


@login_required
def dashboard(request):
    if request.method == 'GET':
        return render(request, 'dashboard.html')


@login_required
def view_members(request):
    if request.method == 'GET':
        return render(request, 'members.html')


@csrf_exempt
@login_required
def create_new_member(request):
    """
    View to handle create_new_member
    """
    if request.method == 'GET':
        return render(request, 'create_member.html')
    if request.method == 'POST':
        data = request.POST
        firstname , lastname = data['firstname'], data['lastname']
        address = data['address']
        phone_number = data['phone_number']
        photo = request.FILES['photo']
        print photo

        new_member = create_member(user=request.user, firstname=firstname,
                lastname=lastname, address=address, phone_number=phone_number,
                photo=photo)

        return redirect('view_members')