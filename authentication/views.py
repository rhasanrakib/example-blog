from django.http import Http404
from django.shortcuts import render, redirect
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from json import loads as jsonloads
from django.http import HttpResponseRedirect
from . models import User
# LOGIN VIEW ENDPOINT


def login(response):

    return render(response, 'login.html')


@csrf_exempt
def register(request):
    if request.method == 'POST':

        try:
            #datas = jsonloads(request.POST["val"])
            # print(datas)
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            password = request.POST['pass2']
            # first_name=datas['first_name']
            #last_name = datas['last_name']
            #email =datas['email']
            #password =datas['pass2']
            # print(first_name)
            user = User.objects.create_user(
                first_name=first_name, last_name=last_name, password=password, email=email)
            user.save()
            y={'mgs':'success'}
            return render(request, 'register.html',{'x':y})
            #return redirect("posts:post_home",{'x':y})
            # return JsonResponse({}, status=200)
        except Exception as ex:
            y={'mgs':'failed',
                'error':ex,
            }
            
            return render(request, 'register.html',{'x':y})
            #return redirect("posts:post_home",{'x':y})
    return render(request, 'register.html')
