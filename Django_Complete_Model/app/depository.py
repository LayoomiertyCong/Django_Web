from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app.forms import BootstrapAuthenticationForm
from django import forms
from django.utils.translation import ugettext_lazy as _
import pymysql

def depository_query(request,param1):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/query_depository.html',
        {
            'username':param1,
            'title':'What a pity',
            'message':'You can only query yourself.',
            'year':datetime.now().year,
        }
    )

def depository_query_own(request,param2):
     assert isinstance(request, HttpRequest)
     return render(
            request,
            'app/query_depository_result.html',
            {
                'username':param2,
                'message1':"LCY",
                'message2':"LCY",
                'year':datetime.now().year,
            }
        )



def depository_update(request,param4):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/update_depository.html',
        {
            'username':param4,
            'title':'Depository Update',
            'message':'UpdateGo',
            'year':datetime.now().year,
        }
    )


def depository_update_transfer(request,param5):
    assert isinstance(request, HttpRequest)
    return render(
            request,
            'app/update_depository_result.html',
            {
                'username':param5,
                'message2':"LCY Updated",
                'year':datetime.now().year,
            }
        )

def depository_update_distribution(request,param5):
    assert isinstance(request, HttpRequest)
    return render(
            request,
            'app/update_depository_result.html',
            {
                'username':param5,
                'message2':"LCY Updated",
                'year':datetime.now().year,
            }
        )

def depository_update_management(request,param5):
    assert isinstance(request, HttpRequest)
    return render(
            request,
            'app/update_depository_result.html',
            {
                'username':param5,
                'message2':"LCY Updated",
                'year':datetime.now().year,
            }
        )

def depository_change(request,param4):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/change_depository.html',
        {
            'username':param4,
            'title':'Depository Change',
            'message':'You can only change management information.',
            'year':datetime.now().year,
        }
    )

def depository_change_management(request,param4):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/change_depository_result.html',
        {
            'username':param4,
            'message2':'LCY Changed',
            'year':datetime.now().year,
        }
    )