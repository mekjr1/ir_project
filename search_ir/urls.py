from django.conf.urls import patterns, include, url
from views import search_view,autocomplete
from search_ir import views

urlpatterns = patterns('search_ir.views',
    # Examples:
    # url(r'^$', 'django17_haystack.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^search$', search_view, name='search_view'),
    url(r'^autocomplete/$', 'autocomplete'),

)