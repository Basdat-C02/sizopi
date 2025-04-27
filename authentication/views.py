from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'main/index.html')

def login_view(request):
    return render(request, 'login/index.html')

def choose_role_view(request):
    return render(request, 'choose_role/index.html')

def register_view(request):
    return render(request, 'register/index.html')