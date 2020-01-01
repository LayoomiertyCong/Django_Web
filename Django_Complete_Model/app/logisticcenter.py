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

def lc_query_depository_information(request,param1):
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
    '''
        input:
            生产商编号 Sno
        output:
            生产商名称 Sname
            生产商地址 Saddress
            生产商电话 Stel
            生产商邮编 Spostalcode
            生产商联系人 Scontact
    '''

    Sno = ""
    if request.method == 'POST':
        Sno = request.POST.get("Sno",None)
    cursor = ac.connect_into_database()
    cursor.execute('select * from supplier where Sno=%s',Sno)

    if cursor.rowcount>0:
        information=cursor.fetchone()
        assert isinstance(request, HttpRequest)

        Sname = information['Sname']
        Saddress = information['Saddress']
        Stel = information['Stel']
        Spostalcode = information['Spostalcode']
        Scontact = information['Scontact']

        result = "Sname:"+Sname+'\n' + "Saddress:"+Saddress+'\n' + "Stel:"+Stel+'\n' + "Spostalcode:"+Spostalcode+'\n' + "Scontact:"+Scontact+'\n'

        return render(
            request,
            'app/query_logisticcenter_result.html',
            {
                'username':param,
                'message1':"Query Result",
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
    

def lc_query_customer_information(request,param):
    '''
        input:
            客户编号 Cno
        output:
            客户名称 Cname
            客户地址 Caddress
            客户电话 Ctel
            客户邮编 Cpostalcode
            客户联系人 Ccontact
    '''
    Cno = ""
    if request.method == 'POST':
        Cno = request.POST.get("Cno",None)
    cursor = ac.connect_into_database()
    cursor.execute('select * from customer where Cno=%s',Cno)

    if cursor.rowcount>0:
        information=cursor.fetchone()
        assert isinstance(request, HttpRequest)

        Cname = information['Cname']
        Caddress = information['Caddress']
        Ctel = information['Ctel']
        Cpostalcode = information['Cpostalcode']
        Ccontact = information['Ccontact']

        result="Cname:"+Cname+'\n'+"Caddress:"+Caddress+'\n'+"Ctel:"+Ctel+'\n'+"Cpostalcode:"+Cpostalcode+'\n'+"Ccontact:"+Ccontact+'\n'

        return render(
            request,
            'app/query_logisticcenter_result.html',
            {
                'username':param,
                'message1':"Query Result",
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

def lc_query_waybill_information(request,param):
    '''
        input:
            运单号 Wno
        output:
            订单号 Ono
            负责物流中心编号 Lno
            客户编号 Cno
    '''
    Wno = ""
    if request.method == 'POST':
        Wno = request.POST.get("Wno",None)
    cursor = ac.connect_into_database()
    cursor.execute('select * from waybill where Wno=%s',Wno)

    if cursor.rowcount>0:
        information=cursor.fetchone()
        assert isinstance(request, HttpRequest)

        Ono = information['Ono']
        Lno = information['Lno']
        Cno = information['Cno']

        result="Ono:"+Ono+'\n'+"Lno:"+Lno+'\n'+"Cno:"+Cno+'\n'

        return render(
            request,
            'app/query_logisticcenter_result.html',
            {
                'username':param,
                'message1':"Query Result",
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

def lc_query_order_information(request,param):
    '''
        input:
            订单号 Ono
        output:
            客户编号 Cno
            生产商编号 Sno
            总价 Oprice
            总量 Oamount
            日期 Odate
    '''
    Ono = ""
    if request.method == 'POST':
        Ono = request.POST.get("Ono",None)
    cursor = ac.connect_into_database()
    cursor.execute('select * from `order` where Ono=%s',Ono)

    if cursor.rowcount>0:
        information=cursor.fetchone()
        assert isinstance(request, HttpRequest)

        Cno = information['Cno']
        Sno = information['Sno']
        Oprice = information['Oprice']
        Oamount=information['Oamount']
        Odate = information['Odate']

        result="Cno:"+Cno+'\n'+"Sno:"+Sno+'\n'+"Oprice:"+str(Oprice)+'\n'+"Oamount:"+str(Oamount)+'\n'+"Odate:"+str(Odate)+'\n'

        return render(
            request,
            'app/query_logisticcenter_result.html',
            {
                'username':param,
                'message1':"Query Result",
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

def lc_query_transfer_information(request,param):
    '''
        input:
            运单号 Wno
        output:
            到达仓库编号 Dno
            进库时间 Ttime
    '''
    Wno = ""
    if request.method == 'POST':
        Wno = request.POST.get("Wno",None)
    cursor = ac.connect_into_database()
    cursor.execute('select * from transfer where Wno=%s order by Ttime',Wno)

    if cursor.rowcount>0:
        tuplelist = cursor.fetchall()
        assert isinstance(request, HttpRequest)

        Dnolist = []
        Ttimelist = []

        result = ""

        for information in tuplelist:
            result += "Dno:%s   Ttime:%s\n"%(information['Dno'],str(information['Ttime']))

        assert isinstance(request, HttpRequest)
        return render(
            request,
            'app/query_logisticcenter_result.html',
            {
                'username':param,
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

def lc_query_depository_leftcapacity(request,param):
    
    '''
        input:
            仓库编号 Dno
        output:
            剩余容量 LeftCapacity
    '''
    if request.method == 'POST':
        Dno = request.POST.get("Dno",None)
    cursor = ac.connect_into_database()
    cursor.execute('select LeftCapacity from management where Dno=%s',Dno)

    if cursor.rowcount>0:
        information=cursor.fetchone()
        assert isinstance(request, HttpRequest)

        LeftCapacity = information['LeftCapacity']
        result="LeftCapacity:"+str(LeftCapacity)+'\n'
        return render(
            request,
            'app/query_logisticcenter_result.html',
            {
                'username':param,
                'message1':"Query Result",
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

def lc_query_deliverman_information(request,param):
    '''
        input:
            配货员编号 DMno
        output:
            姓名 DMname
            性别 Dmgender
            联系方式 Dmtel
    '''
    DMno = ""
    if request.method == 'POST':
        DMno = request.POST.get("DMno",None)
    cursor = ac.connect_into_database()
    cursor.execute('select * from deliverman where DMno=%s',DMno)

    if cursor.rowcount>0:
        information=cursor.fetchone()
        assert isinstance(request, HttpRequest)

        DMname = information['DMname']
        DMsex = information['DMsex']
        DMtel = information['DMtel']

        result="DMname:"+DMname+"\n"+"DMgender:"+DMsex+"\n"+"DMtel:"+DMtel
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'app/query_logisticcenter_result.html',
            {
                'username':param,
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

def lc_query_distribution_information(request,param1):
    '''
        input:
            运单号 Wno
        output:
            配货员编号 DMno
            收货人姓名 Cname
            收货人联系方式 Ctel
            运货地址 Caddress
    '''
    Wno = ""
    if request.method == 'POST':
        Wno = request.POST.get("Wno",None)
    cursor = ac.connect_into_database()
    cursor.execute('select * from distribution where Wno=%s',Wno)

    if cursor.rowcount>0:
        information=cursor.fetchone()
        assert isinstance(request, HttpRequest)

        DMno = information['DMno']
        Cname = information['Cname']
        Ctel = information['Ctel']
        Caddress = information['Caddress']

        result="DMno:"+DMno+"\n"+"Cname"+Cname+"\n"+"Ctel:"+Ctel+"\n"+"Caddress:"+Caddress
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'app/query_logisticcenter_result.html',
            {
                'username':param,
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