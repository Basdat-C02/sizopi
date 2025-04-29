from django.shortcuts import render

# Create your views here.
def daftar_habitat_view(request):
    habitat = [
        {
            "nama": "Wetlands",
            "luas_area": 940.58,
            "kapasitas": 90,
            "status": "Habitat berair dengan kelembapan tinggi, ditumbuhi rerumputan air, suhu hangat hingga sedang."
        },
        {
            "nama": "Tundra",
            "luas_area": 544.68,
            "kapasitas": 87,
            "status": "Wilayah dingin ekstrem dengan tanah beku (permafrost), vegetasi rendah seperti lumut dan semak."
        },
        {
            "nama": "Savanna",
            "luas_area": 912.13,
            "kapasitas": 100,
            "status": "Padang rumput luas dengan pohon tersebar, iklim tropis dengan musim hujan dan kemarau yang kering."
        },
        {
            "nama": "Rainforest",
            "luas_area": 736.25,
            "kapasitas": 31,
            "status": "Hutan lebat dengan curah hujan tinggi, kelembapan sangat tinggi, dan vegetasi yang sangat beragam."
        },
        {
            "nama": "Desert",
            "luas_area": 801.73,
            "kapasitas": 79,
            "status": "Wilayah sangat kering dengan suhu ekstrem, sedikit vegetasi seperti kaktus dan semak tahan panas."
        },
        {
            "nama": "Arctic",
            "luas_area": 779.28,
            "kapasitas": 25,
            "status": "Daerah beku dengan suhu sangat rendah sepanjang tahun, ditutupi es dan salju permanen."
        },
        {
            "nama": "Coral Reef",
            "luas_area": 687.11,
            "kapasitas": 45,
            "status": "Ekosistem laut tropis dengan air jernih, suhu hangat, dan biodiversitas laut yang tinggi."
        },
        {
            "nama": "Grasslands",
            "luas_area": 660.16,
            "kapasitas": 92,
            "status": "Padang rumput luas beriklim sedang hingga kering, mendukung tumbuhan pendek seperti rumput dan bunga liar."
        }
    ]
    context = {
        'daftar_habitat': habitat,
        'user_role': 'penjaga_hewan',
        'is_authenticated': True,
    }
    return render(request, 'daftar_habitat/index.html', context)

def add_habitat_view(request):
    if request.method == 'POST':
        # Handle form submission to add a new habitat
        pass  # Implement your logic here
    context = {
        'user_role': 'penjaga_hewan',
        'is_authenticated': True,
    }
    return render(request, 'add_habitat/index.html', context)

def edit_habitat_view(request):
    data = {
        "nama": "Savanna",
        "luas_area": 912.13,
        "kapasitas": 100,
        "status": "Padang rumput luas dengan pohon tersebar, iklim tropis dengan musim hujan dan kemarau yang kering."
    }
    context = {
        'habitat': data,
        'user_role': 'penjaga_hewan',
        'is_authenticated': True,
    }
    return render(request, 'edit_habitat/index.html', context)

def detail_habitat_view(request):
    # Fetch habitat details based on habitat_id
    habitat = {
        "nama": "Savanna",
        "luas_area": 912.13,
        "kapasitas": 100,
        "status": "Padang rumput luas dengan pohon tersebar, iklim tropis dengan musim hujan dan kemarau yang kering."
    }
    daftar_hewan = [
        {
            "nama": "Leo",
            "spesies": "Panthera leo",
            "asal_hewan": "Afrika",
            "tanggal_lahir": "2018-06-15",
            "status_kesehatan": "Sehat",
        },
        {
            "nama": "Nala",
            "spesies": "Panthera leo",
            "asal_hewan": "Afrika",
            "tanggal_lahir": "2019-04-12",
            "status_kesehatan": "Sehat",
        },
        {
            "nama": "Simba",
            "spesies": "Panthera leo",
            "asal_hewan": "Afrika",
            "tanggal_lahir": "2017-03-10",
            "status_kesehatan": "Sehat",
        },
        {
            "nama": "Toby",
            "spesies": "Struthio camelus",
            "asal_hewan": "Afrika",
            "tanggal_lahir": "2015-04-07",
            "status_kesehatan": "Sehat",
        },
        {
            "nama": "Trixie",
            "spesies": "Giraffa camelopardalis",
            "asal_hewan": "Afrika",
            "tanggal_lahir": "2015-03-21",
            "status_kesehatan": "Sehat",
        },
        {
            "nama": "Ellie",
            "spesies": "Loxodonta africana",
            "asal_hewan": "Afrika",
            "tanggal_lahir": "2014-11-11",
            "status_kesehatan": "Sakit",
        },
        {
            "nama": "Hazel",
            "spesies": "Hyaena hyaena",
            "asal_hewan": "Afrika",
            "tanggal_lahir": "2015-12-24",
            "status_kesehatan": "Sakit",
        }
    ]

    context = {
        'habitat': habitat,
        'daftar_hewan' : daftar_hewan,
        'user_role': 'penjaga_hewan',
        'is_authenticated': True,
    }
    return render(request, 'detail_habitat/index.html', context)