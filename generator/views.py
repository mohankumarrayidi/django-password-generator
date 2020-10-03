from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.

#
def home(request):
    return HttpResponse('hellow')

#
# def homeHtml(request):
#     return render(request,'generator/home.html',{'password':'mjkgjgGKGgk'})

def homeHtml(request):
    return render(request,'generator/home.html')

def About(request):
    return render(request,'generator/About.html')

# def egg(request):
#     return HttpResponse('eggs')

def password(request):

    charactors = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('special'):
        charactors.extend(list('@#$%^&*!'))

    if request.GET.get('uppercase'):
        charactors.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        charactors.extend(list('1234567890'))




    length = int(request.GET.get('length',10))
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(charactors)
    return render(request,'generator/password.html', {'password':thepassword})
