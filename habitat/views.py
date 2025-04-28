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
    }
    return render(request, 'daftar_habitat/index.html', context)