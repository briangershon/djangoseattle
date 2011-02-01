from django.shortcuts import render_to_response
from django.template.context import RequestContext

def home(request):
    ''' 
    Home Page of the twitter search app
    '''
    
    return render_to_response(
        'twitsearch/twit_include.html',
        RequestContext(request)                     
        )