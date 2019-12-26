"""
Definition of urls for Django_Complete_Model.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about$', app.views.about, name='about'),
    #url(r'^login/$',
        #django.contrib.auth.views.login,
        #{
            #'template_name': 'app/login.html',
            #'authentication_form': app.forms.BootstrapAuthenticationForm,
            #'extra_context':
            #{
                #'title': 'Log in',
                #'year': datetime.now().year,
            #}
        #},
        #name='login'),
    url(r'^login$', app.views.login, name='login'),
    url(r'^do_login$',app.views.do_login,name='do_login'),
    url(r'^query/(.+)/$',app.views.query,name='query'),
    url(r'^update/(.+)/$',app.views.update,name='update'),
    url(r'^real_query_order/(.+)/$',app.views.real_query_order,name='real_query_order'),
    url(r'^real_query_tracking/(.+)/$',app.views.real_query_tracking,name='real_query_tracking'),
    url(r'^real_update/(.+)/$',app.views.real_update,name='real_update'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
