from django.conf.urls import patterns, include, url
from scratchApp.views import hello,view_browser,form_search
from scratchApp import views
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'scratch.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^hello$',hello),
    (r'^$',views.home),
    (r'^form_search',views.form_search),
    (r'^search_this',views.search_this),
    (r'^submit_data',views.submit_data),
    (r'^login_check',views.login_check),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                 {'document_root': settings.MEDIA_ROOT}),
) 
