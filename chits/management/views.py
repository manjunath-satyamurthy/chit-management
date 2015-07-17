import json, datetime

from django.shortcuts import render, redirect
from django.template import loader, RequestContext
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate, login as dj_login, \
    logout as dj_logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from base.models import ChitUser
from management.models import Member

from management.dbapi import get_members_by_user, create_member, \
    get_chits_by_user, create_chit_batch, get_members_by_ids


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
        members_template = loader.get_template('view_members.html')
        c = RequestContext(request,
                {'members': get_members_by_user(request.user)}
            )
        return HttpResponse(members_template.render(c))


# @login_required
# def view_member_details(request):
#     if request.method == 'GET':
        

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
        photo = request.FILES.get('photo')

        new_member = create_member(user=request.user, firstname=firstname,
                lastname=lastname, address=address, phone_number=phone_number,
                photo=photo)

        return redirect('view_members')


@login_required
def view_chits(request):
    """
    To view information of all chit batches
    """
    if request.method == "GET":
        view_chits_template = loader.get_template('view_chits.html')
        c = RequestContext(request,
                {'chits': get_chits_by_user(request.user)}
            )
        return HttpResponse(view_chits_template.render(c))


@csrf_exempt
@login_required
def create_chit(request):
    """
    To create a new chit batch
    """
    if request.method == 'GET':
        create_chit_template = loader.get_template('create_chit.html')
        c = RequestContext(request,
                {'members': get_members_by_user(request.user)}
            )
        return HttpResponse(create_chit_template.render(c))

    if request.method == 'POST':
        data = json.loads(request.POST['data'])

        raw_dt = data['datetime']
        mids = data['chit_members_id']
        date = datetime.date(raw_dt['yyyy'], raw_dt['mm'], raw_dt['dd'])
        time = datetime.time(raw_dt['h'], raw_dt['m'], 0) 
        members = get_members_by_ids(mids)
        new_chit = create_chit_batch(user=request.user, name=data['name'],
            principal=data['principal'], period=data['period'],
            no_of_members=data['no_of_members'], start_date=date,
            start_time=time, members=members)

        return JsonResponse({
            'status': 'success'
            })

