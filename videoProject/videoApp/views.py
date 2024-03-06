from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, 'login.html', {'success': 'Registration Success. Please Login'})
        else:
            errorMessage = form.errors.as_text()
            return render(request, 'register.html', {'error': errorMessage})
 
    return render(request, 'register.html')

def login_view(request):
    if request.method=="POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            return render(request, 'login.html', {'error': "Invalid credentials. Please try again."})

    return render(request, 'login.html')


@login_required
def dashboard(request): 
    return render(request, 'dashboard.html', {'email' : request.user.email})


@login_required
def videoCallView(request):
    return render(request, 'videoCall.html', {'email' : request.user.email} )

@login_required
def logoutView(request):
    logout(request)
    return redirect('login')

@login_required
def joinRoom(request):
    if request.method == 'POST':
        roomID = request.POST['roomID']
        return redirect('/meeting/?roomID=' + roomID) 
    return render(request, 'joinRoom.html', {'email' : request.user.email})
