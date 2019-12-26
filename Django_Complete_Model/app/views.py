"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app.forms import BootstrapAuthenticationForm
from django import forms
from django.utils.translation import ugettext_lazy as _
import pymysql
def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def login(request):
    #username=forms.CharField(max_length=254,widget=forms.TextInput({'class':'form-control','placeholder':'User name'}))
    #password=forms.CharField(label=_("Password"),widget=forms.PasswordInput({'class':'form-control','placeholder':'Password'}))
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/login.html',
        {
            'title':'Log in',
            'year': datetime.now().year,
        }
    )

def do_login(request):
    username=""
    password=""
    if request.method=='POST':
        username=request.POST.get("username",None)
        password=request.POST.get("password",None)
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='syddbw5200608',
                           db='test', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    cursor=conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute('select * from login where username=%s and password=%s',(username,password))
    if cursor.rowcount>0:
        cursor.execute('select * from login where username=%s',username)
        login=cursor.fetchone()
        ad=login["identy"]
        if ad=='admin':
            assert isinstance(request, HttpRequest)
            return render(
                request,
                'app/al_log_attention_ad.html',
                {
                    'username':username,
                    'title':'Welcome to admin page.',
                    'message':'You can do all you want.',
                    'year':datetime.now().year,
                }
            )
        if ad=='visitor':
            assert isinstance(request, HttpRequest)
            return render(
                request,
                'app/al_log_attention_normal.html',
                {
                    'username':username,
                    'title':'Welcome to lcy\'s page.',
                    'message':'CY Li is chou di di.',
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
                'message':'Please input the right username and password.',
                'year':datetime.now().year,
            }
        )
def query(request,param1):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/query.html',
        {
            'username':param1,
            'title':'Query',
            'message':'QueryGo',
            'year':datetime.now().year,
        }
    )

def update(request,param2):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/update.html',
        {
            'username':param2,
            'title':'Update',
            'message':'UpdateGo',
            'year':datetime.now().year,
        }
    )

def real_query_order(request,param3):
    order_number=""
    #param3=""
    #param3=request.GET["param3"]
    if request.method=='POST':
        order_number=request.POST.get("order_num",None)
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='syddbw5200608',
                           db='test', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    cursor=conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute('select * from cus_to_pro where o_n=%s',order_number)
    if cursor.rowcount>0:
        cursor.execute('select * from cus_to_pro where o_n=%s',order_number)
        o_to_p=cursor.fetchone()
        oo=o_to_p["o_n"]
        pp=o_to_p["p_n"]
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'app/query_result.html',
            {
                'username':param3,
                'message1':oo,
                'message2':pp,
                'year':datetime.now().year,
            }
        )
    elif cursor.rowcount==0:
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'app/query_result.html',
            {
                'username':param3,
                'message1':"There is no such order.",
                'message2':"Please check.",
                'year':datetime.now().year,
            }
        )

def real_query_tracking(request,param4):
    tracking_number=""
    if request.method=='POST':
        tracking_number=request.POST.get("tracking_num",None)
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='syddbw5200608',
                           db='test', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    cursor=conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute('select * from track where t_n=%s',tracking_number)
    if cursor.rowcount>0:
        cursor.execute('select * from track where t_n=%s',tracking_number)
        track=cursor.fetchone()
        tt=track["t_n"]
        pl=track["place"]
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'app/query_result.html',
            {
                'username':param4,
                'message1':tt,
                'message2':pl,
                'year':datetime.now().year,
            }
        )
    elif cursor.rowcount==0:
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'app/query_result.html',
            {
                'username':param4,
                'message1':"There is no such tracking.",
                'message2':"Please check.",
                'year':datetime.now().year,
            }
        )

def real_update(request,param5):
    tracking_number=""
    place=""
    if request.method=='POST':
        tracking_number=request.POST.get("tracking_num",None)
        place=request.POST.get("place",None)
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='syddbw5200608',
                           db='test', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    cursor=conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute('select * from track where t_n=%s',tracking_number)
    if cursor.rowcount>0:
        cursor.execute('select * from track where t_n=%s',tracking_number)
        track=cursor.fetchone()
        tt=track["t_n"]
        pl=track["place"]
        cursor.execute('update track set place=%s where t_n=%s',(place,tracking_number))
        conn.commit()
        cursor.close()
        conn.close()
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'app/update_result.html',
            {
                'username':param5,
                'message1':pl,
                'message2':place,
                'year':datetime.now().year,
            }
        )
    elif cursor.rowcount==0:
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'app/query_result.html',
            {
                'username':param5,
                'message1':"There is no such tracking.",
                'message2':"Please check.",
                'year':datetime.now().year,
            }
        )
    
