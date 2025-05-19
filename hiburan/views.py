from django.shortcuts import render
pelatih_list = [
    'Amanda Putri',
    'Bobby Maulana',
    'Citra Anindya',
    'David Susanto',
    'Eka Prasetya',
    'Farah Amalia',
    'Gilang Satriya',
    'Hana Mabel',
    'Indra Nugraha',
    'Jessica Rahma'
]
user_role = 'staf_admin'
reservasi = [{
    "id": "c5c3f0f6-37eb-43ae-8566-9f80413a6e74",
    "nama_atraksi": "Pertunjukan lumba-lumba",
    "lokasi": "Area Akuatik",
    "jam": "10:00",
    "tanggal": "12 Mei 2025",
    "jumlah_tiket": 10,
    "status": "Terjadwal"
}]

# Create your views here.
def fasilitas_menu(request):
    context = {
            'user_role': user_role,
            'is_authenticated': True
            }
    return render(request, 'menu.html', context)

# -- page atraksi --
def data_atraksi_view(request):
    atraksi = [
    {
        'nama': 'Atraksi Lumba-lumba',
        'lokasi': 'Zona Laut',
        'kapasitas': 70,
        'jadwal': '2025-05-06 10:00:00',
        'hewan_terlibat': ['Leo', 'Nala'],
        'pelatih': ''
    },
    {
        'nama': 'Pertunjukan Harimau',
        'lokasi': 'Blok A',
        'kapasitas': 80,
        'jadwal': '2025-05-07 16:00:00',
        'hewan_terlibat': ['Koko', 'Polly'],
        'pelatih': ''
    },
    {
        'nama': 'Kebun Binatang Mini',
        'lokasi': 'Taman Fauna',
        'kapasitas': 40,
        'jadwal': '2025-05-08 09:30:00',
        'hewan_terlibat': ['Rocky', 'Charlie'],
        'pelatih': ''
    },
    {
        'nama': 'Atraksi Gajah',
        'lokasi': 'Zona Gajah',
        'kapasitas': 25,
        'jadwal': '2025-05-09 11:00:00',
        'hewan_terlibat': ['Luna', 'Oscar'],
        'pelatih': ''
    },
    {
        'nama': 'Pertunjukan Kuda',
        'lokasi': 'Lapangan Kuda',
        'kapasitas': 90,
        'jadwal': '2025-05-10 14:30:00',
        'hewan_terlibat': ['Cleo'],
        'pelatih': ''
    },
    {
        'nama': 'Sirkus Singa',
        'lokasi': 'Panggung Sirkus',
        'kapasitas': 50,
        'jadwal': '2025-05-11 15:00:00',
        'hewan_terlibat': ['Max'],
        'pelatih': ''
    },
    {
        'nama': 'Atraksi Ular',
        'lokasi': 'Zona Ular',
        'kapasitas': 35,
        'jadwal': '2025-05-12 12:00:00',
        'hewan_terlibat': [],
        'pelatih': ''
    },
    {
        'nama': 'Kandang Kuda',
        'lokasi': 'Blok Kuda',
        'kapasitas': 45,
        'jadwal': '2025-05-13 10:30:00',
        'hewan_terlibat': [],
        'pelatih': ''
    }
    ]
    context = {
        'user_role': user_role, 
            'is_authenticated': True,
        'atraksi_entries': atraksi,
    }

    return render(request, 'atraksi/data.html', context)

def create_atraksi_view(request):
    context = {
        'user_role': user_role,
        'is_authenticated': True,
        'pelatih_list': pelatih_list
    }
    return render(request, 'atraksi/create.html', context)

def edit_atraksi_view(request, nama):
    context = {
        'user_role': user_role, 
        'nama': nama,
        'is_authenticated': True,
        'pelatih_list': pelatih_list
    }
    return render(request, 'atraksi/edit.html', context)

def delete_atraksi_view(request):
    return render(request, 'atraksi/delete.html')

# -- page wahana --
def data_wahana_view(request):
    wahana = [
    {
        'nama': 'Arung Jeram',
        'kapasitas': 50,
        'jadwal': '2025-05-01 09:00:00',
        'peraturan': 'Pengunjung wajib mengenakan pelampung dan mengikuti instruksi pemandu saat melakukan arung jeram.'
    },
    {
        'nama': 'Bianglala',
        'kapasitas': 100,
        'jadwal': '2025-05-02 14:00:00',
        'peraturan': 'Pengunjung harus duduk dengan aman di kursi dan mematuhi batas tinggi badan yang ditentukan.'
    },
    {
        'nama': 'Roller Coaster',
        'kapasitas': 20,
        'jadwal': '2025-05-03 10:00:00',
        'peraturan': 'Pengunjung harus duduk dengan aman, mengenakan pengaman, dan mengikuti instruksi operator sebelum naik roller coaster.'
    },
    {
        'nama': 'Komedi Putar',
        'kapasitas': 30,
        'jadwal': '2025-05-04 11:00:00',
        'peraturan': 'Dilarang membawa barang tajam dan pengunjung wajib duduk di tempat yang telah disediakan.'
    },
    {
        'nama': 'Kora-kora',
        'kapasitas': 60,
        'jadwal': '2025-05-05 13:00:00',
        'peraturan': 'Pengunjung harus mematuhi petunjuk keselamatan dan tidak diperbolehkan berdiri selama wahana bergerak.'
    },
]
    context = {
        'user_role': user_role,
        'is_authenticated': True,
        'wahana_entries': wahana
    }
    return render(request, 'wahana/data.html', context)

def create_wahana_view(request):
    context = {
        'is_authenticated': True,
        'user_role': user_role,
    }
    return render(request, 'wahana/create.html', context)

def edit_wahana_view(request, nama):
    context = {
        'is_authenticated': True,
        'user_role': user_role,
        'nama': nama
    }
    return render(request, 'wahana/edit.html', context)

def delete_wahana_view(request):
    return render(request, 'wahana/delete.html')

# -- page reservasi --
def data_reservasi_view(request):
    context = {
        'is_authenticated': True,
        'user_role': user_role,
        'reservasi': reservasi,
    }
    return render(request, 'reservasi/data.html', context)

def create_reservasi_view(request):
    context = {
        'is_authenticated': True,
        'user_role': user_role,
    }
    return render(request, 'reservasi/create.html', context)

def detail_reservasi_view(request, id):
    context = {
        'is_authenticated': True,
        'user_role': user_role,
        'reservasi': reservasi,
        'id': id
    }
    return render(request, 'reservasi/detail.html', context)

def edit_reservasi_view(request, id):
    context = {
        'is_authenticated': True,
        'user_role': user_role,
        'id': id
    }
    return render(request, 'reservasi/edit.html', context)

def delete_reservasi_view(request, id):
    return render(request, 'reservasi/delete.html')
