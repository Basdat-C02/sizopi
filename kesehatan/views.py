from django.shortcuts import render, redirect

# ================ REKAM MEDIS HEWAN ================
def list_rekam_medis(request):
    hewan_list = [
        {
            'id': '6883e846-f894-40be-9282-30c29169e852',
            'nama': 'Leo',
            'spesies': 'Panthera leo',
            'status_kesehatan': 'Sehat',
            'url_foto': 'https://example.com/leo.jpg',
        },
        {
            'id': '94fc7265-5f8f-434a-afa0-0c5d5599c21c',
            'nama': 'Nala',
            'spesies': 'Panthera leo',
            'status_kesehatan': 'Sakit',
            'url_foto': 'https://example.com/nala.jpg',
        },
        {
            'id': '64a42f19-f82e-4a72-ba6f-3d3ff0c5a3c0',
            'nama': 'Koko',
            'spesies': 'Cacatua galerita',
            'status_kesehatan': 'Sehat',
            'url_foto': 'https://example.com/koko.jpg',
        },
    ]
    
    context = {
        'hewan_list': hewan_list
    }
    return render(request, 'list_rekam_medis.html', context)


def rekam_medis_hewan(request, pk):
    catatan_medis_list = [
        {
            'id_hewan': '6883e846-f894-40be-9282-30c29169e852',
            'username_dh': 'farhan.nur',
            'tanggal_pemeriksaan': '2025-04-01',
            'diagnosis': 'Infeksi kulit',
            'pengobatan': 'Salep antibiotik',
            'status_kesehatan': 'Sehat',
            'catatan_tindak_lanjut': ''
        },
        {
            'id_hewan': '94fc7265-5f8f-434a-afa0-0c5d5599c21c',
            'username_dh': 'citra.melati',
            'tanggal_pemeriksaan': '2025-04-02',
            'diagnosis': 'Cacingan',
            'pengobatan': 'Obat cacing',
            'status_kesehatan': 'Sakit',
            'catatan_tindak_lanjut': ''
        },
        {
            'id_hewan': '64a42f19-f82e-4a72-ba6f-3d3ff0c5a3c0',
            'username_dh': 'dwi.ananda',
            'tanggal_pemeriksaan': '2025-04-05',
            'diagnosis': 'Patah tulang',
            'pengobatan': 'Operasi dan gips',
            'status_kesehatan': 'Sehat',
            'catatan_tindak_lanjut': ''
        },
    ]

    catatan_medis_hewan = [catatan for catatan in catatan_medis_list if catatan['id_hewan'] == str(pk)]

    context = {
        'catatan_medis': catatan_medis_hewan,
        'id_hewan': pk,
    }

    return render(request, 'rekam_medis_hewan.html', context)


def edit_rekam_medis(request, pk):
    dummy_data = {
        'catatan_tindak_lanjut': '',
        'diagnosis': '',
        'pengobatan': '',
    }

    if request.method == 'POST':
        # Edit logic
        return redirect('kesehatan:rekam_medis_hewan', pk=pk)

    return render(request, 'edit_rekam_medis.html', {'catatan': dummy_data, 'pk': pk})

def create_rekam_medis(request, pk):
    dummy_data = {
        'tanggal_pemeriksaan': '',
        'nama_dokter': '',
        'status_kesehatan': '',
        'diagnosis': '',
        'pengobatan': '',
        'catatan_tindak_lanjut': ''
    }

    if request.method == 'POST':
        # Create logic
        return redirect('kesehatan:rekam_medis_hewan', pk=pk)
    
    context = {
        'form_data': dummy_data,
    }

    return render(request, 'create_rekam_medis.html', context)

def delete_rekam_medis(request, pk):
    if request.method == 'POST':
        # Delete logic
        return redirect('kesehatan:list_rekam_medis')
    
    context = {
        'pk': pk,
    }
    
    return render(request, 'delete_rekam_medis.html', context)


# ================ PENJADWALAN PEMERIKSAAN KESEHATAN ================
def jadwal_pemeriksaan(request, pk):  
    jadwal_list = [
        {
            'id_hewan': '6883e846-f894-40be-9282-30c29169e852',
            'freq_pemeriksaan_rutin': 30,
            'tgl_pemeriksaan_selanjutnya': '2025-06-01',
        },
        {
            'id_hewan': '2',
            'freq_pemeriksaan_rutin': 60,
            'tgl_pemeriksaan_selanjutnya': '2025-06-02',
        },
    ]

    jadwal_list_hewan = [jadwal for jadwal in jadwal_list if jadwal['id_hewan'] == str(pk)]
    
    context = {
        'jadwal_list': jadwal_list_hewan,
        'id_hewan': pk,
    }

    return render(request, 'jadwal_pemeriksaan.html', context)

