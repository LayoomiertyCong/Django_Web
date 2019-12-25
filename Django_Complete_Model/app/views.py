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
import PyMySQL
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
    conn = PyMySQL.connect(host='127.0.0.1', port=3306, user='root', password='syddbw5200608',
                           db='test', charset='utf8', cursorclass=PyMySQL.cursors.DictCursor)
    cursor=conn.cursor(PyMySQL.cursors.DictCursor)
    cursor.execute('select * from login where username=%s and password=%s',(username,password))
    if cursor.rowcount>0:
        cursor.execute('select * from login where username=%s',username)
        login=cursor.fetchone()
        ad=login["identy"]
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'app/about.html',
            {
                'title':'Log In result',
                'message':ad,
                'year':datetime.now().year,
            }
    )
    