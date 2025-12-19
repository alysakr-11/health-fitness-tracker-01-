from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            return render(request, 'registration/signup.html', {
                'error': 'Passwords do not match'
            })

        User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )
        return redirect('/accounts/login/')

    return render(request, 'registration/signup.html')
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def signup(request):
    return render(request, 'registration/signup.html')

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def userprofile(request):
    return render(request, 'userprofile.html')

@login_required
def checkin(request):
    return render(request, 'checkin.html')

@login_required
def goals(request):
    return render(request, 'goals.html')

@login_required
def reminders(request):
    return render(request, 'reminders.html')

@login_required
def setting(request):
    return render(request, 'setting.html')
