from django.shortcuts import render

# Create your views here.

def add_satwa_view(request):
    status_kesehatan = [
        'Sehat',
        'Sakit',
        'Luka',
        'Mati'
    ]
    
    daftar_habitat = [
        'Hutan',
        'Sungai',
        'Laut',
        'Padang Rumput'
    ]
    
    context = {
        'status_kesehatan': status_kesehatan,
        'daftar_habitat': daftar_habitat,
    }

    return render(request, 'add_satwa/index.html', context)