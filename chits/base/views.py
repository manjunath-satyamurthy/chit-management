from django.shortcuts import render, redirect
from django.template import loader, RequestContext
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login as dj_login, \
    logout as dj_logout
from django.views.decorators.csrf import csrf_exempt

from base.models import ChitUser

@csrf_exempt
def login(request):
    if request.method == "GET":
        login_template = loader.get_template('login.html')
        c = RequestContext(request)
        return HttpResponse(login_template.render(c))
    if request.method == "POST":
        data = request.POST
        username, password = data['username'], data['password']
        user = authenticate(username=username, password=password)

        if user:
            dj_login(request, user)
            c = RequestContext(request)
            return redirect('calendar')
        return JsonResponse({'message': 'Invalid Credentials'}, status=401)

