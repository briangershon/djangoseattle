from django.conf import settings
from django.conf.urls.defaults import * #@UnusedWildImport
from django.contrib import admin
from django.views import static
from dssite.views import home
import os

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', home, name='home_page'),
    url(r'^twitter/', include('twitsearch.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'dssite/login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', {'login_url': '/' }),
)

urlpatterns += patterns('',
    url(r'^blog/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{1,2})/(?P<slug>[-\w]+)/$',
        view='basic.blog.views.post_detail',
        kwargs={'template_name':'custom_blog/post_detail.html'},
        name='blog_detail'),
    url(r'^blogs/', 
        view='basic.blog.views.post_list',
        kwargs={'template_name':'custom_blog/post_list.html'},
        name='blog_list'),
    url(r'^profile/', include('basic.profiles.urls'), name="profiles"),
    url(r'^events/', include('basic.events.urls'), name="events"),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', static.serve, {'document_root': os.path.join(settings.PROJECT_ROOT, 'static')}),
    ) 
