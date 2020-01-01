"""
Definition of urls for Django_Complete_Model.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views
import app.customer
import app.supplier
import app.depository
import app.logisticcenter

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
    url(r'^customer_query/(.+)/$',app.customer.customer_query,name='customer_query'),
    url(r'^change_pw/(.+)/$',app.customer.change_pw,name='change_pw'),
    url(r'^real_change_pw/(.+)/$',app.customer.real_change_pw,name='real_change_pw'),
    url(r'^customer_query_order/(.+)/$',app.customer.customer_query_order,name='customer_query_order'),
    url(r'^customer_query_waybill/(.+)/$',app.customer.customer_query_waybill,name='customer_query_waybill'),
    url(r'^customer_query_dm/(.+)/$',app.customer.customer_query_deliverman,name='customer_query_dm'),
    url(r'^customer_query_all_order/(.+)/$',app.customer.customer_query_all_order,name='customer_query_all_order'),
    url(r'^supplier_query/(.+)/$',app.supplier.supplier_query,name='supplier_query'),
    url(r'^supplier_query_order/(.+)/$',app.supplier.supplier_query_order,name='supplier_query_order'),
    url(r'^supplier_query_waybill/(.+)/$',app.supplier.supplier_query_waybill,name='supplier_query_waybill'),
    url(r'^supplier_query_latest_customer/(.+)/$',app.supplier.supplier_query_latest_customer,name='supplier_query_latest_customer'),
    url(r'^supplier_query_latest_order_amount/(.+)/$',app.supplier.supplier_query_latest_order_amount,name='supplier_query_latest_order_amount'),
    url(r'^supplier_query_all_order/(.+)/$',app.supplier.supplier_query_all_order,name='supplier_query_all_order'),
    url(r'^depository_query/(.+)/$',app.depository.depository_query,name='depository_query'),
    url(r'^depository_query_own/(.+)/$',app.depository.depository_query_own,name='depository_query_own'),
    url(r'^depository_update/(.+)/$',app.depository.depository_update,name='depository_update'),
    url(r'^depository_change/(.+)/$',app.depository.depository_change,name='depository_change'),
    url(r'^depository_change_management/(.+)/$',app.depository.depository_change_management,name='depository_change_management'),
    url(r'^depository_update_transfer/(.+)/$',app.depository.depository_update_transfer,name='depository_update_transfer'),
    url(r'^depository_update_distribution/(.+)/$',app.depository.depository_update_distribution,name='depository_update_distribution'),
    url(r'^depository_update_management/(.+)/$',app.depository.depository_update_management,name='depository_update_management'),
    url(r'^logisticcenter_query/(.+)/$',app.logisticcenter.logisticcenter_query,name='logisticcenter_query'),
    url(r'^logisticcenter_update/(.+)/$',app.logisticcenter.logisticcenter_update,name='logisticcenter_update'),
    url(r'^logisticcenter_change(.+)/$',app.logisticcenter.logisticcenter_change,name='logisticcenter_change'),
    url(r'^logisticcenter_delete(.+)/$',app.logisticcenter.logisticcenter_delete,name='logisticcenter_delete'),
    url(r'^lc_query_depository_information/(.+)/$',app.logisticcenter.lc_query_depository_information,name='lc_query_depository_information'),
    url(r'^lc_query_supplier_information/(.+)/$',app.logisticcenter.lc_query_supplier_information,name='lc_query_supplier_information'),
    url(r'^lc_query_customer_information/(.+)/$',app.logisticcenter.lc_query_customer_information,name='lc_query_customer_information'),
    url(r'^lc_query_waybill_information/(.+)/$',app.logisticcenter.lc_query_waybill_information,name='lc_query_waybill_information'),
    url(r'^lc_query_order_information/(.+)/$',app.logisticcenter.lc_query_order_information,name='lc_query_order_information'),
    url(r'^lc_query_transfer_information/(.+)/$',app.logisticcenter.lc_query_transfer_information,name='lc_query_transfer_information'),
    url(r'^lc_query_depository_leftcapacity/(.+)/$',app.logisticcenter.lc_query_depository_leftcapacity,name='lc_query_depository_leftcapacity'),
    url(r'^lc_query_deliverman_information/(.+)/$',app.logisticcenter.lc_query_deliverman_information,name='lc_query_deliverman_information'),
    url(r'^lc_query_distribution_information/(.+)/$',app.logisticcenter.lc_query_distribution_information,name='lc_query_distribution_information')
    url(r'^lc_update_supplier/(.+)/$',app.logisticcenter.lc_update_supplier,name='lc_update_supplier'),
    url(r'^lc_update_customer/(.+)/$',app.logisticcenter.lc_update_customer,name='lc_update_customer'),
    url(r'^lc_update_depository/(.+)/$',app.logisticcenter.lc_update_depository,name='lc_update_depository'),
    url(r'^lc_update_waybill/(.+)/$',app.logisticcenter.lc_update_waybill,name='lc_update_waybill'),
    url(r'^lc_update_order/(.+)/$',app.logisticcenter.lc_update_order,name='lc_update_order'),
    url(r'^lc_update_order_good/(.+)/$',app.logisticcenter.lc_update_order_good,name='lc_update_order_good'),
    url(r'^lc_update_route/(.+)/$',app.logisticcenter.lc_update_route,name='lc_update_route'),
    url(r'^lc_change_management/(.+)/$',app.logisticcenter.lc_change_management,name='lc_change_management'),
    url(r'^lc_delete_customer/(.+)/$',app.logisticcenter.lc_delete_customer,name='lc_delete_customer'),
    url(r'^lc_delete_supplier/(.+)/$',app.logisticcenter.lc_delete_supplier,name='lc_delete_supplier'),
    url(r'^lc_delete_depository/(.+)/$',app.logisticcenter.lc_delete_depository,name='lc_delete_depository'),
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
