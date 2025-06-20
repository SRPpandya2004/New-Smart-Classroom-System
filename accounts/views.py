from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard after login
        else:
            return render(request, 'signin.html', {'error': 'Invalid credentials'})
    return render(request, 'signin.html')


def registration(request):
    if request.method == 'POST':
        # Process your registration form data here and create a user.
        # For example:
        # user = User.objects.create_user(...)
        # return redirect('signin')
        pass
    return render(request, 'registration.html')


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


def signout(request):
    logout(request)
    return redirect('signin')


# from django.shortcuts import render

# def dashboard(request):
#     return render(request, 'dashbord.html')

# def registration(request):
#     return render(request, "registration.html")

# def signin(request):
#     return render(request, "signin.html")
