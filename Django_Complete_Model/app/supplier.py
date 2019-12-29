from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app.forms import BootstrapAuthenticationForm
from django import forms
from django.utils.translation import ugettext_lazy as _
import pymysql

def supplier_query(request,param1):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/query_supplier.html',
        {
            'username':param1,
            'title':'Query',
            'message':'Go Query',
            'year':datetime.now().year,
        }
    )

def supplier_query_order(request,param2):
     assert isinstance(request, HttpRequest)
     return render(
            request,
            'app/query_supplier_result.html',
            {
                'username':param2,
                'message1':"LCY",
                'message2':"LCY",
                'year':datetime.now().year,
            }
        )

def supplier_query_waybill(request,param3):
    assert isinstance(request, HttpRequest)
    return render(
            request,
            'app/query_supplier_result.html',
            {
                'username':param3,
                'message1':"LCY",
                'message2':"LCY",
                'year':datetime.now().year,
            }
        )

def supplier_query_latest_customer(request,param3):
    assert isinstance(request, HttpRequest)
    return render(
            request,
            'app/query_supplier_result.html',
            {
                'username':param3,
                'message1':"LCY",
                'message2':"LCY",
                'year':datetime.now().year,
            }
        )

def supplier_query_latest_order_amount(request,param3):
    assert isinstance(request, HttpRequest)
    return render(
            request,
            'app/query_supplier_result.html',
            {
                'username':param3,
                'message1':"LCY",
                'message2':"LCY",
                'year':datetime.now().year,
            }
        )

def supplier_query_all_order(request,param3):
    assert isinstance(request, HttpRequest)
    return render(
            request,
            'app/query_supplier_result.html',
            {
                'username':param3,
                'message1':"LCY",
                'message2':"LCY",
                'year':datetime.now().year,
            }
        )
