# howdy/views.py
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse


# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

def callback(request):
    
    verification_code = request.GET.get('verification_code')
    userid = request.GET.get('userid')
    
#    context = {
#        'verification_code': verification_code,
#        'userid': verification_url,
#    }

    return HttpResponse ("Your verification code is: '{0}' and your user id is: '{1}'".format(verification_code, userid))
