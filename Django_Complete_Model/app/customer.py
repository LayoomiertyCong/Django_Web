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
    O_PW=""
    N_PW=""
    RN_PW=""
    '''
        input 
            新密码 PW_new
    '''
    if request.method == 'POST':
        O_PW = request.POST.get("o_pw",None)
        N_PW = request.POST.get("n_pw",None)
        RN_PW = request.POST.get("rn_pw",None)
    cursor= ac.connect_into_database()
  #cursor.execute('update user set password = %s where username = %s ',Ono,param2)
    cursor.execute('select password from user where username = %s',param2)
    
    if cursor.rowcount>0:
        information = cursor.fetchone()
        assert isinstance(request,HttpRequest)
        
        password = information['password']

        cursor.close()
        #conn.close()

        if O_PW == password and N_PW == RN_PW:
            cursor1,conn1 = ac.connect_into_database_up()
            cursor1.execute('update user set password = %s where username = %s ',(N_PW,param2))
            if cursor1.rowcount>0:
                cursor1.execute('update user set password = %s where username = %s ',(N_PW,param2))
                conn1.commit()
                conn1.close()
                cursor1.close()
                assert isinstance(request,HttpRequest)
                return render(
                    request,
                    'app/change_password_result.html',
                    {
                        'username':param2,
                        'message1':"change the passwword successfully!",
                        'year':datetime.now().year,
                    }
                )
            elif cursor1.rowcount ==0:
                assert isinstance(request,HttpRequest)
                return render(
                    request,
                    'app/about.html',
                    {
                        'title':'Change Error',
                        'message1':"something wrong happened.",
                        'year':datetime.now().year,
                    }
                )
        elif O_PW != password:
            assert isinstance(request,HttpRequest)
            return render(
                request,
                'app/change_password_result.html',
                {
                    'title':'Change Error',
                    'message1':"your password is wrong!please try it again.",
                    'year':datetime.now().year,
                }
            )
        elif N_PW !=RN_PW:
            assert isinstance(request,HttpRequest)
            return render(
                request,
                'app/change_password_result.html',
                {
                    'title':'Change Error',
                    'message1':"first password and second password are different.",
                    'year':datetime.now().year,
                }
            )

    elif cursor.rowcount==0:
        

        cursor.close()
        #conn.close()
        assert isinstance(request,HttpRequest)
        return render(
            request,
            'app/about.html',
            {
                'title':'Change Error',
                'message1':"update unsucessfully",
                'year':datetime.now().year,
            }
        )
    
