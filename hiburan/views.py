from django.shortcuts import render

# Create your views here.
def fasilitas_menu(request):
    return render(request, 'menu.html')

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
    'atraksi_entries': atraksi,
    }

    return render(request, 'atraksi/data.html', context)

def create_atraksi_view(request):
    return render(request, 'atraksi/create.html')

def edit_atraksi_view(request):
    return render(request, 'atraksi/edit.html')

def delete_atraksi_view(request):
    return render(request, 'atraksi/delete.html')

# -- page wahana --
def data_wahana_view(request):
    return render(request, 'wahana/data.html')

def create_wahana_view(request):
    return render(request, 'wahana/create.html')

def edit_wahana_view(request):
    return render(request, 'wahana/edit.html')

def delete_wahana_view(request):
    return render(request, 'wahana/delete.html')

# -- page reservasi --
def data_reservasi_view(request):
    return render(request, 'reservasi/data.html')

def create_reservasi_view(request):
    return render(request, 'reservasi/create.html')

def read_reservasi_view(request):
    return render(request, 'reservasi/read.html')

def edit_reservasi_view(request):
    return render(request, 'reservasi/edit.html')

def delete_reservasi_view(request):
    return render(request, 'reservasi/delete.html')
