from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'main/index.html')

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

def profile_pengunjung_view(request):
    pengunjung_data = {
        "nama_lengkap": "Alya Putri Ramadhani",
        "username": "alya.ramadhani",
        "email": "alya.ramadhani@gmail.com",
        "no_telepon": "6281234567890",
        "peran": "Pengunjung",
        "alamat_lengkap": "Jl. Mawar No. 23, Bandung, Jawa Barat, Indonesia",
        "tanggal_lahir": "2001-07-15",
        "riwayat_kunjungan": [
            {
                "nama_atraksi": "Safari Malam",
                "lokasi": "Zona Savanna",
                "tanggal_kunjungan": "2024-11-20",
                "status_reservasi": "Sukses"
            },
            {
                "nama_atraksi": "Pertunjukan Burung",
                "lokasi": "Amphitheater",
                "tanggal_kunjungan": "2025-01-05",
                "status_reservasi": "Sukses"
            },
            {
                "nama_atraksi": "Interaksi Satwa Jinak",
                "lokasi": "Zona Hutan Tropis",
                "tanggal_kunjungan": "2025-03-12",
                "status_reservasi": "Sukses"
            }
        ],
        "informasi_tiket_dibeli": [
            {
                "nama_atraksi": "Safari Malam",
                "jumlah_tiket": 2
            },
            {
                "nama_atraksi": "Pertunjukan Burung",
                "jumlah_tiket": 1
            },
            {
                "nama_atraksi": "Interaksi Satwa Jinak",
                "jumlah_tiket": 3
            }
        ]
    }
    context = {
        'data_pengunjung': pengunjung_data,
    }
    return render(request, 'profile/pengunjung.html', context)

def profile_dokter_hewan_view(request):
    data_profile = {
        'nama_lengkap': 'Farhan Nur Hakim',
        'username': 'farhan.nur',
        'email': 'farhan.hakim@gmail.com',
        'nomor_telepon': '081234568050',
        'peran': 'Dokter Hewan',
        'no_str': 'STR-001',
        'spesialisasi': ['Bedah Hewan', 'Mamalia Besar'],
        'jumlah_hewan_ditangani': 45
    }
    return render(request, 'profile/dokter_hewan.html', {'data_profile': data_profile})

def profile_penjaga_hewan_view(request):
    data_profile = {
        'nama_lengkap': 'Bima Prasetya',
        'username': 'bima.prasetya',
        'email': 'bima.prasetya@gmail.com',
        'nomor_telepon': '081234567892',
        'peran': 'Penjaga Hewan',
        'id_staf': '3265abbf-8b32-4f94-b4f1-b3bb5567bff0',
        'jumlah_hewan_diberi_pakan': 120
    }
    return render(request, 'profile/penjaga_hewan.html', {'data_profile': data_profile})

def profile_staf_admin_view(request):
    data_profile = {
        'nama_lengkap': 'Ariq Maulana Malik',
        'username': 'ariq.maulana',
        'email': 'ariq.maulana@gmail.com',
        'nomor_telepon': '081234568090',
        'peran': 'Staf Administrasi',
        'id_staf': 'a404d027-154b-49a6-bb7a-6a21e686eb5a',
        'ringkasan_penjualan_tiket': 1500000,
        'jumlah_pengunjung_hari_ini': 320,
        'laporan_pendapatan_mingguan': 9500000
    }
    return render(request, 'profile/staf_admin.html', {'data_profile': data_profile})

def profile_pelatih_hewan_view(request):
    data_profile = {
        'nama_lengkap': 'Amanda Putri',
        'username': 'amanda.putri',
        'email': 'amanda.putri@gmail.com',
        'nomor_telepon': '081234568080',
        'peran': 'Staf Pelatih Pertunjukan',
        'id_staf': '3e02c96a-b6db-4e03-b8ba-0baf1021eb56',
        'jadwal_pertunjukan_hari_ini': [
            {
                'waktu': '2025-05-01 07:00:00',
                'nama_pertunjukan': 'Pertunjukan Singa'
            },
            {
                'waktu': '2025-05-01 09:00:00',
                'nama_pertunjukan': 'Atraksi Burung'
            }
        ],
        'daftar_hewan_dilatih': ['Singa Leo', 'Burung Koko'],
    }
    return render(request, 'profile/pelatih.html', {'data_profile': data_profile})