def customer_query_supplier(request,param2):
    Sname=""
    '''
        input：
            生产商姓名 Sname
        output：
            生产商编号 Sno
            生产商姓名 Sname
            生产商地址 Saddress
            生产商电话 Stel
            生产商邮编 Spostalcode
            生产商联系人 Scontact
    '''
    if request.method == 'POST':
        Sname = request.POST.get("Sname",None)
    cursor= ac.connect_into_database()
    cursor.execute('select * from supplier where supplier.Sname=%s', Sname)
    if cursor.rowcount>0:
        result = ""
        result = result + "Sno" + "\t\t" + "Sname" + "\t\t" + "Saddress" + "\t\t"+ "Stel" + "\t\t"+"Spostalcode"+"\t\t"+"Scontact"+"\t\t\n"
        information = cursor.fetchone()
        #assert isinstance(request, HttpRequest)

        Sno = information['Sno']
        Sname = information['Sname']
        Saddress = information['Saddress']
        Stel = information['Stel']
        Spostalcode = information['Spostalcode']
        Scontact = information['Scontact']

        result = result + Sno + "\t\t" + Sname + "\t\t" + Saddress + "\t\t"+ Stel + "\t\t"+Spostalcode+"\t\t"+Scontact+"\t\t\n"


        cursor.close()
        #conn.close()
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'app/query_customer_result.html',
            {
                'username':param2,
                'message1':"Query Result",
                'message2':result,
                'year':datetime.now().year,
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
    
def customer_query_order(request,param2):
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
            总量 Oamount
            日期 Odate
    '''
    if request.method == 'POST':
        Ono = request.POST.get("Ono",None)
    cursor= ac.connect_into_database()
    cursor.execute('select customer.Cname, customer.Ctel, customer.Caddress, \
        `order`.Oprice, `order`.Oamount, `order`.Odate from `order`, customer where Ono=%s and `order`.Cno=customer.Cno',Ono)
    order_count = cursor.rowcount

    if order_count>0:
        result = ""
        result = result+"客户名称"+"\t"+"客户联系方式"+"\t"+"客户地址"+"\t"+"总价"+"\t"+"总量"+"\t"+"日期"+"\t\n"
        information=cursor.fetchone()
        #assert isinstance(request, HttpRequest)

        Cname = information['Cname']
        Ctel = information['Ctel']
        Caddress = information['Caddress']
        Oprice = information['Oprice']
        Oamount = information['Oamount']
        Odate = information['Odate']

        result = result + Cname+"\t"+Ctel+"\t"+Caddress+"\t"+str(Oprice)+"\t"+str(Oamount)+"\t"+str(Odate)+"\t\n"

        cursor.close()
        #conn.close()

        cursor2= ac.connect_into_database()
        cursor2.execute('select Gname, Gprice from good, order_good where order_good.Ono=%s \
            and order_good.Gno=good.Gno', Ono)

        if cursor2.rowcount > 0:
            result = result+"货物名称"+"\t"+"货物单价"+"\t\n"
            good_info = cursor2.fetchall()
            Gname = []
            Gprice = []
            for info_dict in good_info: 
                Gname.append(info_dict['Gname'])
                Gprice.append(info_dict['Gprice'])
                result =result+info_dict['Gname']+"\t"+str(info_dict['Gprice'])+"\t\n"

        cursor2.close()
        #conn2.close()

        assert isinstance(request, HttpRequest)
        return render(
            request,
            'app/query_customer_result.html',
            {
                'username':param2,
                'message1':"Query Result",
                'message2':result,
                'year':datetime.now().year,
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

def customer_query_waybill(request,param3):
    Wno=""
    '''
        input：
            运单号 Wno
        output：
            订单号 Ono
            物流中心名称 Lname
            物流中心地址 Laddress
            物流中心邮编 Lpostalcode
            物流中心联系方式 Ltel
            中转信息：
            进库时间 Ttime
            到达仓库的地址 Daddress
    '''
    if request.method == 'POST':
        Wno = request.POST.get("Wno",None)
    cursor = ac.connect_into_database()
    cursor.execute('select waybill.Ono, logisticcenter.Lname, logisticcenter.Laddress, logisticcenter.Lpostalcode,\
        logisticcenter.Ltel from waybill, logisticcenter where waybill.Wno=%s and logisticcenter.Lno=waybill.Lno',Wno)
    waybill_corsorcount = cursor.rowcount
    if waybill_corsorcount >0:
        result =""
        result = result+"Ono"+"\t\t"+"Lname"+"\t\t"+"Laddress"+"\t\t"+"Lpostalcode"+"\t\t"+"Ltel"+"\t\t\n"
        information = cursor.fetchone()
        #assert isinstance(request, HttpRequest)

        Ono = information['Ono']
        Lname = information['Lname']
        Laddress = information['Laddress']
        Lpostalcode = information['Lpostalcode']
        Ltel = information['Ltel']

        result = result+Ono+"\t\t"+Lname+"\t\t"+Laddress+"\t\t"+Lpostalcode+"\t\t"+Ltel+"\t\t\n"


        cursor.close()
        #conn.close()

        cursor2 = ac.connect_into_database()
        cursor2.execute('select Ttime, Daddress from transfer, depository where transfer.Wno=%s \
            and depository.Dno=transfer.Dno',Wno)
        result = result + "transfer information：\n"
        if cursor2.rowcount > 0:
            transfer_info = cursor2.fetchall()
            Ttime = []
            Daddress = []
            for info_dict in transfer_info: 
                Ttime.append(info_dict['Ttime'])
                Daddress.append(info_dict['Daddress'])
                result = result + str(info_dict['Ttime']) +"："+info_dict['Daddress']+"\n" 
        cursor2.close()
        #conn2.close()

        # TODO: transfer列表转字符串
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'app/query_customer_result.html',
            {
                'username':param3,
                'message1':"Query Result",
                'message2':result,
                'year':datetime.now().year,
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

def customer_query_deliverman(request,param3):
    Wno=""
    '''
        input:
            运单号Wno
        output:
            配送员信息：
                配送员编号 DMno
                配送员姓名 DMname
                配送员性别 DMsex
                配送员电话 DMtel
    '''
    if request.method == 'POST':
        Wno = request.POST.get("Wno",None)
    cursor = ac.connect_into_database()
    cursor.execute('select deliverman.DMno, deliverman.DMname, deliverman.DMsex, \
        deliverman.DMtel from deliverman,waybill,distribution where \
            waybill.Wno = %s and distribution.Wno= waybill.Wno',Wno)
    count1 = cursor.rowcount

    if count1>0:
        result =""
        result = result+"配送员编号"+"\t"+"配送员姓名"+"\t"+"配送员你性别"+"\t"+"配送员电话"+"\t\n"
        information = cursor.fetchone()
        
        DMno = information['DMno']
        DMname = information['DMname']
        DMsex = information['DMsex']
        DMtel = information['DMtel']

        result+= information['DMno']+"\t"+information['DMname']+"\t"+information['DMsex']+"\t"+information['DMtel']+"\n"


        cursor.close()
        #coon.close()

        assert isinstance(request, HttpRequest)
        return render(
            request,
            'app/query_customer_result.html',
            {
                'username':param3,
                'message1':"Query Result",
                'message2':result,
                'year':datetime.now().year,
            }
        )
    elif count1==0:
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

def customer_query_all_order(request,param3):
    '''
        input：
            Cno
        output:
            所有订单的订单号 Ono
    '''

    cursor= ac.connect_into_database()
    cursor.execute('select `order`.Ono from `order`,customer where \
        customer.Cno = %s and `order`.Cno = customer.Cno', param3)
    count1 = cursor.rowcount

    if count1>0:
        result = ""
        result+="订单号 \n"

        info_list = cursor.fetchall()
        
        Ono = []

        cursor.close()
        #conn.close()

        for information in info_list:
            Ono.append(information['Ono'])
            result+=information['Ono']+ "\n"

        assert isinstance(request, HttpRequest)
        return render(
            request,
            'app/query_customer_result.html',
            {
                'username':param3,
                'message1':"Query Result",
                'message2':result,
                'year':datetime.now().year,
            }
        )
    elif count1==0:
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

    
