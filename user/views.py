from django.shortcuts import render, HttpResponse, redirect
from django.contrib import auth
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth.models import Group
from .models import *
import sys
import re

def home(request):
    room = Room.objects.all()
    context = {
        'room': room
    }

    if request.method == "POST":
        if 'signup1' in request.POST:
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('booking')
            else:
                return redirect('failure')
    else:
        return render(request, 'index.html', context)

def booking(request):
    if request.method == "POST":
        if 'search' in request.POST:
        
            check_in = request.POST['check_in']
            check_out = request.POST['check_out']
            adult = request.POST['adult']
            child = request.POST['child']
        
            book = Booking()
            book.check_in = check_in
            book.check_out = check_out
            book.adult = adult
            book.child = child
            book.save()
            
            return redirect('room')

    else:
        return render(request, 'booking.html', {})

def room(request):
    context = {}
    try:
        room = Room.objects.all()
        booking = Booking.objects.latest()
        context={'room': room, 'booking': booking}
    except :
        pass
    return render(request, 'room.html', context )

def fare(request, pk):
    try:
        booking = Booking.objects.latest()
        room = Room.objects.get(pk=pk)
        context = {
            'room': room,
            'booking':booking
        }
    except:
        pass
    
    return render(request, 'fare.html', context)

def success(request):
    return render(request,'success.html',{})

def failure(request):
    return render(request, 'failure.html',{})

def usersignup(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        lis = password_checker(password) 

        if (password != confirm_password):
            messages.info(request,'Password does not match.')
            return redirect('adsignup')
        elif (len(lis) != 0  ):
            for i in lis:
                messages.info(request,i)
            return redirect('signup')

        user = Usersignup()
        user.firstname = firstname
        user.lastname = lastname
        user.username = username
        user.email = email
        user.save()
        try:
            myuser = User.objects.create_user(username, email, password)
            myuser.firstname = firstname
            myuser.lastname = lastname

            myuser.save()
            return redirect('home')

        except IntegrityError:
            return redirect('failure')
    else:
        return render(request, 'usersignup.html')

def adminsignup(request):
    if request.method == "POST":
        name = request.POST.get('name')
        staffid = request.POST.get('staffid')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        lis = password_checker(password) 

        if (password != confirm_password):
            messages.info(request,'Password does not match.')
            return redirect('adsignup')
        elif (len(lis) != 0  ):
            for i in lis:
                messages.info(request,i)
            return redirect('adsignup')

        admin = Adminsignup()
        admin.name = name
        admin.staffid = staffid
        admin.save()

        try:
            myuser = User.objects.create_user(staffid, name, password)
            myuser.is_staff = True
            myuser.save()
            mygroup = Group.objects.get(name="admins")
            mygroup.user_set.add(myuser)
            mygroup.save()

            return redirect('home')
        except IntegrityError:
            messages.error("laters baby")
    else:
        return render(request, 'adminsignup.html')

def userlogout(request):
    logout(request)
    messages.success(request, 'Succesfully Logged Out')
    return redirect('home')

def password_checker(password):
    msg=[]
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    #     length
    correct_length = len(password) >=   8
    if not correct_length:
        msg.append("Invalid password: too short")
    #     digit
    su = sum(1 for character in password if character.isdigit())
    sufficient_digits = su >= 2
    if not sufficient_digits:
        msg.append("Must have at least 2 digits")
    #     Upper/Lower
    letters = set(password)
    lower = any(letter.islower() for letter in letters)
    upper = any(letter.isupper() for letter in letters)
    if not upper:
        msg.append("No uppercase characters detected")
    if not lower:
        msg.append("No lowercase characters detected")
    #     special char
    if (regex.search(password) == None ):
        msg.append("Must contain atleast one special symbol.")
    else:
        print("Congratulations! This password is valid")
    return msg