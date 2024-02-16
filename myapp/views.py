import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from django.http import HttpResponseRedirect
from django .contrib.auth.decorators import login_required
# from django.shortcuts import render_to_response
from bs4 import BeautifulSoup
import re
import pandas as pd
import requests
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import auth
import io
from myapp import store1
import threading
import schedule


# Create your views here.
conn = connection.cursor()

def dataCrawl(product):
    results = []
    pc24_thread = threading.Thread(target=store1.store().PC,args = (product,results))
    cf_thread = threading.Thread(target=store1.store().Carrefour,args = (product,results))
    momo_thread = threading.Thread(target=store1.store().momo,args = (product,results))
    poya_thread = threading.Thread(target=store1.store().Poya,args = (product,results))

    pc24_thread.start()
    cf_thread.start()
    momo_thread.start()
    poya_thread.start()
    pc24_thread.join()
    cf_thread.join()
    momo_thread.join()
    poya_thread.join()
    return results

# def ele(request):
#     results = dataCrawl("3C產品")
#     # eleresults = json.dumps(results)
#     title = results[0]["標題"]
#     price = results[0]["價錢"]
#     link = results[0]["連結"]
#     pic = results[0]["圖片"]

#     # return render(request, "en_index.html", {"eleresults":eleresults}) 

#     return render(request, "ex_index.html", {"title": title, "price": price, 
#                                              "link":link,"pic":pic,})

def product3C():
    rows = conn.execute("select * from product3C")
    




def search(request):
    product=request.GET['product']
    results=dataCrawl(product)
    return render(request, "search.html", {'product':product,'results': results})
#首頁
def ex_index(request):
    return render(request, "ex_index.html")

def base(request):
    return render(request, "search-base.html")

def ex_fashion_3C(request):
    product='3C'
    results=dataCrawl(product)
    return render(request, "search.html", {'product':product,'results': results})

def ex_fashion_colthing(request):
    product='外套'
    results=dataCrawl(product)
    return render(request, "search.html", {'product':product,'results': results})

def ex_fashion_pet(request):
    product='飼料'
    results=dataCrawl(product)
    return render(request, "search.html", {'product':product,'results': results})

def ex_fashion_Srationery(request):
    product='筆'
    results=dataCrawl(product)
    return render(request, "search.html", {'product':product,'results': results})
def ex_fashion_daily(request):
    product='冰箱'
    results=dataCrawl(product)
    return render(request, "search.html", {'product':product,'results': results})

#首頁(測試)
def index(request):
    product = "3C產品"
    results = dataCrawl(product)
    eleresults = json.dumps(results)
    # title = eleresults.json()["title"]
    # price = eleresults.json()["price"]
    # link = eleresults.json()["lick"]
    # pic = eleresults.json()["pic"]
    title = eleresults.json.dumps(title)
    price = eleresults.json.dumps(price)
    link = eleresults.json.dumps(link)
    pic = eleresults.json.dumps(pic)
    return render(request, "index.html", {"eleresults":eleresults, "title": title, "price": price, 
                                             "link":link,"pic":pic})

def profile(request):
    user = request.user

    return render(request, "profile.html", {"user": user})

# def login(request):
#     if request.user.is_authenticated:
#         return HttpResponseRedirect('')
#     username = request.POST.get('username', '')
#     password = request.POST.get('password', '')
#     user = auth.authenticate(username=username, password=password)
#     if user is not None and user.is_active:
#         auth.login(request, user)
#         return HttpResponseRedirect('')
#     else:
#         return render(request, 'login.html', locals())
def login(request):
    message = ""
    if request.method == "POST":
        if request.POST.get("register"):
            return redirect("register")
        elif request.POST.get("login"):
            username = request.POST["username"]
            password = request.POST["password"]
            user = User.objects.filter(username=username)
            if not user:
                message = "無此帳號!"
            else:
                user = authenticate(
                    request, username=username, password=password)
                if not user:
                    message = "密碼錯誤!"
                else:
                    login(request, user)
                    message = "登入成功!"
                    return redirect("profile")

        print(user)

    return render(request, "login.html", {"message": message})

# def logout(request):
#     auth.logout(request)
#     return HttpResponseRedirect('../../../')
def user_logout(request):
    logout(request)
    return redirect(request,"ex_index.html")

def register(request):
    message = ""
    if request.method == "POST":
        print(request.POST)
        username = request.POST["username"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        email=request.POST["email"]

        print(username, password1, password2)
        if password1 != password2:
            message = "輸入兩次密碼不相同"
        elif len(password1) < 8:
            message = "錯誤，密碼過短"
        else:
            if User.objects.filter(username=username):
                message = "帳號重複"
            else:
                user = User.objects.create_user(username=username,
                                                password=password1,
                                                email=email)
                user.save()
                message = "註冊成功"

    form = UserCreationForm()
    return render(request, "register.html", {"form": form, "message": message})
    # return render(request, "register.html")


def regadd(request):
    username=request.POST['username']
    email=request.POST['email']
    password=request.POST['password']
    sex=request.POST['sex']
    birthday=request.POST['birthday']
    conn.execute('insert into userinfo(username, email, password, \
                     sex, birthday) values(%s, %s, %s, %s, %s)', \
                        (username, email, password, sex, birthday))
    check = conn.execute('select username from userinfo')
    checkname = check.fetchall()
    if username == checkname :
        return HttpResponse("註冊成功")
    else:
        return redirect("register.html")