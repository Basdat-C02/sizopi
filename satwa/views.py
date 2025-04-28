from django.shortcuts import render

# Create your views here.

def add_satwa_view(request):
    status_kesehatan = [
        'Sehat',
        'Sakit',
        'Dalam Pemantauan',
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

def daftar_satwa_view(request):
    # Dummy data for demonstration purposes
    daftar_satwa = [
        {
            'nama': 'Khan',
            'spesies': 'Harimau',
            'asal_hewan': 'Sumatera',
            'tanggal_lahir': '2015-06-15',
            'status_kesehatan': 'Sehat',
            'habitat': 'Hutan',
            'foto': 'https://media.4-paws.org/6/1/9/0/61905f50890c481987d29191ff0c2aa89d41e822/VIER%20PFOTEN_2022-05-18_00011-2890x2000.jpg',
        },
        {
            'nama': 'Ellie',
            'spesies': 'Gajah',
            'asal_hewan': 'Asia',
            'tanggal_lahir': '2010-03-20',
            'status_kesehatan': 'Sakit',
            'habitat': 'Hutan',
            'foto': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSMn4brZ_2miUn4OOUpfEJNP_iYymn5Cllf2Q&s',
        },
        {
            'nama': 'Marty',
            'spesies': 'Zebra',
            'asal_hewan': 'Afrika',
            'tanggal_lahir': '2018-01-05',
            'status_kesehatan': 'Dalam Pemantauan',
            'habitat': 'Padang Rumput',
            'foto': 'https://media.istockphoto.com/id/1086990568/photo/zebra-in-kalahari-desert.jpg?s=1024x1024&w=is&k=20&c=uKIP_sueIR43Y1z6JmhBgA9RDaslOwHB2F-kaxX2xcQ=',
        },
        {
            'nama': 'Bimo',
            'spesies': 'Orangutan',
            'asal_hewan': 'Kalimantan',
            'tanggal_lahir': '2012-11-10',
            'status_kesehatan': 'Luka',
            'habitat': 'Hutan',
            'foto': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQYXQy2G99oP_h3T71qkrCT3Y44DA5reQBd0g&s',
        },
    ]

    context = {
        'daftar_satwa': daftar_satwa,
    }

    return render(request, 'daftar_satwa/index.html', context)