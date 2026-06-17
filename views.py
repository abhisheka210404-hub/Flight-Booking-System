from django.shortcuts import render,redirect
from .models import Fligths,user,History
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash

# Create your views here.

def register(request):


    if request.method == 'POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        uname=request.POST['uname']
        email=request.POST['email']
        password=request.POST['pass']


        try:
            User.objects.get(username=uname)
            messages.error(request,"Username already exist")
            return redirect('register')


        except:
            User.objects.create_user(
                first_name=fname,
                last_name=lname,
                username=uname,
                password=password,
                email=email
            )
            messages.success(request,"Register Sucess".upper())
            return redirect('login')

    return render(request,'register.html')

def login_(request):

    if request.method=='POST':
        uname=request.POST['uname']
        password=request.POST['pass']

        user=authenticate(username=uname,password=password)

        if user:
            login(request,user)
            messages.success(request,"login sucess".upper())
            return redirect('home')
        else:
            messages.error(request,'Username or password is incorect'.upper())
            return redirect('login')

    return render(request,'login.html')

def logout_(request):
    logout(request)
    return redirect('login')


def home(request):

    data=Fligths.objects.all()

    return render(request,'home.html',{'data':data})

@login_required(login_url='login')
def confirm(request,id):

    data=Fligths.objects.get(id=id)

    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        age=request.POST['age']
        adhar=request.POST['adhar']
        phno=request.POST['phno']
        seat_class=request.POST['seatclass']
        seat_number=request.POST['seatnumber']
        user.objects.create(
            user=request.user,
            flight=data,
            name=name,
            email=email,
            age=age,
            adhar=adhar,
            phno=phno,
            seat_class=seat_class,
            seat_number=seat_number
        )

        return redirect('home')


    return render(request,'conform.html',{'data':data})


def bookings(request):

    print(request.user)
    # AnonymousUser when user is not log in that time request.user 

    if request.user.is_authenticated:

        data=user.objects.filter(user=request.user)

        return render(request,'bookings.html',{'data':data})

    else:
        print(request.user)
        # messages.error(request,"Please Login to book".upper())
        return redirect('login')


def update(request,id):

    data=user.objects.get(id=id)

    if request.method=='POST':
        print(request.POST['age'])

        name=request.POST['name']
        email=request.POST['email']
        age=request.POST['age']
        adhar=request.POST['adhar']
        phno=request.POST['phno']
        seat_class=request.POST['seatclass']
        seat_number=request.POST['seatnumber']

        data.name=name
        data.email=email
        data.age=age
        data.adhar=adhar
        data.phno=phno
        data.seat_class=seat_class
        data.seat_number=seat_number

        data.save()

        return redirect('bookings')

    return render(request,'update.html',{'data':data})


def cancel(request,id):

    data=user.objects.get(id=id)

    History.objects.create(
        user=request.user,
        flight=data.flight,
        name=data.name,
        email=data.email,
        age=data.age,
        adhar=data.adhar,
        phno=data.phno,
        seat_class=data.seat_class,
        seat_number=data.seat_number
    )

    data.delete()

    return redirect('bookings')


@login_required(login_url='login')
def history(request):

    data=History.objects.filter(user=request.user)

    return render(request,'history.html',{'data':data})

@login_required(login_url='login')
def profile(request):
    return render(request,'profile.html')

@login_required(login_url='login')
def reset(request):
    if request.method=='POST':
        if 'opass' in request.POST:
            old_pass=request.POST['opass']

            action=authenticate(username=request.user,password=old_pass)

            if action:
                messages.success(request,"Enter The New Password")
                return render(request,'reset.html',{'new':True})
            else:
                messages.error(request,"Entered Password Is Incorrect")
                return redirect('reset')
        
        if 'npass' in request.POST:
            new_pass=request.POST['npass']
            c_pass=request.POST['cpass']
            if not new_pass==c_pass:
                messages.error(request,'Password Mismatch')
                return redirect('reset')
            else:
                user=User.objects.get(username=request.user)
                if user.check_password(new_pass):
                    messages.error(request,'Password Cant Be Same')
                    return redirect('reset')
                else:
                    user.set_password(new_pass)
                    user.save()
                    update_session_auth_hash(request,user)
                    messages.success(request,"Password Update Successfully")
                    return redirect('profile')

    return render(request,'reset.html')


def pupdate(request):

    username=request.user
    user=User.objects.get(username=username)

    if request.method=='POST':
        user.first_name=request.POST['fname']
        user.last_name=request.POST['lname']
        user.email=request.POST['email']
        user.save()
        messages.success(request,'Details Updated Succesfully..')
        return redirect('profile')

    return render(request,'pupdate.html',{'data':user})

def forgot_pasw(request):

    print(request.POST)
    if request.method=='POST':
        if 'uname' in request.POST:
            uname=request.POST['uname']

            try:
                user=User.objects.get(username=uname)
                request.session['username']=uname
                return render(request,'forgot_pasw.html',{'show':True})

            except:
                messages.error(request,'Username Doesnt Exist..')
                return redirect('forgot_pasw')

        if 'npass' in request.POST:
            new_password=request.POST['npass']
            confirm_password=request.POST['cpass']
            username=request.session['username']
            print(username)

            if new_password != confirm_password:
                messages.error(request,'Password Mismatch')
                return redirect('forgot_pasw')
            
            user=User.objects.get(username=username)

            if user.check_password(new_password):
                messages.error(request,"Password Cant Be Same..")
                return redirect('forgot_pasw')

            if not username:
                messages.success(request,'Session Got Expired...')
                return redirect('forgot_pasw')
            
            user.set_password(new_password)
            user.save()
            del username
            messages.success(request,'Password Update successfully...')
            return redirect('login')

    return render(request,'forgot_pasw.html')


def about(request):
    return render(request,'about.html')

