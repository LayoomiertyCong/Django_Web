from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app.forms import BootstrapAuthenticationForm
from django import forms
from django.utils.translation import ugettext_lazy as _
import pymysql
import app.connectsql as ac
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


# 根据订单号查询用户信息
def sup_query_customer_information(request,param2):
    Ono=""
    '''
        input:
            订单号 Ono
        output:
            客户名称 Cname
            客户地址 Caddress
            客户电话 Ctel
            客户邮编 Cpostalcode
            客户联系人 Ccontact
    '''
    if request.method == 'POST':
        Ono = request.POST.get("Ono",None)
    cursor = ac.connect_into_database()
    cursor.execute('select customer.* from customer, `order` where `order`.Ono=%s and `order`.Cno=customer.Cno',Ono)
    if cursor.rowcount>0:
        information=cursor.fetchone()

        Cname = information['Cname']
        Caddress = information['Caddress']
        Ctel = information['Ctel']
        Cpostalcode = information['Cpostalcode']
        Ccontact = information['Ccontact']

        cursor.close()

        result = "客户姓名： " + Cname + "\n客户地址： " + Caddress + "\n客户电话： " + Ctel + \
            "\n客户邮编： " + Cpostalcode + "\n客户联系人： " + Ccontact +'\n'
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'app/query_supplier_result.html',  # TODO: 更改html
            {
                # the page of information
                'message1': "Query Result:",
                'message2': result,
                'year':datetime.now().year
            }
        )
    elif cursor.rowcount==0:
        cursor.close()
        #conn.close()
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'app/about.html',   # TODO: 更改html
            {
                # the page: no such tuple
                'title': "Query Error",
                'message': "There is no such tuple",
                'year':datetime.now().year
            }
        )

def sup_query_waybill_information(request,param3):
    Wno=""
    '''
        input:
            运单号 Wno
        output:
            订单号 Ono
            负责物流中心信息 
                物流中心名称 Lname
                物流中心地址 Laddress
                物流中心邮编 Lpostalcode
                物流中心联系方式 Ltel
            中转信息 
                进库时间 Ttime，到达仓库地址(具体到省市) Daddress
    '''
    if request.method == 'POST':
        Wno = request.POST.get("Wno",None)
    cursor = ac.connect_into_database()
    cursor.execute('select waybill.Ono, logisticcenter.Lname, logisticcenter.Laddress, logisticcenter.Lpostalcode,\
        logisticcenter.Ltel from waybill, logisticcenter where waybill.Wno=%s and logisticcenter.Lno=waybill.Lno',Wno)
    waybill_corsorcount = cursor.rowcount
    if waybill_corsorcount>0:
        information=cursor.fetchone()
        #assert isinstance(request, HttpRequest)

        Ono = information['Ono']
        Lname = information['Lname']
        Laddress = information['Laddress']
        Lpostalcode = information['Lpostalcode']
        Ltel = information['Ltel']

        cursor.close()
        

        waybill_info = "该运单对应的订单号为： " + Ono + "\n\t" + Lname + " 联系方式： " + Ltel + "\n\t邮编： " \
            + Lpostalcode + " 总部地址： " + Laddress + '\n\n'

        cursor2 = ac.connect_into_database()
        cursor2.execute('select Ttime, Daddress from transfer, depository where transfer.Wno=%s \
            and depository.Dno=transfer.Dno order by Ttime desc',Wno)
        if cursor2.rowcount > 0:
            transfer_info = cursor2.fetchall()
            Ttime = []
            Daddress = []
            for info_dict in transfer_info: 
                Ttime.append(str(info_dict['Ttime']))
                Daddress.append(info_dict['Daddress'])

            cursor2.close()

            # trans-info:
            trans_info = "快递信息：该快递已于\n\t"
            for i in range(len(Ttime)):
                trans_info += Ttime[i] + "到达 " + Daddress[i] + '\n\t'

            result = waybill_info + trans_info
            assert isinstance(request, HttpRequest)
            return render(
                request,
                'app/query_supplier_result.html',  # TODO: 更改html
                {
                    # the page of information
                    'message1': "Query Result:",
                    'message2': result,
                    'year':datetime.now().year
                }
            )
    elif cursor.rowcount==0:
        cursor.close()
        #conn.close()
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'app/about.html',   # TODO: 更改html
            {
                # the page: no such tuple
                'title': "Query Error",
                'message': "There is no such tuple",
                'year':datetime.now().year
            }
        )



