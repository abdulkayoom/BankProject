from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from bank.forms import AccountCreationForm
from bank.models import Branch


# Create your views here.
def index(request):
    return render(request, 'base.html')

def login(request):
        if request.method=='POST':
            username=request.POST['username']
            password=request.POST['password']
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('account')
            else:
                messages.info(request,"invalid login")
                return redirect('login')
        return render(request, 'login.html')

def register(request):
    try:
        if request.method== 'POST':
            username=request.POST['username']
            password=request.POST['password']
            cpassword=request.POST['password1']
            if password==cpassword:
                if User.objects.filter(username=username).exists():
                    messages.info(request,'Username Taken')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password)
                    user.save();
                    return redirect('login')
            else:
                messages.info(request, 'Passwords do NOT match')
                return redirect('register')
            # return redirect('/')
        return render(request, 'register.html')
    except Exception as e:
        messages.info(request, 'Please fill the Fields')
        return redirect('register')

def logout(request):
    auth.logout(request)
    return render(request, 'base.html')

def account(request):
    form = AccountCreationForm()
    if request.method == 'POST':
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account_add')
    return render(request, 'application_form.html',{'form':form})

def confirm(request):
    return render(request, 'confirm.html')

# def load_branch(request):
#     district_id = request.GET.get('district_id')
#     branch = Branch.objects.filter(district_id=district_id).all()
#     return render(request, 'branch_options.html', {'branch':branch})