from django.shortcuts import render, redirect
from .forms import CreateUserForm,LoginForm, CreateFormRecord, UpdateFormRecord

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

from .models import Records
from django.contrib import messages

# Create your views here.

# Home Page
def home(request):

    return render (request, 'webapp/index.html')

# Register users

def Register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            
            messages.success(request, "Account created successfully!")

            return redirect('my-login')
        
    context = {'form': form}

    return render (request, 'webapp/register.html', context)

# login a user   

def Login(request):

    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request, data = request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password') 

            user = authenticate(request, username = username , password = password)

            if user is not None:
                auth.login(request, user)

                messages.success(request, "Logged in successfully")


                return redirect('profile-dashboard')
    context = {'form': form}
    return render (request, 'webapp/my-login.html', context=context) 


# DASHBOARD/PROFILE
@login_required(login_url='my-login')
def profile(request): 

    records = Records.objects.all()

    context = {'records': records}

    return render (request, 'webapp/profile-dashboard.html', context=context)

# Log out a user    

def Logout(request):
    auth.logout(request)

    messages.success(request, "Logged out successfully")

    return redirect('my-login')

# Create a record 

@login_required(login_url='my-login')
def create_record(request):

    form = CreateFormRecord()

    if request.method == 'POST':
        form = CreateFormRecord(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, "Record created")
            return redirect('profile-dashboard')
    context = {'form': form}

    return render(request, 'webapp/create-record.html', context=context) 

# Update a record


@login_required(login_url='my-login')
def update_record(request,pk):

   record = Records.objects.get(id=pk)

   form = UpdateFormRecord(instance=record)

   if request.method == 'POST':
       form = UpdateFormRecord(request.POST, instance=record)

       if form.is_valid():
           form.save()

           messages.success(request, 'Your record was successfully updated')
           return redirect('profile-dashboard')
       
   context = {'form': form}  

   return render(request, 'webapp/update-record.html', context) 


# View/Read Records

@login_required(login_url='my-login')
def singular_record(request,pk):
    
    all_records = Records.objects.get(id=pk)

    context = {'record':all_records}

    return render(request, 'webapp/view-record.html', context = context)

# Delete a record

@login_required(login_url='my-login')
def delete_record(request,pk):
    
    record = Records.objects.get(id=pk)

    record.delete()

    messages.success(request, 'Deleted successfully')

    return redirect('profile-dashboard')