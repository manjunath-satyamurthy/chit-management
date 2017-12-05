import json, datetime, time

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
    get_chits_by_user, create_chit_batch, get_members_by_ids, \
    is_chit_name_existing, get_live_chit_batches, \
    get_payment_records_by_chitbatch_id_date, get_chitbatch_by_id, \
    get_chitbatch_distinct_bit_dates, update_payment, \
    get_recent_auctions, update_bid_record, update_chit_batch

from management.view_utils \
    import group_auctions_by_current_complete_remaining


@login_required
def calendar(request):
    if request.method == 'GET':
        return render(request, 'calendar.html')

@csrf_exempt
def test(request):
    if request.method == 'POST':
        data = json.loads(request.POST['data'])

        return JsonResponse({
                'greetings': 'Hi jaanu',
                'message': 'I love you',
                'client message': data['message']
                })


@login_required
def view_members(request):
    if request.method == 'GET':
        members_template = loader.get_template('view_members.html')
        c = RequestContext(request,
                {'members': get_members_by_user(request.user)}
            )
        return HttpResponse(members_template.render(c))
        

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

        if is_chit_name_existing(data['name']):
            return JsonResponse({
                'status': 'failed',
                'message': 'Chit name already exists'
                })

        members = get_members_by_ids(mids)
        new_chit = create_chit_batch(user=request.user, name=data['name'],
            principal=data['principal'], period=data['period'],
            no_of_members=data['no_of_members'], start_date=date,
            start_time=time, members=members)

        return JsonResponse({
            'status': 'success'
            })


@csrf_exempt
@login_required
def view_payments(request):
    if request.method == 'GET':

        chitbatch_id = request.GET.get('id')
        bid_date = request.GET.get('bid_date')
        payment_record_template = loader.get_template(
            'payment_record.html'
        )
        if not chitbatch_id:
            bid_dates = {}
            chits = get_live_chit_batches(request.user)
            c = RequestContext(request,{
                    'chits': chits,
                    'bid_dates': get_chitbatch_distinct_bit_dates(chits),
                    'get_chit': True
                })
        else:
            bd = datetime.date(*map(int, bid_date.split('-')))
            c = RequestContext(request,{
                    'chitbatch': get_chitbatch_by_id(chitbatch_id),
                    'payment_records': get_payment_records_by_chitbatch_id_date(
                        chitbatch_id, bd
                    ),
                    'auction_date': str(bd),
                })

        return HttpResponse(payment_record_template.render(c))

    if request.method == 'POST':
        data = json.loads(request.POST['data'])
        update_payment(data)
        return JsonResponse({
            'status': 'success'
            })


@csrf_exempt
@login_required
def auction(request):
    if request.method == 'GET':
        auction_template = loader.get_template('auctions.html')
        months_auctions = get_recent_auctions()

        auctions = group_auctions_by_current_complete_remaining(
            months_auctions)
        if auctions:
            c = RequestContext(request,{
                'auctions': auctions,
                })
        
        else:
            c = RequestContext(request,{})
        return HttpResponse(auction_template.render(c))

    if request.method == 'POST':
        data = json.loads(request.POST['data'])
        chit = get_chitbatch_by_id(data['chit_id'])
        update_chit_batch(chit, data['bid_amt'])
        update_bid_record(chit, data['mid'], data['bid_amt'])
        return JsonResponse({
            'status': 'success'
            })




