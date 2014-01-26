from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from tango_in_blood_app.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tango_in_blood.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^team/(?P<team_name>\w+)/$', TeamView.as_view()),
    
    url(r'^accounts/profile/$', ProfileView.as_view()),

    url(r'^logout/$', 'tango_in_blood_app.views.user_logout'),
    
    url(r'^accounts/', include('allauth.urls')),
   
    url(r'^checkpassword/$', 'tango_in_blood_app.views.checkpassword'),   
     
    url(r'^$', TemplateView.as_view(template_name='index.html')),
)