def sup_query_order_information(request,param3):
    Ono=""
    '''
        input:
            订单号 Ono
        output:
            客户信息 
                客户名称 Cname
                客户联系方式 Ctel
                客户地址 Caddress
            货物信息 
                货物名称 Gname
                单价 Gprice
            总价 Oprice
            日期 Odate
    '''
    if request.method == 'POST':
        Ono = request.POST.get("Ono",None)

    cursor= ac.connect_into_database()
    cursor.execute('select customer.Cname, customer.Ctel, customer.Caddress, \
        `order`.Oprice, `order`.Odate from `order`, customer where Ono=%s \
            and `order`.Cno=customer.Cno',Ono)
    order_count = cursor.rowcount
    if order_count>0:
        information=cursor.fetchone()
        assert isinstance(request, HttpRequest)

        Cname = information['Cname']
        Ctel = information['Ctel']
        Caddress = information['Caddress']
        Oprice = str(information['Oprice'])
        Odate = str(information['Odate'])

        cursor.close()
        #conn.close()

        order_info_str = "订单号 ：" + Ono + "详细信息如下：\n\t客户基本信息： \n\t\t客户姓名： " + Cname + \
            "\n\t\t客户电话： " + Ctel + "\n\t\t客户地址： " + Caddress + "\n\t订单信息： \n\t\t订单总价： " + \
                Oprice + "元\n\t\t订单日期: " + Odate + "\n\n"  

        cursor2 = ac.connect_into_database()
        cursor2.execute('select Gname, Gprice from good, order_good where order_good.Ono=%s \
            and order_good.Gno=good.Gno', Ono)
        if cursor2.rowcount > 0:
            good_info = cursor2.fetchall()
            Gname = []
            Gprice = []
            for info_dict in good_info: 
                Gname.append(str(info_dict['Gname']))
                Gprice.append(str(info_dict['Gprice']))

        cursor2.close()
        #conn2.close()

        good_info_str = "\t货物信息：\n\t\t"
        for i in range(len(Gname)):
            good_info_str += "货物名称： " + Gname[i] + " 数量： " + Gprice[i] + "\n\t\t"

        result = order_info_str + good_info_str
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'app/query_supplier_result.html',  # TODO: 更改html
            {
                # the page of information
                'message1': "Query Result:",
                'message2': result,
                'year':datetime.now().year
            }
        )
    elif cursor.rowcount==0:
        cursor.close()
        #conn.close()
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'app/about.html',   # TODO: 更改html
            {
                # the page: no such tuple
                'title': "Query Error",
                'message': "There is no such tuple",
                'year':datetime.now().year
            }
        )

    
# 查询最近三个月内的订单信息
def sup_query_recent_order_by_time(request,param3):
    '''
        output:
            客户信息 
                客户名称 Cname
                客户联系方式 Ctel
                客户地址 Caddress
            货物信息 
                货物名称 Gname
                单价 Gprice
            总价 Oprice
            总量 Oamount
            日期 Odate
    '''
    # TODO: get Sno

    cursor = ac.connect_into_database()
    cursor.execute('select `order`.Ono, customer.Cname, customer.Ctel, customer.Caddress, \
        `order`.Oprice, `order`.Oamount, `order`.Odate from `order`, customer where \
            `order`.Sno=%s and `order`.Cno=customer.Cno and\
            DATE_SUB(CURDATE(), INTERVAL 3 month) <= date(Odate)', param3)
    order_count = cursor.rowcount

    # order_count为订单总数
    if order_count>0:
        info_list=cursor.fetchall()
        #assert isinstance(request, HttpRequest)
        Ono = []
        Cname = []
        Ctel = []
        Caddress = []
        Oprice = []
        Oamount = []
        Odate = []

        result = '最近三个月共有 '+ str(order_count) +" 条订单记录: \n" 

        for information in info_list:
            Ono.append(information['Ono'])
            Cname.append(information['Cname'])
            Ctel.append(information['Ctel'])
            Caddress.append(information['Caddress'])
            Oprice.append(information['Oprice'])
            Oamount.append(information['Oamount'])
            Odate.append(information['Odate'])

            order_info_str = "订单号 ：" + information['Ono'] + "\n\t订单总价： " + \
                str(information['Oprice']) + "元, 订单日期: " + str(information['Odate']) + ", 客户姓名： " + information['Cname'] + \
            ", 客户电话： " + information['Ctel'] + ", 客户地址： " + information['Caddress'] + "\n"

            result += order_info_str
            cursor.close()
            #conn.close()

            cursor2= ac.connect_into_database()
            cursor2.execute('select Gname, Gprice from good, order_good where order_good.Ono=%s \
                and order_good.Gno=good.Gno', information['Ono'])

            if cursor2.rowcount > 0:
                good_info = cursor2.fetchall()
                Gname = []
                Gprice = []
                for info_dict in good_info: 
                    Gname.append(info_dict['Gname'])
                    Gprice.append(str(info_dict['Gprice']))

                good_info_str = "\t货物信息： "

                for i in range(len(Gname)):
                    good_info_str += "货物名称： " + Gname[i] + " 数量： " + Gprice[i] + ", "

                good_info_str += '\n\n'

            cursor2.close()
            #conn2.close()
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'app/query_supplier_result.html',  # TODO: 更改html
            {
                # the page of information
                'message1': "Query Result:",
                'message2': result,
                'year':datetime.now().year
            }
        )
    elif cursor.rowcount==0:
        cursor.close()
        #conn.close()
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'app/about.html',   # TODO: 更改html
            {
                # the page: no such tuple
                'title': "Query Error",
                'message': "There is no such tuple",
                'year':datetime.now().year
            }
        )
    

