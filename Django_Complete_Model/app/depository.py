from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app.forms import BootstrapAuthenticationForm
from django import forms
from django.utils.translation import ugettext_lazy as _
import pymysql
import app.connectsql as ac

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
# 直接查询仓库信息
def depository_query_own(request,param2):
    '''
        output:
            仓库编号 Dno
            仓库地址 Daddress
            仓库容量 Dcapacity
            仓库联系方式 Dtel
            所属物流中心 Lname
            仓库类型 Dtype
    '''
    # TODO: 获得仓库管理员编号

    cursor = ac.connect_into_database()
    cursor.execute('select depository.Dtel, depository.Dtype,depository.Dno, depository.Daddress, depository.Dcapacity, management.LeftCapacity, logisticcenter.Lname\
         from depository, management, logisticcenter where \
            management.Dno=%s and depository.Lno=logisticcenter.Lno and depository.Dno=management.Dno', param2)
    if cursor.rowcount>0:
        information=cursor.fetchone()
        assert isinstance(request, HttpRequest)

        Dno = information['Dno']
        Daddress = information['Daddress']
        Dcapacity = information['Dcapacity']
        LeftCapacity = information['LeftCapacity']
        Lname = information['Lname']
        Dtel = information['Dtel']
        Dtype = information['Dtype']

        cursor.close()

        result = "仓库编号： " + Dno + "\n仓库地址： " + Daddress + "\n仓库容量： " + str(Dcapacity) + \
            "\n剩余容量; "+ str(LeftCapacity) +"\n所属物流中心： " + Lname + "\n仓库联系方式： " + Dtel +'\n仓库类型： ' + Dtype + '\n'

        assert isinstance(request, HttpRequest)
        return render(
            request,
            'app/query_depository_result.html',
            {
                'username':param2,
                'message1':"Query Result",
                'message2':result,
                'year':datetime.now().year,
            }
        )
    elif cursor.rowcount==0:
        cursor.close()
        assert isinstance(request, HttpRequest)

        
        return render(
            request,
            'app/about.html',   # TODO: 更改html
            {
                # the page: no such tuple
                'title':'Are you szs?',
                'message':'There is no such depository.',
                'year':datetime.now().year,
            }
        )
    

# 查询路线图
def dep_query_route_information(request,param2):
    Wno=""
    '''
        input:
            运单号 Wno
        output:
            出发仓库编号 Dano
            到达仓库编号 Dbno
            起点仓库编号 Dstartno
            重点仓库编号 Ddestinyno
    '''

    # TODO: 获得仓库管理员编号Manager

    if request.method == 'POST':
        Wno = request.POST.get("Wno",None)

    startno = Wno[0]
    destinyno = Wno[1]

    cursor = ac.connect_into_database()
    cursor.execute('select Dano, Dbno from Route where Dstartno=%s and Ddestinyno=%s', (startno, destinyno))

    if cursor.rowcount>0:
        infor_list =cursor.fetchall()
    
        Dano_list = []
        Dbno_list = []
        for info in infor_list:
            Dano_list.append(info['Dano'])
            Dbno_list.append(info['Dbno'])
    
        route = [startno]


        while(1):
            for i in range(len(Dano_list)):
                if Dano_list[i] == route[-1]:
                    route.append(Dbno_list[i])
                    break
            if route[-1] == destinyno:
                break

        cursor.close()

        route_graph = "运单号为： "+ Wno +"\n该运单的路线图为： \n"

        for i in range(len(route)):
            route_graph += " -> " + route[i]

         # 获得自己的dno:
        next_dno = ''
        message = ''
        for i in range(len(route)):
            if route[i] == param2 and i < len(route)-1:
                next_dno = route[i+1] 
        if next_dno == '':
            message = "\n已到达终点仓库，请交予配送员进行配送。"  

        cursor3 = ac.connect_into_database()
        cursor3.execute('select Dno, Daddress, Dtel from depository where depository.Dno=%s', param2)

        if cursor3.rowcount > 0:
            depinfo = cursor3.fetchone()
            Dno = depinfo['Dno']
            Daddress = depinfo['Daddress']
            Dtel = depinfo['Dtel']

            cursor3.close()
            message = "\n下一站请发往： 仓库编号： " + Dno + "\n仓库地址： " + Daddress + "\n仓库联系方式： " + Dtel + '\n'
    
        result = route_graph + message
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'app/query_depository_result.html',
            {
                'username':param2,
                'message1':"Query Result",
                'message2':result,
                'year':datetime.now().year,
            }
        )

    elif cursor.rowcount==0:
        cursor.close()
        assert isinstance(request, HttpRequest)

        
        return render(
            request,
            'app/about.html',   # TODO: 更改html
            {
                # the page: no such tuple
                'title':'Are you szs?',
                'message':'There is no such depository.',
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
    Wno=""
    Ttime=""

    '''
        input:
            运单号 Wno
            进库时间时间 Ttime 
    '''
    # TODO: 获得仓库管理员编号Manager

    if request.method == 'POST':
        Wno = request.POST.get("Wno",None)
        Ttime = request.POST.get("Ttime",None)

    
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='syddbw5200608',
                           db='test2', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    cursor,conn= ac.connect_into_database_up()
    cursor.execute('insert into transfer values(%s,%s,%s)', (Wno, param5, Ttime))
    conn.commit()
    conn.close()
    cursor.close()
    # TODO: commit update
    
    assert isinstance(request, HttpRequest)
    return render(
            request,
            'app/update_depository_result.html',
            {
                'username':param5,
                'message2':"Update Complete",
                'year':datetime.now().year,
            }
        )

def depository_update_distribution(request,param5):
    Wno=""
    DMno=""
    Cname=""
    Ctel=""
    Caddress=""
    '''
        input:
            运单号 Wno
            配送员编号 DMno
            收货人姓名 Cname
            收货人联系方式 Ctel
            收获人地址 Caddress
    '''

     # TODO: 获得仓库管理员编号Manager

    if request.method == 'POST':
        Wno = request.POST.get("Wno",None)
        DMno = request.POST.get("DMno", None)
        Cname = request.POST.get("Cname",None)
        Ctel = request.POST.get("Ctel",None)
        Caddress = request.POST.get("Caddress",None)
        
    cursor, conn = ac.connect_into_database_up()
    cursor.execute('insert into distribution values(%s,%s,%s,%s,%s)', (Wno, DMno, Cname, Ctel, Caddress))
    conn.commit()
    conn.close()
    cursor.close()
    assert isinstance(request, HttpRequest)
    return render(
            request,
            'app/update_depository_result.html',
            {
                'username':param5,
                'message2':"Distribution Updated Complete",
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