# import cv2
import os
# import numpy as np
from typing import Any
from django.shortcuts import render, HttpResponse
#from home.models import sign_up
#from datetime import datetime
from home.models import ID, PASP, PDCP, PIGP, PIP, PSIP, Search_Name, User
from home.models import Officers
from home.models import Other
from home.models import Add_Criminal
from home.models import Reports
from home.models import Search_Name
# from PIL import ImageChops


#from home.models import Ex


# Create your views here.
def index(request):
    context= {
                "variable":"this is sent"
    }
    return render(request, 'index.html',context)
    #return HttpResponse("This is homepage")
    
def offindex(request):
    return render(request, 'offIndex.html')

def otheroffindex(request):
    return render(request, 'OtherOffIndex.html')


def about(request):
    return render(request, 'about.html')
    #return HttpResponse("This is about page")
    
def contact(request):
    return render(request, 'contact.html')
    #return HttpResponse("This is contact page")

def services1(request):
    if request.method == "POST":
        ufname = request.POST.get('ufname')
        ulname = request.POST.get('ulname')
        usename = request.POST.get('username')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        cfname = request.POST.get('cfname')
        clname = request.POST.get('clname')
        reason = request.POST.get('reason')
        services = Search_Name(ufname=ufname, ulname=ulname, username=usename, phone=phone, city=city, cfname=cfname , clname=clname, reason=reason)
        services.save()
        
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        result3 = Add_Criminal.objects.filter(fname=fname,lname=lname)
        print(result3)
        # for i in result3:
        #     x = i
        #     print(i)
        #     print(type(i))
        if result3:
            return render(request, 'after_nm_search.html', {'result3':result3 })
        # if services:
        #     return render(request, 'after_nm_search.html')
    return render(request, 'services1.html')
    #return HttpResponse("Search here by suspects name for getting info about them if there is any")    
    
# def match1(image1, image2):
#     return ImageChops.difference(image1, image2).getbbox() is None

def services2(request):
    if request.method == "POST":
        image1 = request.POST.get('image1')
        abc = os.path.abspath(image1)
        # im1 = cv2.imread(abc)
        print(abc)
        result3 = Add_Criminal.objects.all()
        # result4 = ID.objects.filter(image1=image1)
        if result3:
            for r in result3:
                # im2 = cv2.imread(r.image.url)
                # print(type(im2))

                # if (im1.shape == im2.shape):
                    # diff = cv2.subtract(im1, im2)
                    # b, g, r = cv2.split(diff)
                    # if (cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0):
                        print("same")
                        return render(request, 'after_nm_search.html', {'result3': r })
                    # else:
                        # print("not same")

                # else:
                    # print("not same")

    return render(request, 'services2.html')
