from dssite.forms import LaunchReminderForm
import django.utils.simplejson as json
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponse

from basic.blog.models import Post

def home(request):
    """ Dynamic Home Page """
    blog_entries = Post.objects.published()[:4]
    
    form = LaunchReminderForm()
    parameters = {'form': form,
                  'blog_entries': blog_entries}
    return render_to_response('dssite/home.html', parameters, RequestContext(request))
