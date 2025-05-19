import uuid
from django.shortcuts import render, redirect
from django.contrib import messages
from authentication.services.auth_service import AuthService
from authentication.utils.jwt_utils import generate_jwt


# Create your views here.
def landing_view(request):
    return render(request, 'landing/index.html')

def choose_role_view(request):
    return render(request, 'choose_role/index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = AuthService.get_user_by_username(username)
        if not user:
            messages.error(request, 'Username tidak ditemukan')
            return redirect('authentication:login')
        
        if password != user['password']:
            messages.error(request, 'Password salah')
            return redirect('authentication:login')
        
        token = generate_jwt(username)
        response = redirect('authentication:profile_pengguna')
        response.set_cookie('jwt', token, httponly=True, samesite='Strict')
        return response
        
    return render(request, 'login/index.html')

def register_pengunjung_view(request):
    if request.method == 'POST':
        data = {
            "username": request.POST.get("username"),
            "password": request.POST.get("password"),
            "email": request.POST.get("email"),
            "nama_depan": request.POST.get("nama_depan"),
            "nama_tengah": request.POST.get("nama_tengah"),
            "nama_belakang": request.POST.get("nama_belakang"),
            "no_telepon": request.POST.get("no_telepon"),
            "alamat": request.POST.get("alamat"),
            "tgl_lahir": request.POST.get("tanggal_lahir"),
            "role": "Pengunjung",
        }
        
        if request.POST.get("password") != request.POST.get("confirm_password"):
            messages.error(request, "Konfirmasi password tidak cocok.")
            return redirect("authentication:register_pengunjung") 
        
        AuthService.create_profile(data)
        messages.success(request, "Registrasi berhasil. Silakan login.")
        return redirect("authentication:login")

    return render(request, 'register/pengunjung.html')

def register_dokter_hewan_view(request):
    if request.method == 'POST':
        spesialisasi = request.POST.getlist("spesialisasi")
        lainnya = request.POST.get("spesialisasi_lainnya")
        if lainnya:
            spesialisasi.append(lainnya)
        data = {
            "username": request.POST.get("username"),
            "password": request.POST.get("password"),
            "email": request.POST.get("email"),
            "nama_depan": request.POST.get("nama_depan"),
            "nama_tengah": request.POST.get("nama_tengah"),
            "nama_belakang": request.POST.get("nama_belakang"),
            "no_telepon": request.POST.get("no_telepon"),
            "no_str": request.POST.get("no_str"),
            "spesialisasi": spesialisasi,
            "role": "Dokter Hewan",
        }
        
        if request.POST.get("password") != request.POST.get("confirm_password"):
            messages.error(request, "Konfirmasi password tidak cocok.")
            return redirect("authentication:register_pengunjung") 
        
        AuthService.create_profile(data)
        messages.success(request, "Registrasi berhasil. Silakan login.")
        return redirect("authentication:login")
    
    return render(request, 'register/dokter_hewan.html')

def register_staff_view(request):
    if request.method == 'POST':
        peran = request.POST.get("peran")
        id_staf = str(uuid.uuid4())
        data = {
            "username": request.POST.get("username"),
            "password": request.POST.get("password"),
            "email": request.POST.get("email"),
            "nama_depan": request.POST.get("nama_depan"),
            "nama_tengah": request.POST.get("nama_tengah"),
            "nama_belakang": request.POST.get("nama_belakang"),
            "no_telepon": request.POST.get("no_telepon"),
            "role": peran,
            "id_staf": id_staf
        }
        
        if request.POST.get("password") != request.POST.get("confirm_password"):
            messages.error(request, "Konfirmasi password tidak cocok.")
            return redirect("authentication:register_pengunjung") 
        
        AuthService.create_profile(data)
        messages.success(request, "Registrasi berhasil. Silakan login.")
        return redirect("authentication:login")

    return render(request, 'register/staf.html')

def profile_view(request):
    if not request.user.get("is_authenticated"):
        return redirect("authentication:login")

    role = request.user["role"]
    username = request.user["username"]
    
    data = AuthService.get_user_detail(username)

    if role == "Pengunjung":
        print(data)
        return render(request, "profile/pengunjung.html", {"data_pengunjung": data})
    elif role == "Dokter Hewan":
        return render(request, "profile/dokter_hewan.html", {"data_profile": data})
    elif role == "Penjaga Hewan":
        return render(request, "profile/penjaga_hewan.html", {"data_profile": data})
    elif role == "Pelatih Hewan":
        return render(request, "profile/pelatih_hewan.html", {"data_profile": data})
    elif role == "Staf Admin":
        return render(request, "profile/staf_admin.html", {"data_profile": data})
    else:
        messages.error(request, "Peran tidak dikenali.")
        return redirect("authentication:login")

def update_profile_view(request):
    if not request.user.get("is_authenticated"):
        return redirect("authentication:login")
    
    role = request.user["role"]
    username = request.user["username"]
    data = AuthService.get_user_detail(username)
    
    if request.method == 'POST':
        updated_data = {
            "username": username,
            "nama_depan": request.POST.get("nama_depan"),
            "nama_tengah": request.POST.get("nama_tengah"),
            "nama_belakang": request.POST.get("nama_belakang"),
            "email": request.POST.get("email"),
            "no_telepon": request.POST.get("no_telepon"),
            "role": role
        }
        if role == 'Pengunjung':
            updated_data["alamat"] = request.POST.get("alamat")
            updated_data["tgl_lahir"] = request.POST.get("tanggal_lahir")
        elif role == 'Dokter Hewan':
            updated_data["no_str"] = request.POST.get("no_str")
            updated_data["spesialisasi"] = request.POST.getlist("spesialisasi")
            lainnya = request.POST.get("spesialisasi_lainnya")
            if lainnya:
                updated_data["spesialisasi"].append(lainnya)
        elif role in ["Penjaga Hewan", "Pelatih Hewan", "Staf Admin"]:
            updated_data["id_staf"] = request.POST.get("id_staf")
        
        AuthService.update_profile(updated_data)
        messages.success(request, "Profil berhasil diperbarui.")
        return redirect("authentication:profile_pengguna")
    
    template = ""
    if role == "Pengunjung":
        template = "profile/pengunjung.html"
        context_name = "data_pengunjung"
    elif role == "Dokter Hewan":
        template = "profile/dokter_hewan.html"
        context_name = "data_profile"
    elif role in ["Penjaga Hewan", "Pelatih Hewan", "Staf Admin"]:
        template = "profile/staf.html"
        context_name = "data_profile"
    else:
        messages.error(request, "Peran tidak dikenali.")
        return redirect("authentication:login")
    return render(request, template, {context_name: data})

def logout_view(request):
    response = redirect("authentication:login")
    response.delete_cookie("jwt")
    return response