from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app.forms import BootstrapAuthenticationForm
from django import forms
from django.utils.translation import ugettext_lazy as _
import pymysql
import app.connectsql as ac

def customer_query(request,param1):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/query_customer.html',
        {
            'username':param1,
            'title':'Query',
            'message':'Go Query',
            'year':datetime.now().year,
        }
    )
def change_pw(request,param2):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/change_password.html',
        {
            'username':param2,
            'title':'Change your password!',
            'message':'ChangeGo',
            'year':datetime.now().year,
        }
    )
def real_change_pw(request,param2):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/change_password_result.html',
        {
            'username':param2,
            'message1':'You have changed your password.',
            'year':datetime.now().year,
        }
    )
def customer_query_order(request,param2):
     assert isinstance(request, HttpRequest)
     return render(
            request,
            'app/query_customer_result.html',
            {
                'username':param2,
                'message1':"LCY",
                'message2':"LCY",
                'year':datetime.now().year,
            }
        )

def customer_query_waybill(request,param3):
    assert isinstance(request, HttpRequest)
    return render(
            request,
            'app/query_customer_result.html',
            {
                'username':param3,
                'message1':"LCY",
                'message2':"LCY",
                'year':datetime.now().year,
            }
        )

def customer_query_deliverman(request,param3):
    assert isinstance(request, HttpRequest)
    return render(
            request,
            'app/query_customer_result.html',
            {
                'username':param3,
                'message1':"LCY",
                'message2':"LCY",
                'year':datetime.now().year,
            }
        )

def customer_query_all_order(request,param3):
    assert isinstance(request, HttpRequest)
    return render(
            request,
            'app/query_customer_result.html',
            {
                'username':param3,
                'message1':"LCY",
                'message2':"LCY",
                'year':datetime.now().year,
            }
        )
