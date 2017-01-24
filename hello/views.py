
# hello/views.py
from django.http import HttpResponse
from datetime import datetime


# Create your views here.
def hello(request):
    # get name param
    name = request.GET.get('name')
        
    # compose head
    head='<head><title>Spring Hello</title></head>';
        
    # get time
    hour = datetime.now().time().hour
    greeting=''
    if hour >= 4 and hour <= 10:
        greeting = 'Good morning, {0}!'
    elif hour >= 11 and hour <= 15:
        greeting = 'Good day, {0}!'
    elif hour >= 16 and hour <= 18:
        greeting = 'Good afternoon, {0}!'
    elif hour >= 19 and hour <= 22:
        greeting = 'Good evening, {0}!'
    else:
        greeting = 'Good night, {0}!'

    print hour
        
    # compose body
    body=('<body>'+greeting+'</body>').format(name if name != None else 'hoo-man')

    # compose html
    html='<html>'+head+body+'</html>'
    
    return HttpResponse(html)
