from django.shortcuts import render

# Create your views here.
# -- page atraksi --
def data_atraksi_view(request):
    atraksi = [
        {
            'nama': '',
            'lokasi': '',
            'kapasitas': '',
            'jadwal': '',
            'hewan_terlibat': '',
            'pelatih': ''
        }
    ]
    return render(request, 'atraksi/data.html')

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
