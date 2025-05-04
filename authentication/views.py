from django.shortcuts import render

# Create your views here.
def landing_view(request):
    return render(request, 'landing/index.html')

def login_view(request):
    return render(request, 'login/index.html')

def choose_role_view(request):
    return render(request, 'choose_role/index.html')

def register_pengunjung_view(request):
    if request.method == 'POST':
        # Validasi dan logika buat akun
        pass
    return render(request, 'register_pengunjung/index.html')

def register_dokter_hewan_view(request):
    if request.method == 'POST':
        # Validasi dan logika buat akun
        pass
    return render(request, 'register_dokter/index.html')

def register_staff_view(request):
    if request.method == 'POST':
        # Validasi dan logika buat akun
        pass
    return render(request, 'register_staff/index.html')