from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from django.contrib.auth import authenticate, login as dj_login, \
    logout as dj_logout
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login(HttpRequest):
    if HttpRequest.method == "POST":
        data = HttpRequest.POST
        username, password = data['username'], data['password']

        user = authenticate(username=username, password=password)
        if user:
            dj_login(HttpRequest, user)
            return JsonResponse({'message': 'success'})
        return JsonResponse({'message': 'Invalid Credentials'}, status=401)