def report(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip = request.POST.get('zip')
        complaint = request.POST.get('complaint')
        add_reports = Reports(fname=fname, lname=lname, phone=phone, city=city, state=state, zip=zip, complaint=complaint)
        add_reports.save()
        if add_reports:
            return render(request, 'index.html')
    return render(request, 'report.html')
    #return HttpResponse("Report any issues About This Website if there is any")    

def userReg(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        address2 = request.POST.get('address2')
        city = request.POST.get('city')
        #state = request.POST.get('state')
        zip = request.POST.get('zip')
        print(email,password)
        user = User(email=email, password=password, address=address, address2=address2, city=city, zip=zip)
        user.save()
        if user:
            return render(request, 'userLogin.html')
    return render(request, 'UserRegistrations.html')

    '''if request.method == "POST":
        email = request.POST.get('email')
        text = request.POST.get('text')
        ex = Ex(email=email,text=text)
        ex.save()
        '''
    '''if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        address2 = request.POST.get('address2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip = request.POST.get('zip')
        user = User(email=email, password=password, address=address, address2=address2, city=city, state=state, zip=zip, date=datetime.today())
        user.save()
'''

def officialRegistration(request):
    print("hii")
    if request.method == "POST":
        print("hello")
        name1 = request.POST.get('name1')
        name2 = request.POST.get('name2')
        email1 = request.POST.get('email1')
        password1 = request.POST.get('password1')
        contact1 = request.POST.get('contact1')
        rank1 = request.POST.get('rank1')
        uniq1 = request.POST.get('uniq1')
        address01 = request.POST.get('address01')
        address02 = request.POST.get('address02')
        city1 = request.POST.get('city1')
        #print(email,password)
        official = Officers(name2=name2, email1=email1, password1=password1, contact1=contact1, rank1=rank1, uniq1=uniq1, address01=address01, address02=address02, city1=city1)
        official.save()
        if official:
            return render(request, 'offlogin.html')
    return render(request, 'officialRegistration.html')

def otheroffReg(request):
    if request.method == "POST":
        name11 = request.POST.get('name11')
        name22 = request.POST.get('name22')
        email11 = request.POST.get('email11')
        password11 = request.POST.get('password11')
        contact11 = request.POST.get('contact11')
        pro11 = request.POST.get('pro11')
        uniq11 = request.POST.get('uniq11')
        address11 = request.POST.get('address11')
        address22 = request.POST.get('address22')
        city11 = request.POST.get('city11')
        #print(email,password)
        other_official = Other(name11=name11, name22=name22, email11=email11, password11=password11, contact11=contact11, pro11=pro11, uniq11=uniq11, address11=address11, address22=address22, city11=city11)
        other_official.save()
        if other_official:
            return render(request, 'otheroffLogin.html')
    return render(request, 'otheroffReg.html')

def userLogin(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email,password)
        # result = User.objects.all()
        # for i in result:
        #     print(i.email,i.password)
        result1 = User.objects.filter(email=email,password=password)
        if result1:
            return render(request, 'index.html')
    return render(request, 'userLogin.html')


def offLogin(request):
    if request.method == "POST":
        email1 = request.POST.get('email1')
        password1 = request.POST.get('password1')
        uniq1 = request.POST.get('uniq1')
        #print(email,password,zip)
        # result = User.objects.all()
        # for i in result:
        #     print(i.email,i.password)
        result2 = Officers.objects.filter(email1=email1,password1=password1,uniq1=uniq1)
        if result2:
            return render(request, 'offIndex.html')
    return render(request, 'offLogin.html')

def otheroffLogin(request):
    if request.method == "POST":
        email11 = request.POST.get('email11')
        password11 = request.POST.get('password11')
        uniq11 = request.POST.get('uniq11')
        #print(email,password,zip)
        # result = User.objects.all()
        # for i in result:
        #     print(i.email,i.password)
        result3 = Other.objects.filter(email11=email11,password11=password11,uniq11=uniq11)
        if result3:
            return render(request, 'OtherOffIndex.html')
    return render(request, 'otheroffLogin.html')


def addCriminals(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        age = request.POST.get('age')
        charges = request.POST.get('charges')
        city = request.POST.get('city')
        zip = request.POST.get('zip')
        duration = request.POST.get('duration')
        uniq1 = request.POST.get('uniq1')
        location = request.POST.get('location')
        image10 = request.POST.get('image')
        status = request.POST.get('status')
        fname1 = request.POST.get('fname1')
        lname1 = request.POST.get('lname1')
        age1 = request.POST.get('age1')
        rank = request.POST.get('rank')
        phone = request.POST.get('phone')
        print(type(image10))
        add_criminal = Add_Criminal(fname=fname, lname=lname, age=age, charges=charges, city=city, zip=zip, duration=duration, uniq1=uniq1, location=location, image=image10, status=status, fname1=fname1, lname1=lname1, age1=age1, rank=rank, phone=phone)
        add_criminal.save()
        if add_criminal:
            return render(request, 'offIndex.html')

    return render(request, 'addCriminals.html')


# def complaint(request):
#     if request.method == "POST":
#         fname = request.POST.get('fname')
#         lname = request.POST.get('lname')
#         phone = request.POST.get('phone')
#         city = request.POST.get('city')
#         state = request.POST.get('state')
#         zip = request.POST.get('zip')
#         add_complaits = Complaints(fname=fname, lname=lname, phone=phone, city=city, state=state, zip=zip)
#         add_complaits.save()
#         if add_complaits:
#             return render(request, 'offIndex.html')
#         return render(request, 'complaint.html')

def other_search(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        uniq1 = request.POST.get('uniq1')
        result3 = Add_Criminal.objects.filter(fname=fname,lname=lname, uniq1=uniq1)
        if result3:
            return render(request, 'after_nm_search.html', {'result3':result3 })
    return render(request, 'other_search.html')

def after_nm_search(request):
    return render(request, 'after_nm_search.html')

def view_all_criminals(request):
    criminals = Add_Criminal.objects.all()
    criminals = PSIP.objects.all()
    criminals = PIP.objects.all()
    criminals = PDCP.objects.all()
    criminals = PASP.objects.all()
    criminals = PIGP.objects.all()
    return render(request, 'view_all_criminals.html', {'criminals':criminals})

def view_complaints(request):
    complaints = Reports.objects.all()
    return render(request, 'view_complaints.html', {'complaints':complaints})

def view_searched_criminals(request):
    searched = Search_Name.objects.all()
    # searched = Add_Criminal.objects.all()
    return render(request, 'view_searched_criminals.html', {'searched':searched})

def error(request):
    return render(request, 'error.html')    

# def match(image, image1):
#     result3 = Add_Criminal.objects.filter(image=image)
#     result4 = ID.objects.filter(image1=image1)
#     if result3 and result4:
#         return ImageChops.difference(image, image1).getbbox() is None

# def match(image, image1):
#     return ImageChops.difference(image, image1).getbbox() is None

def Rape(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        age = request.POST.get('age')
        charges = request.POST.get('charges')
        city = request.POST.get('city')
        zip = request.POST.get('zip')
        duration = request.POST.get('duration')
        uniq1 = request.POST.get('uniq1')
        location = request.POST.get('location')
        image10 = request.POST.get('image')
        status = request.POST.get('status')
        fname1 = request.POST.get('fname1')
        lname1 = request.POST.get('lname1')
        age1 = request.POST.get('age1')
        rank = request.POST.get('rank')
        phone = request.POST.get('phone')
        print(type(image10))
        add_criminal = PASP(fname=fname, lname=lname, age=age, charges=charges, city=city, zip=zip, duration=duration, uniq1=uniq1, location=location, image=image10, status=status, fname1=fname1, lname1=lname1, age1=age1, rank=rank, phone=phone)
        add_criminal.save()
        if add_criminal:
            return render(request, 'offIndex.html')

    return render(request, 'Pasp.html')


def Murder(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        age = request.POST.get('age')
        charges = request.POST.get('charges')
        city = request.POST.get('city')
        zip = request.POST.get('zip')
        duration = request.POST.get('duration')
        uniq1 = request.POST.get('uniq1')
        location = request.POST.get('location')
        image10 = request.POST.get('image')
        status = request.POST.get('status')
        fname1 = request.POST.get('fname1')
        lname1 = request.POST.get('lname1')
        age1 = request.POST.get('age1')
        rank = request.POST.get('rank')
        phone = request.POST.get('phone')
        print(type(image10))
        add_criminal = PDCP(fname=fname, lname=lname, age=age, charges=charges, city=city, zip=zip, duration=duration, uniq1=uniq1, location=location, image=image10, status=status, fname1=fname1, lname1=lname1, age1=age1, rank=rank, phone=phone)
        add_criminal.save()
        if add_criminal:
            return render(request, 'offIndex.html')

    return render(request, 'Pdcp.html')

def Terrorist(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        age = request.POST.get('age')
        charges = request.POST.get('charges')
        city = request.POST.get('city')
        zip = request.POST.get('zip')
        duration = request.POST.get('duration')
        uniq1 = request.POST.get('uniq1')
        location = request.POST.get('location')
        image10 = request.POST.get('image')
        status = request.POST.get('status')
        fname1 = request.POST.get('fname1')
        lname1 = request.POST.get('lname1')
        age1 = request.POST.get('age1')
        rank = request.POST.get('rank')
        phone = request.POST.get('phone')
        print(type(image10))
        add_criminal = PIGP(fname=fname, lname=lname, age=age, charges=charges, city=city, zip=zip, duration=duration, uniq1=uniq1, location=location, image=image10, status=status, fname1=fname1, lname1=lname1, age1=age1, rank=rank, phone=phone)
        add_criminal.save()
        if add_criminal:
            return render(request, 'offIndex.html')

    return render(request, 'Pigp.html')

def Kidnapping(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        age = request.POST.get('age')
        charges = request.POST.get('charges')
        city = request.POST.get('city')
        zip = request.POST.get('zip')
        duration = request.POST.get('duration')
        uniq1 = request.POST.get('uniq1')
        location = request.POST.get('location')
        image10 = request.POST.get('image')
        status = request.POST.get('status')
        fname1 = request.POST.get('fname1')
        lname1 = request.POST.get('lname1')
        age1 = request.POST.get('age1')
        rank = request.POST.get('rank')
        phone = request.POST.get('phone')
        print(type(image10))
        add_criminal = PIP(fname=fname, lname=lname, age=age, charges=charges, city=city, zip=zip, duration=duration, uniq1=uniq1, location=location, image=image10, status=status, fname1=fname1, lname1=lname1, age1=age1, rank=rank, phone=phone)
        add_criminal.save()
        if add_criminal:
            return render(request, 'offIndex.html')

    return render(request, 'Pip.html')

def Robbery_cases(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        age = request.POST.get('age')
        charges = request.POST.get('charges')
        city = request.POST.get('city')
        zip = request.POST.get('zip')
        duration = request.POST.get('duration')
        uniq1 = request.POST.get('uniq1')
        location = request.POST.get('location')
        image10 = request.POST.get('image')
        status = request.POST.get('status')
        fname1 = request.POST.get('fname1')
        lname1 = request.POST.get('lname1')
        age1 = request.POST.get('age1')
        rank = request.POST.get('rank')
        phone = request.POST.get('phone')
        print(type(image10))
        add_criminal = PSIP(fname=fname, lname=lname, age=age, charges=charges, city=city, zip=zip, duration=duration, uniq1=uniq1, location=location, image=image10, status=status, fname1=fname1, lname1=lname1, age1=age1, rank=rank, phone=phone)
        add_criminal.save()
        if add_criminal:
            return render(request, 'offIndex.html')

    return render(request, 'Psip.html')

def Robbers(request):
    criminals1 = PSIP.objects.all()
    return render(request, 'Robbers.html', {'criminals1':criminals1})

def Kidnappers(request):
    criminals2 = PIP.objects.all()
    return render(request, 'Kidnappers.html', {'criminals2':criminals2})

def Murderers(request):
    criminals3 = PDCP.objects.all()
    return render(request, 'Murderers.html', {'criminals3':criminals3})

def Rapists(request):
    criminals4 = PASP.objects.all()
    return render(request, 'Rapists.html', {'criminals4':criminals4})

def Terrorists(request):
    criminals5 = PIGP.objects.all()
    return render(request, 'Terrorists.html', {'criminals5':criminals5})

def map(request):
    mapbox_access_token = 'pk.my_mapbox_access_token'
    return render(request, 'map.html',{'mapbox_access_token': mapbox_access_token})    
