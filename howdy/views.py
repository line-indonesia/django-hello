# howdy/views.py
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from datetime import datetime


# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

def callback(request):
    
    verification_code = request.GET.get('verification_code')
    userid = request.GET.get('userid')

    return HttpResponse ("Your verification code is: '{0}' and your user id is: '{1}'".format(verification_code, userid))


def hello(request):

    name = request.GET.get('name')

    localHour = datetime.now().time().hour
    if localHour >= 4 and localHour <= 10:
        greeting = "Good morning, {0}!".format(name)
    elif localHour >= 11 and localHour <= 15:
        greeting = "Good day, {0}!".format(name)
    elif localHour >= 16 and localHour <= 18:
        greeting = "Good afternoon, {0}!".format(name)
    elif localHour >= 19 and localHour <= 22:
        greeting = "Good evening, {0}!".format(name)
    else:
        greeting = "Good night, {0}!".format(name)

    return HttpResponse (greeting)