def sup_query_recent_waybill_by_time(request,param3):
    '''
        output:
            运单号 Wno
            订单号 Ono
            负责物流中心信息 
                物流中心名称 Lname
                物流中心地址 Laddress
                物流中心邮编 Lpostalcode
                物流中心联系方式 Ltel
            中转信息 
                进库时间 Ttime，到达仓库地址(具体到省市) Daddress
    '''
    # TODO: get Sno from parameters

    cursor= ac.connect_into_database()
    cursor.execute('select waybill.Wno, waybill.Ono, logisticcenter.Lname, logisticcenter.Laddress, \
        logisticcenter.Lpostalcode, logisticcenter.Ltel from waybill, logisticcenter, `order` where \
            logisticcenter.Lno=waybill.Lno and waybill.Ono=`order`.Ono and `order`.Sno=%s and \
                DATE_SUB(CURDATE(), INTERVAL 3 month) <= date(`order`.Odate)', param3)
    waybill_count = cursor.rowcount
    if waybill_count>0:
        info_list=cursor.fetchall()
        #assert isinstance(request, HttpRequest)
        Wno = []
        Ono = []
        Lname = []
        Laddress = []
        Lpostalcode = []
        Ltel = []

        result = '最近三个月共有 '+ str(waybill_count) +" 条订单记录: \n" 

        for information in info_list:
            Wno.append(information['Wno'])
            Ono.append(information['Ono'])
            Lname.append(information['Lname'])
            Laddress.append(information['Laddress'])
            Lpostalcode.append(information['Lpostalcode'])
            Ltel.append(information['Ltel'])

            cursor.close()
            #conn.close()

            waybill_info = "运单号： "+ information['Wno'] +", 订单号： " + information['Ono'] + \
                "\n\t" + information['Lname'] + ", 联系方式： " + information['Ltel'] + \
                    ", 邮编： " + information['Lpostalcode'] + ", 总部地址： " + information['Laddress'] + '\n\t'

            result += waybill_info

            cursor2 = ac.connect_into_database()
            cursor2.execute('select Ttime, Daddress from transfer, depository where transfer.Wno=%s \
                and depository.Dno=transfer.Dno order by Ttime desc', information['Wno'])
            if cursor2.rowcount > 0:
                transfer_info = cursor2.fetchall()
                Ttime = []
                Daddress = []
                for info_dict in transfer_info: 
                    Ttime.append(str(info_dict['Ttime']))
                    Daddress.append(info_dict['Daddress'])

            cursor2.close()
            #conn2.close()

            result += "\t该运单目前于"+Ttime[0]+"到达："+Daddress[0] + "\n\n"
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'app/query_supplier_result.html',  # TODO: 更改html
            {
                # the page of information
                'message1': "Query Result:",
                'message2': result,
                'year':datetime.now().year
            }
        )
    elif cursor.rowcount==0:
        cursor.close()
        #conn.close()
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'app/about.html',   # TODO: 更改html
            {
                # the page: no such tuple
                'title': "Query Error",
                'message': "There is no such tuple",
                'year':datetime.now().year
            }
        )
    