def create_jadwal_pemeriksaan(request, pk):
    if request.POST:
        # Create logic
        return redirect('kesehatan:jadwal_pemeriksaan', pk=pk)
    
def edit_jadwal_pemeriksaan(request, pk):
    if request.POST:
        # Edit logic
        return redirect('kesehatan:jadwal_pemeriksaan', pk=pk)
    
def delete_jadwal_pemeriksaan(request, pk):
    if request.POST:
        # Delete logic
        return redirect('kesehatan:jadwal_pemeriksaan', pk=pk)

def edit_freq_pemeriksaan(request, pk):
    if request.POST:
        # Edit freq pemeriksaan logic
        return redirect('kesehatan:jadwal_pemeriksaan', pk=pk)
    

# ================ PEMBERIAN PAKAN ================
def pemberian_pakan(request, pk):
    jadwal_list = [
        {
            'jenis_pakan': 'Daging',
            'pakan': {
                'id_hewan': '6883e846-f894-40be-9282-30c29169e852',
                'jadwal': '2025-04-01 08:00:00',
                'jenis': 'Daging',
                'jumlah': 500,
                'status': 'Selesai Diberikan'
            },
            'username_jh': 'adi.susanto',
        },
        {
            'jenis_pakan': 'Ikan Segar',
            'pakan': {
                'id_hewan': '6883e846-f894-40be-9282-30c29169e852',
                'jadwal': '2025-04-01 12:00:00',
                'jenis': 'Ikan Segar',
                'jumlah': 600,
                'status': 'Menunggu Pemberian'
            },
            'username_jh': 'fitri.nuraini',
        }
    ]

    context = {
        'jadwal_list': jadwal_list,
        'id_hewan': pk,
    }

    return render(request, 'pemberian_pakan.html', context)

def create_pemberian_pakan(request, pk):
    if request.POST:
        # Create logic
        return redirect("kesehatan:pemberian_pakan", pk=pk)

def update_pemberian_pakan(request, pk):
    if request.POST:
        # Update logic
        return redirect("kesehatan:pemberian_pakan", pk=pk)

def delete_pemberian_pakan(request, pk):
    if request.POST:
        # Delete logic
        return redirect("kesehatan:pemberian_pakan", pk=pk)
    
def beri_pakan(request, pk):
    if request.POST:
        # Beri pakan logic
        return redirect("kesehatan:pemberian_pakan", pk=pk)
    
def riwayat_pemberian_pakan(request):
    pemberian = [
        {
            'jenis_pakan': 'Daging',
            'pakan': {
                'hewan': {
                    'id': '6883e846-f894-40be-9282-30c29169e852',
                    'nama': 'Leo',
                    'spesies': 'Singa',
                    'tanggal_lahir': '2020-01-01',
                    'status_kesehatan': 'Sehat',
                    'nama_habitat': 'Savanna',
                    'url_foto': 'https://media.istockphoto.com/id/1286270203/photo/african-lion-sitting.jpg?s=612x612&w=0&k=20&c=8ULxT0Wm-Hys4DtZO1UQq0E6dFbpaOpjJ3TaOOGOKyU='
                },
                'jadwal': '2025-04-01 08:00:00',
                'jenis': 'Daging',
                'jumlah': 500,
                'status': 'Selesai Diberikan'
            },
            'username_jh': 'adi.susanto',
        },
        {
            'jenis_pakan': 'Biji-bijian',
            'pakan': {
                'hewan': {
                    'id': '64a42f19-f82e-4a72-ba6f-3d3ff0c5a3c0',
                    'nama': 'Koko',
                    'spesies': 'Kakatua jambul kuning',
                    'tanggal_lahir': '2020-02-20',
                    'status_kesehatan': 'Sehat',
                    'nama_habitat': 'Rainforest',
                    'url_foto': 'https://media.istockphoto.com/id/1471333561/photo/white-cockatoo-or-kakatua-putih.jpg?s=612x612&w=0&k=20&c=foE2zDycJnhcIS9rR6-lV32nOXrydmPns0ErzUCF5dk='
                },
                'jadwal': '2025-04-01 09:00:00',
                'jenis': 'Biji-bijian',
                'jumlah': 50,
                'status': 'Menunggu Pemberian'
            },
            'username_jh': 'adi.susanto',
        }
    ]

    context = {
        'pemberian': pemberian,
    }

    return render(request, 'riwayat_pemberian_pakan.html', context)

