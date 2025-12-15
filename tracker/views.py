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
