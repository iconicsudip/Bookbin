from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from shop.models import Query, OrdersUpdate
from shop.models import Contact
from shop.models import Product
from shop.models import Order
#from shop.models import OrdersUpdate
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from math import ceil
import json

# Create your views here.


def index(request):

    #params={'no_of_slides':nslides,'range':range(1,nslides),'product': products}
    # allProds=[[products,range(1,len(products)),nslides],
    # [products,range(1,len(products)),nslides]]
    allProds = []
    catprods = Product.objects.values('subcatagory', 'id')
    cats = {item['subcatagory'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(subcatagory=cat)
        n = len(prod)
        nslides = n//4 + ceil((n/4)-(n//4))
        allProds.append([prod, range(1, nslides), nslides])

    params = {'allProds': allProds}
    if request.user.is_anonymous:
        pass
    return render(request, "home.html", params)

def searchMatch(query,item):
    """return true if only matches"""
    if query in item.desc2.lower() or query in item.desc2 or query in item.product_name.lower() or query in item.product_name or query in item.subcatagory.lower() or query in item.subcatagory:
        return True
    else:
        return False

def search(request):
    query = request.GET.get('search')
    allProds = []
    catprods = Product.objects.values('subcatagory', 'id')
    cats = {item['subcatagory'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(subcatagory=cat)
        prod = [item for item in prodtemp if searchMatch(query,item)]
        n = len(prod)
        nslides = n//4 + ceil((n/4)-(n//4))
        if len(prod)!=0:
            allProds.append([prod, range(1, nslides), nslides])

    params = {'allProds': allProds}
    if len(allProds)==0 or len(query)<4:
        params={'msg':"Please make sure to enter relevent search query"}

    return render(request, "search.html", params)

def privacy_policy(request):
    return render(request, "privacy&policy.html")


def terms_condition(request):
    return render(request, "terms&condition.html")


def about(request):
    return render(request, "aboutus.html")



def Crime(request):
    return render(request, "crime.html")


def Mystery(request):
    return render(request, "mystery.html")


def Thriller(request):
    return render(request, "thriller.html")


def Detail(request):
    return render(request, "details.html")


def Horror(request):
    return render(request, "horror.html")


def queryus(request):
    if request.method == "POST":
        name = request.POST.get('name')
        bookname = request.POST.get('bookname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        queryus = Query(name=name, bookname=bookname, phone=phone,
                        email=email, desc=desc, date=datetime.today())
        queryus.save()
        messages.success(request, 'Your message has been sent !!!')
    return render(request, "queryus.html")


def contactus(request):
    if request.method == "POST":
        name1 = request.POST.get('name1')
        phone1 = request.POST.get('phone1')
        email1 = request.POST.get('email1')
        desc1 = request.POST.get('desc1')
        contactus = Contact(name1=name1, phone1=phone1,
                            email1=email1, desc1=desc1, date=datetime.today())
        contactus.save()
        messages.success(request, 'Your message has been sent !!!')
    return render(request, "contactus.html")


def tracker(request):
    if request.method=="POST":
        orderId=request.POST.get('orderId','')
        email = request.POST.get('email','')
        try:
            order = Order.objects.filter(order_id=orderId,email=email)
            if len(order)>0:
                update = OrdersUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps(updates, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}') 
    return render(request, "tracker.html")


def admin_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/admin')
        else:
            return render(request, 'login.html')

    return render(request, "login.html")


def handleSignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if len(username) > 10:
            messages.error(request, "Username must be under 10 character")
            return redirect('home')

        if not username.isalnum():
            messages.error(
                request, "Username should only contain letters and number")
            return redirect('home')

        if pass1 != pass2:
            messages.error(request, "Password doesnot match")
            return redirect('home')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(
            request, "Your account created in bookbin, You are welcome")
        return redirect('home')
    else:
        return HttpResponse('404 - Not Found')


def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']
        user = authenticate(username=loginusername, password=loginpass)
        if user is not None:
            login(request, user)
            messages.success(request, "You successfully login")
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials,Please try again")
            return redirect('home')
    return HttpResponse('404 - Not Found')


def handleLogout(request):
    logout(request)
    messages.success(request, "You successfully logout")
    return redirect('home')



def productview(request, myid):
    product = Product.objects.filter(id=myid)
    return render(request, "productview.html", {'product': product[0]})


def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson')
        name2 = request.POST.get('name2', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + \
            "  |  " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone2 = request.POST.get('phone2', '')
        order = Order(items_json=items_json, name2=name2, email=email,
                      address=address, city=city, state=state, zip_code=zip_code, phone2=phone2)
        #order.save()
        #update= OrdersUpdate(order_id= order.order_id, update_desc="The order has been placed")
        #update.save()
        #thank = True
        #id = order.order_id""
        return render(request, "checkout.html", {'thank': thank, 'id': id})
    return render(request, "checkout.html")
