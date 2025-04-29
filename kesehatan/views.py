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
            'status_kesehatan': 'Sedang',
            'catatan_tindak_lanjut': ''
        },
        {
            'id_hewan': '94fc7265-5f8f-434a-afa0-0c5d5599c21c',
            'username_dh': 'citra.melati',
            'tanggal_pemeriksaan': '2025-04-02',
            'diagnosis': 'Cacingan',
            'pengobatan': 'Obat cacing',
            'status_kesehatan': 'Baik',
            'catatan_tindak_lanjut': ''
        },
        {
            'id_hewan': '64a42f19-f82e-4a72-ba6f-3d3ff0c5a3c0',
            'username_dh': 'dwi.ananda',
            'tanggal_pemeriksaan': '2025-04-05',
            'diagnosis': 'Patah tulang',
            'pengobatan': 'Operasi dan gips',
            'status_kesehatan': 'Kritis',
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
