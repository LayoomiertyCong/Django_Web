from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app.forms import BootstrapAuthenticationForm
from django import forms
from django.utils.translation import ugettext_lazy as _
import pymysql


def connect_into_database():
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='syddbw5200608',db='test', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    cursor=conn.cursor(pymysql.cursors.DictCursor)
    return cursor



# 根据仓库编号查仓库信息
def lc_query_depository_information(request):
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
        Dno = request.POST.get("Dno",None)

    cursor = connect_into_database()

    cursor.execute('select Dtype,Dcapacity,Daddress,Dtel from depository where Dno=%s',Dno)

    if cursor.rowcount>0:
        information=cursor.fetchone()
        assert isinstance(request, HttpRequest)

        Dtype = information['Dtype']
        Dcapacity = information['Dcapacity']
        Daddress = information['Daddress']
        Dtel = information['Dtel']

        return render(
            request,
            'xxx.html',
            {
                # the page
                'year':datetime.now().year,
            }
        )
    elif cursor.rowcount==0:
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'xxx.html',
            {
                # the page
                'year':datetime.now().year,
            }
        )

# 根据生产商编号查询生产商信息
def lc_query_supplier_information(request):
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

    if request.method == 'POST':
        Sno = request.POST.get("Sno",None)
    cursor = connect_into_database()
    cursor.execute('select * from supplier where Sno=%s',Sno)

    if cursor.rowcount>0:
        information=cursor.fetchone()
        assert isinstance(request, HttpRequest)

        Sname = information['Sname']
        Saddress = information['Saddress']
        Stel = information['Stel']
        Spostalcode = information['Spostalcode']
        Scontact = information['Scontact']

        return render(
            request,
            'xxx.html',
            {
                # the page of information
                'year':datetime.now().year
            }
        )
    elif cursor.rowcount==0:
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'xxx.html',
            {
                # the page: no such tuple
                'year':datetime.now().year
            }
        )

# 根据客户编号查询生产商信息
def lc_query_customer_information(request):
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

    if request.method == 'POST':
        Sno = request.POST.get("Cno",None)
    cursor = connect_into_database()
    cursor.execute('select * from customer where Cno=%s',Cno)

    if cursor.rowcount>0:
        information=cursor.fetchone()
        assert isinstance(request, HttpRequest)

        Cname = information['Cname']
        Caddress = information['Caddress']
        Ctel = information['Ctel']
        Cpostalcode = information['Cpostalcode']
        Ccontact = information['Ccontact']

        return render(
            request,
            'xxx.html',
            {
                # the page of information
                'year':datetime.now().year
            }
        )
    elif cursor.rowcount==0:
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'xxx.html',
            {
                # the page: no such tuple
                'year':datetime.now().year
            }
        )


# 根据运单号查询运单信息
def lc_query_waybill_information(request):
    '''
        input:
            运单号 Wno
        output:
            订单号 Ono
            负责物流中心编号 Lno
            客户编号 Cno
    '''

    if request.method == 'POST':
        Wno = request.POST.get("Wno",None)
    cursor = connect_into_database()
    cursor.execute('select * from waybill where Wno=%s',Wno)

    if cursor.rowcount>0:
        information=cursor.fetchone()
        assert isinstance(request, HttpRequest)

        Ono = information['Ono']
        Lno = information['Lno']
        Cno = information['Cno']

        return render(
            request,
            'xxx.html',
            {
                # the page of information
                'year':datetime.now().year
            }
        )
    elif cursor.rowcount==0:
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'xxx.html',
            {
                # the page: no such tuple
                'year':datetime.now().year
            }
        )


# 根据订单号查询订单信息
def lc_query_order_information(request):
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

    if request.method == 'POST':
        Ono = request.POST.get("Ono",None)
    cursor = connect_into_database()
    cursor.execute('select * from order where Ono=%s',Ono)

    if cursor.rowcount>0:
        information=cursor.fetchone()
        assert isinstance(request, HttpRequest)

        Cno = information['Cno']
        Sno = information['Sno']
        Oprice = information['Oprice']
        Oamount = information['Oamount']
        Odate = information['Odate']

        return render(
            request,
            'xxx.html',
            {
                # the page of information
                'year':datetime.now().year
            }
        )
    elif cursor.rowcount==0:
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'xxx.html',
            {
                # the page: no such tuple
                'year':datetime.now().year
            }
        )

# 查询中转信息
# Attention 这里涉及到多个元组的fetch
def lc_query_transfer_information(request):
    '''
        input:
            运单号 Wno
        output:
            到达仓库编号 Dno
            进库时间 Ttime
    '''
    if request.method == 'POST':
        Wno = request.POST.get("Wno",None)
    cursor = connect_into_database()
    cursor.execute('select * from transer where Ono=%s',Ono)

    if cursor.rowcount>0:
        tuplelist = cursor.fetchall()
        assert isinstance(request, HttpRequest)

        Dnolist = []
        Ttimelist = []

        for information in tuplelist:
            Dnolist.append(information['Dno'])
            Ttimelist.append(information['Ttime'])

        return render(
            request,
            'xxx.html',
            {
                # the page of information
                'year':datetime.now().year
            }
        )
    elif cursor.rowcount==0:
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'xxx.html',
            {
                # the page: no such tuple
                'year':datetime.now().year
            }
        )


# 根据仓库编号查询剩余容量
def lc_query_depository_leftcapacity(request):
    '''
        input:
            仓库编号 Dno
        output:
            剩余容量 LeftCapacity
    '''
    if request.method == 'POST':
        Dno = request.POST.get("Dno",None)
    cursor = connect_into_database()
    cursor.execute('select LeftCapacity from management where Dno=%s',Dno)

    if cursor.rowcount>0:
        information=cursor.fetchone()
        assert isinstance(request, HttpRequest)

        LeftCapacity = information['LeftCapacity']

        return render(
            request,
            'xxx.html',
            {
                # the page of information
                'year':datetime.now().year
            }
        )
    elif cursor.rowcount==0:
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'xxx.html',
            {
                # the page: no such tuple
                'year':datetime.now().year
            }
        )
