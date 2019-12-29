from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app.forms import BootstrapAuthenticationForm
from django import forms
from django.utils.translation import ugettext_lazy as _
import pymysql
import app.connectsql as ac

def logisticcenter_query(request,param1):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/query_logisticcenter.html',
        {
            'username':param1,
            'title':'Query',
            'message':'Go Query',
            'year':datetime.now().year,
        }
    )

def lc_query_depository_information(request,param1,param2):
    Dno=""
    '''
        input:
            仓库编号 Dno
        output:
            仓库性质 Dtype
            仓库总量 Dcapacity
            仓库地址 Daddress
            仓库电话 Dtel
    '''
    if request.method == 'POST':
        Dno= request.POST.get("Dno",None)

    cursor = ac.connect_into_database()

    cursor.execute('select Dtype,Dcapacity,Daddress,Dtel from depository where Dno=%s',Dno)
    if cursor.rowcount>0:
        information=cursor.fetchone()
        

        Dtype = information['Dtype']
        Dcapacity = information['Dcapacity']
        Daddress = information['Daddress']
        Dtel = information['Dtel']
        result="Dtype:"+Dtype+"\n"+"Dcapacity:"+str(Dcapacity)+"\n"+"Daddress:"+Daddress+"\n"+"Dtel:"+Dtel
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'app/query_logisticcenter_result.html',
            {
                'username':param1,
                'message1':"Query Result:",
                'message2':result,
                'year':datetime.now().year,
            }
        )
    elif cursor.rowcount==0:
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'app/about.html',
            {
                'title':'Are you szs?',
                'message':'There is no such depository.',
                'year':datetime.now().year,
            }
        )
    

def lc_query_supplier_information(request,param):
    assert isinstance(request, HttpRequest)
    return render(
            request,
            'app/query_logisticcenter_result.html',
            {
                'username':param,
                'message1':"LCY_Logistic",
                'message2':"LCY_Logistic",
                'year':datetime.now().year,
            }
        )

def lc_query_customer_information(request,param):
    assert isinstance(request, HttpRequest)
    return render(
            request,
            'app/query_logisticcenter_result.html',
            {
                'username':param,
                'message1':"LCY_Logistic",
                'message2':"LCY_Logistic",
                'year':datetime.now().year,
            }
        )

def lc_query_waybill_information(request,param):
    assert isinstance(request, HttpRequest)
    return render(
            request,
            'app/query_logisticcenter_result.html',
            {
                'username':param,
                'message1':"LCY_Logistic",
                'message2':"LCY_Logistic",
                'year':datetime.now().year,
            }
        )

def lc_query_order_information(request,param):
    assert isinstance(request, HttpRequest)
    return render(
            request,
            'app/query_logisticcenter_result.html',
            {
                'username':param,
                'message1':"LCY_Logistic",
                'message2':"LCY_Logistic",
                'year':datetime.now().year,
            }
        )

def lc_query_transfer_information(request,param):
    assert isinstance(request, HttpRequest)
    return render(
            request,
            'app/query_logisticcenter_result.html',
            {
                'username':param,
                'message1':"LCY_Logistic",
                'message2':"LCY_Logistic",
                'year':datetime.now().year,
            }
        )

def lc_query_depository_leftcapacity(request,param):
    assert isinstance(request, HttpRequest)
    return render(
            request,
            'app/query_logisticcenter_result.html',
            {
                'username':param,
                'message1':"LCY_Logistic",
                'message2':"LCY_Logistic",
                'year':datetime.now().year,
            }
        )

def lc_query_deliverman_information(request,param):
    assert isinstance(request, HttpRequest)
    return render(
            request,
            'app/query_logisticcenter_result.html',
            {
                'username':param,
                'message1':"LCY_Logistic",
                'message2':"LCY_Logistic",
                'year':datetime.now().year,
            }
        )




def logisticcenter_update(request,param4):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/update_logisticcenter.html',
        {
            'username':param4,
            'title':'Logisticcenter Update',
            'message':'UpdateGo',
            'year':datetime.now().year,
        }
    )


def lc_update_supplier(request,param5):
    assert isinstance(request, HttpRequest)
    return render(
            request,
            'app/update_logisticcenter_result.html',
            {
                'username':param5,
                'message2':"LCY Updated Logistics S",
                'year':datetime.now().year,
            }
        )


def lc_update_customer(request,param5):
    assert isinstance(request, HttpRequest)
    return render(
            request,
            'app/update_logisticcenter_result.html',
            {
                'username':param5,
                'message2':"LCY Updated Logistics C",
                'year':datetime.now().year,
            }
        )

def lc_update_depository(request,param5):
    assert isinstance(request, HttpRequest)
    return render(
            request,
            'app/update_logisticcenter_result.html',
            {
                'username':param5,
                'message2':"LCY Updated Logistics C",
                'year':datetime.now().year,
            }
        )
def lc_update_waybill(request,param5):
    assert isinstance(request, HttpRequest)
    return render(
            request,
            'app/update_logisticcenter_result.html',
            {
                'username':param5,
                'message2':"LCY Updated Logistics W",
                'year':datetime.now().year,
            }
        )

def lc_update_order(request,param5):
    assert isinstance(request, HttpRequest)
    return render(
            request,
            'app/update_logisticcenter_result.html',
            {
                'username':param5,
                'message2':"LCY Updated Logistics O",
                'year':datetime.now().year,
            }
        )

def lc_update_order_good(request,param5):
    assert isinstance(request, HttpRequest)
    return render(
            request,
            'app/update_logisticcenter_result.html',
            {
                'username':param5,
                'message2':"LCY Updated Logistics og",
                'year':datetime.now().year,
            }
        )

def lc_update_route(request,param5):
    assert isinstance(request, HttpRequest)
    return render(
            request,
            'app/update_logisticcenter_result.html',
            {
                'username':param5,
                'message2':"LCY Updated Logistics r",
                'year':datetime.now().year,
            }
        )

def logisticcenter_change(request,param4):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/change_logisticcenter.html',
        {
            'username':param4,
            'title':'Logisticcenter Change',
            'message':'ChangeGo',
            'year':datetime.now().year,
        }
    )
def lc_change_management(request,param5):
    assert isinstance(request, HttpRequest)
    return render(
            request,
            'app/change_logisticcenter_result.html',
            {
                'username':param5,
                'message2':"LCY Changed Logistics m",
                'year':datetime.now().year,
            }
        )

def logisticcenter_delete(request,param4):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/delete_logisticcenter.html',
        {
            'username':param4,
            'title':'Logisticcenter Delete',
            'message':'DeleteGo',
            'year':datetime.now().year,
        }
    )

def lc_delete_customer(request,param5):
    assert isinstance(request, HttpRequest)
    return render(
            request,
            'app/delete_logisticcenter_result.html',
            {
                'username':param5,
                'message2':"LCY Delete Logistics c",
                'year':datetime.now().year,
            }
        )

def lc_delete_supplier(request,param5):
    assert isinstance(request, HttpRequest)
    return render(
            request,
            'app/delete_logisticcenter_result.html',
            {
                'username':param5,
                'message2':"LCY Delete Logistics s",
                'year':datetime.now().year,
            }
        )

def lc_delete_depository(request,param5):
    assert isinstance(request, HttpRequest)
    return render(
            request,
            'app/delete_logisticcenter_result.html',
            {
                'username':param5,
                'message2':"LCY Delete Logistics d",
                'year':datetime.now().year,
            }
        )