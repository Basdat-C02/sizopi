from django.shortcuts import render

def main_staff(request):
    # Contoh data hewan
    animals = [
        {'name': 'Simba', 'type': 'Singa', 'status': 'Diadopsi', 'condition': 'Sehat'},
        {'name': 'Melly', 'type': 'Gajah', 'status': 'Tidak Diadopsi', 'condition': 'Baik'},
    ]
    return render(request, 'adoption_main_staff.html', {'animals': animals})

def main_adopter(request):
    # Contoh data adopter
    adopted_animals = [
        {'name': 'Simba', 'type': 'Singa', 'condition': 'Sehat'},
    ]
    return render(request, 'adoption_main_adopter.html', {'animals': adopted_animals})

def detail_modal(request, animal_id):
    # Logika untuk detail hewan
    return render(request, 'adoption_detail_modal.html')

def register_adopter(request):
    # Logika form pendaftaran
    return render(request, 'adoption_form.html')

def adopter_history(request):
    # Logika riwayat adopter
    return render(request, 'adopter_history.html')

def certificate(request, animal_id):
    # Logika sertifikat
    return render(request, 'certificate.html')

def extend_adoption(request, animal_id):
    # Logika perpanjangan
    return render(request, 'extend_adoption.html')