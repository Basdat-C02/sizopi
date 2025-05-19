from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime, timedelta
import uuid

DUMMY_HEWAN = [
    {
        'id': uuid.UUID('550e8400-e29b-41d4-a716-446655440000'),
        'nama': 'Simba',
        'spesies': 'Singa',
        'asal_hewan': 'Afrika',
        'tanggal_lahir': '2018-05-10',
        'status_kesehatan': 'Sehat',
        'nama_habitat': 'Savanna',
        'url_foto': 'https://www.ruparupa.com/blog/wp-content/uploads/2021/03/james-park-UBYXP8aaGN4-unsplash.jpg'
    },
    {
        'id': uuid.UUID('550e8400-e29b-41d4-a716-446655440001'),
        'nama': 'Dumbo',
        'spesies': 'Gajah Asia',
        'asal_hewan': 'Sumatera',
        'tanggal_lahir': '2015-03-20',
        'status_kesehatan': 'Sehat',
        'nama_habitat': 'Hutan',
        'url_foto': 'https://www.ruparupa.com/blog/wp-content/uploads/2021/03/james-park-UBYXP8aaGN4-unsplash.jpg'
    },
    {
        'id': uuid.UUID('550e8400-e29b-41d4-a716-446655440002'),
        'nama': 'Joko',
        'spesies': 'Harimau Sumatera',
        'asal_hewan': 'Sumatera',
        'tanggal_lahir': '2017-08-15',
        'status_kesehatan': 'Pemulihan',
        'nama_habitat': 'Hutan',
        'url_foto': 'https://www.ruparupa.com/blog/wp-content/uploads/2021/03/james-park-UBYXP8aaGN4-unsplash.jpg'
    }
]

DUMMY_ADOPTER = [
    {
        'username_adopter': 'john_doe',
        'id_adopter': uuid.UUID('660e8400-e29b-41d4-a716-446655440000'),
        'total_kontribusi': 1500000
    },
    {
        'username_adopter': 'eco_corp',
        'id_adopter': uuid.UUID('660e8400-e29b-41d4-a716-446655440001'),
        'total_kontribusi': 2500000
    }
]

DUMMY_INDIVIDU = [
    {
        'nik': '1234567890123456',
        'nama': 'John Doe',
        'id_adopter': uuid.UUID('660e8400-e29b-41d4-a716-446655440000')
    }
]

DUMMY_ORGANISASI = [
    {
        'npp': '87654321',
        'nama_organisasi': 'Eco Corp',
        'id_adopter': uuid.UUID('660e8400-e29b-41d4-a716-446655440001')
    }
]

DUMMY_ADOPSI = [
    {
        'id_adopter': uuid.UUID('660e8400-e29b-41d4-a716-446655440000'),
        'id_hewan': uuid.UUID('550e8400-e29b-41d4-a716-446655440000'),
        'status_pembayaran': 'Lunas',
        'tgl_mulai_adopsi': datetime.now() - timedelta(days=60),
        'tgl_berhenti_adopsi': datetime.now() + timedelta(days=120),
        'kontribusi_finansial': 500000
    },
    {
        'id_adopter': uuid.UUID('660e8400-e29b-41d4-a716-446655440001'),
        'id_hewan': uuid.UUID('550e8400-e29b-41d4-a716-446655440001'),
        'status_pembayaran': 'Tertunda',
        'tgl_mulai_adopsi': datetime.now() - timedelta(days=30),
        'tgl_berhenti_adopsi': datetime.now() + timedelta(days=60),
        'kontribusi_finansial': 700000
    }
]

DUMMY_STAF_ADMIN = [
    {'username_sa': 'admin', 'id_staf': uuid.UUID('770e8400-e29b-41d4-a716-446655440000')}
]

DUMMY_REKAM_MEDIS = [
    {
        'id_hewan': uuid.UUID('550e8400-e29b-41d4-a716-446655440000'),  # Singa
        'tanggal_pemeriksaan': '2025-04-01',
        'nama_dokter': 'Dr. Siti Aminah',
        'status_kesehatan': 'Sakit',
        'diagnosa': 'Infeksi saluran pernapasan',
        'pengobatan': 'Antibiotik selama 7 hari',
        'catatan_tindak_lanjut': 'Evaluasi kondisi perbaikan ventilasi kandang.'
    },
    {
        'id_hewan': uuid.UUID('550e8400-e29b-41d4-a716-446655440000'),  # Singa
        'tanggal_pemeriksaan': '2025-04-15',
        'nama_dokter': 'Dr. Siti Aminah',
        'status_kesehatan': 'Pemulihan',
        'diagnosa': 'Pasca infeksi saluran pernapasan',
        'pengobatan': 'Vitamin dan suplemen',
        'catatan_tindak_lanjut': 'Monitoring kondisi pernapasan selama 2 minggu.'
    },
    {
        'id_hewan': uuid.UUID('550e8400-e29b-41d4-a716-446655440001'),  # Gajah
        'tanggal_pemeriksaan': '2025-03-25',
        'nama_dokter': 'Dr. Budi Santoso',
        'status_kesehatan': 'Sehat',
        'diagnosa': 'Pemeriksaan rutin',
        'pengobatan': 'Tidak ada',
        'catatan_tindak_lanjut': 'Lanjutkan pemantauan diet dan aktivitas.'
    }
]

def status_adopsi(request):
    """View untuk menampilkan status adopsi hewan"""
    # Mendapatkan role dari parameter GET
    role = request.GET.get('role', 'visitor')  # Default sebagai visitor
    role = 'admin'
    # Simulasi username berdasarkan role
    if role == 'admin':
        username = 'admin'
        is_staff = True
    elif role == 'adopter':
        username = 'john_doe'
        is_staff = False
    else:
        # Default pengunjung biasa
        username = 'visitor'
        is_staff = False

    if is_staff:
        # Tampilan untuk staff admin
        daftar_hewan = []
        for hewan in DUMMY_HEWAN:
            info = {
                'id': hewan['id'],
                'nama': hewan['nama'],
                'spesies': hewan['spesies'],
                'kondisi': hewan['status_kesehatan'],
                'foto_url': hewan['url_foto'],
                'habitat': hewan['asal_hewan'],
                'status_adopsi': 'Tidak Diadopsi'
            }
            for adopsi in DUMMY_ADOPSI:
                if adopsi['id_hewan'] == hewan['id'] and adopsi['tgl_berhenti_adopsi'] > datetime.now():
                    info['status_adopsi'] = 'Diadopsi'
                    info['tanggal_adopsi'] = adopsi['tgl_mulai_adopsi'].strftime('%d-%m-%Y')
                    info['tanggal_akhir'] = adopsi['tgl_berhenti_adopsi'].strftime('%d-%m-%Y')
                    info['nominal_kontribusi'] = adopsi['kontribusi_finansial']
                    info['status_pembayaran'] = adopsi['status_pembayaran']
                    # Cek nama adopter
                    for ind in DUMMY_INDIVIDU:
                        if ind['id_adopter'] == adopsi['id_adopter']:
                            info['nama_adopter'] = ind['nama']
                            break
                    if 'nama_adopter' not in info:
                        for org in DUMMY_ORGANISASI:
                            if org['id_adopter'] == adopsi['id_adopter']:
                                info['nama_adopter'] = org['nama_organisasi']
                                break
                    if 'nama_adopter' not in info:
                        info['nama_adopter'] = 'Unknown'
                    break
            daftar_hewan.append(info)
        return render(request, 'staff/status_adopsi.html', {'daftar_hewan': daftar_hewan,
                                                            'is_staff': is_staff,})
    else:
        # Tampilan untuk pengunjung/adopter
        messages.error(request, "Anda tidak memiliki akses untuk halaman ini.")
        return redirect('adopsi:status_adopsi')

def form_adopsi(request, hewan_id):
    """View untuk menampilkan form adopsi hewan"""
    # Simulasi user sebagai admin
    is_staff = request.GET.get('role', '') == 'admin'
    
    if not is_staff:
        messages.error(request, "Anda tidak memiliki akses untuk halaman ini.")
        return redirect('adopsi:status_adopsi')
    
    hewan_terpilih = None
    for hewan in DUMMY_HEWAN:
        if hewan['id'] == hewan_id:
            hewan_terpilih = {
                'id': hewan['id'],
                'nama': hewan['nama'],
                'spesies': hewan['spesies'],
                'kondisi': hewan['status_kesehatan'],
                'foto_url': hewan['url_foto']
            }
            break
    
    if not hewan_terpilih:
        messages.error(request, "Hewan tidak ditemukan.")
        return redirect('adopsi:status_adopsi')
    
    daftar_hewan = []
    for hewan in DUMMY_HEWAN:
        hewan_info = {
            'id': hewan['id'],
            'nama': hewan['nama'],
            'spesies': hewan['spesies'],
            'kondisi': hewan['status_kesehatan'],
            'foto_url': hewan['url_foto'],
            'status_adopsi': 'Tidak Diadopsi'
        }
        for adopsi in DUMMY_ADOPSI:
            if adopsi['id_hewan'] == hewan['id'] and adopsi['tgl_berhenti_adopsi'] > datetime.now():
                hewan_info['status_adopsi'] = 'Diadopsi'
                break
        daftar_hewan.append(hewan_info)
    
    return render(request, 'staff/status_adopsi.html', {
        'daftar_hewan': daftar_hewan,
        'hewan_terpilih': hewan_terpilih
    })

def verifikasi_adopter(request, hewan_id):
    """Verifikasi username adopter sebelum mendaftarkan adopsi"""
    # Simulasi user sebagai admin
    role = request.GET.get('role', 'admin')  # Selalu gunakan admin untuk demo
    is_staff = True  # Untuk demo anggap selalu staff
    
    if request.method == 'POST':
        adopter_username = request.POST.get('username')
        tipe_adopter = request.POST.get('tipe_adopter')
        
        # Dummy data pengunjung yang lebih lengkap
        adopter_info = {
            'username': adopter_username,
            'nama_depan': adopter_username[0],
            'nama_belakang': adopter_username[1:],
            'alamat': 'Jl. Dummy No. 123, Jakarta',
            'no_telepon': '081234567890'
        }
        
        # Cari hewan yang diselect
        hewan_terpilih = None
        for hewan in DUMMY_HEWAN:
            if hewan['id'] == hewan_id:
                hewan_terpilih = {
                    'id': hewan['id'],
                    'nama': hewan['nama'] if hewan['nama'] else 'Tanpa Nama',
                    'spesies': hewan['spesies'],
                    'kondisi': hewan['status_kesehatan'],
                    'foto_url': hewan['url_foto']
                }
                break
        
        if not hewan_terpilih:
            messages.error(request, "Hewan tidak ditemukan.")
            return redirect('adopsi:status_adopsi')
        
        # Siapkan data untuk template
        daftar_hewan = []
        for hewan in DUMMY_HEWAN:
            hewan_info = {
                'id': hewan['id'],
                'nama': hewan['nama'],
                'spesies': hewan['spesies'],
                'kondisi': hewan['status_kesehatan'],
                'foto_url': hewan['url_foto'],
                'status_adopsi': 'Tidak Diadopsi'
            }
            for adopsi in DUMMY_ADOPSI:
                if adopsi['id_hewan'] == hewan['id'] and adopsi['tgl_berhenti_adopsi'] > datetime.now():
                    hewan_info['status_adopsi'] = 'Diadopsi'
                    break
            daftar_hewan.append(hewan_info)
        
        # Simpan di session untuk referensi
        request.session['adopter_username'] = adopter_username
        
        # Tampilkan form berdasarkan tipe adopter dengan flag show_modal=True 
        # untuk memastikan modal muncul di template
        return render(request, 'staff/status_adopsi.html', {
            'daftar_hewan': daftar_hewan,
            'hewan_terpilih': hewan_terpilih,
            'adopter': adopter_info,
            'form_adopsi_tipe': tipe_adopter,
            'show_modal': True,  # Flag khusus untuk memicu modal
            'role': 'admin'
        })
    
    # Jika bukan POST, redirect ke halaman status adopsi
    return redirect('adopsi:status_adopsi')

def submit_adopsi_individu(request, hewan_id):
    """Memproses pengajuan adopsi individu"""
    # Simulasi user sebagai admin
    is_staff = request.GET.get('role', '') == 'admin'
    
    if not is_staff:
        messages.error(request, "Anda tidak memiliki akses untuk halaman ini.")
        return redirect('adopsi:status_adopsi')
    
    if request.method == 'POST':
        # Dalam implementasi asli, di sini akan ada proses pembuatan data adopsi
        messages.success(request, "Berhasil mendaftarkan adopter untuk hewan tersebut.")
        
        if 'adopter_username' in request.session:
            del request.session['adopter_username']
    
    return redirect('adopsi:status_adopsi')

def submit_adopsi_organisasi(request, hewan_id):
    """Memproses pengajuan adopsi organisasi"""
    # Simulasi user sebagai admin
    is_staff = request.GET.get('role', '') == 'admin'
    
    if not is_staff:
        messages.error(request, "Anda tidak memiliki akses untuk halaman ini.")
        return redirect('adopsi:status_adopsi')
    
    if request.method == 'POST':
        # Dalam implementasi asli, di sini akan ada proses pembuatan data adopsi
        messages.success(request, "Berhasil mendaftarkan organisasi sebagai adopter untuk hewan tersebut.")
        
        if 'adopter_username' in request.session:
            del request.session['adopter_username']
    
    return redirect('adopsi:status_adopsi')

def update_status_adopsi(request, hewan_id):
    """Update status pembayaran adopsi"""
    # Simulasi user sebagai admin
    is_staff = request.GET.get('role', '') == 'admin'
    
    if not is_staff:
        messages.error(request, "Anda tidak memiliki akses untuk halaman ini.")
        return redirect('adopsi:status_adopsi')
    
    if request.method == 'POST':
        status_pembayaran = request.POST.get('status_pembayaran')
        messages.success(request, f"Status pembayaran berhasil diubah menjadi {status_pembayaran}.")
    
    return redirect('adopsi:status_adopsi')

def hentikan_adopsi(request, hewan_id):
    """Menghentikan adopsi (oleh staff)"""
    # Simulasi user sebagai admin
    is_staff = request.GET.get('role', '') == 'admin'
    
    if not is_staff:
        messages.error(request, "Anda tidak memiliki akses untuk halaman ini.")
        return redirect('adopsi:status_adopsi')
    
    if request.method == 'POST':
        messages.success(request, "Adopsi berhasil dihentikan.")
    
    return redirect('adopsi:status_adopsi')

def hentikan_adopsi_user(request, hewan_id):
    """Menghentikan adopsi (oleh adopter)"""
    if request.method == 'POST':
        messages.success(request, "Adopsi berhasil dihentikan.")
    
    return redirect('adopsi:status_adopsi')

def adopsi_saya(request):
    """Menampilkan daftar hewan yang diadopsi oleh pengunjung"""
    # Untuk demo, kita anggap user adalah john_doe
    username = 'john_doe'
    
    # Cari adopter berdasarkan username
    adopter = next((a for a in DUMMY_ADOPTER if a['username_adopter'] == username), None)
    
    # Informasi dasar adopter
    adopter_info = {
        'alamat': 'Jl. Dummy No. 123, Jakarta',
        'no_telepon': '081234567890'
    }
    
    # NIK untuk individu dan NPP untuk organisasi
    nik_adopter = None
    npp_adopter = None
    
    hewan_adopsi_saya = []
    if adopter:
        # Cari info tambahan tergantung tipe adopter
        for ind in DUMMY_INDIVIDU:
            if ind['id_adopter'] == adopter['id_adopter']:
                nik_adopter = ind['nik']
                break
                
        for org in DUMMY_ORGANISASI:
            if org['id_adopter'] == adopter['id_adopter']:
                npp_adopter = org['npp']
                break
                
        # Ambil daftar hewan yang diadopsi
        for adopsi in DUMMY_ADOPSI:
            if adopsi['id_adopter'] == adopter['id_adopter'] and adopsi['tgl_berhenti_adopsi'] > datetime.now():
                hewan = next((h for h in DUMMY_HEWAN if h['id'] == adopsi['id_hewan']), None)
                if hewan:
                    info = {
                        'id': hewan['id'],
                        'nama': hewan['nama'],
                        'spesies': hewan['spesies'],
                        'kondisi': hewan['status_kesehatan'],
                        'habitat': hewan['asal_hewan'],
                        'foto_url': hewan['url_foto'],
                        'tanggal_adopsi': adopsi['tgl_mulai_adopsi'].strftime('%d-%m-%Y'),
                        'tanggal_akhir': adopsi['tgl_berhenti_adopsi'].strftime('%d-%m-%Y'),
                        'nominal_kontribusi': adopsi['kontribusi_finansial'],
                        'status_pembayaran': adopsi['status_pembayaran']
                    }
                    # Cek tipe adopter
                    for ind in DUMMY_INDIVIDU:
                        if ind['id_adopter'] == adopter['id_adopter']:
                            info['nama_adopter'] = ind['nama']
                            info['tipe_adopsi'] = 'individu'
                            break
                    if 'nama_adopter' not in info:
                        for org in DUMMY_ORGANISASI:
                            if org['id_adopter'] == adopter['id_adopter']:
                                info['nama_adopter'] = org['nama_organisasi']
                                info['tipe_adopsi'] = 'organisasi'
                                break
                    hewan_adopsi_saya.append(info)
    
    return render(request, 'pengunjung/adopsi_saya.html', {
        'hewan_adopsi_saya': hewan_adopsi_saya,
        'username': username,
        'adopter': adopter_info,
        'nik_adopter': nik_adopter,
        'npp_adopter': npp_adopter
    })

def lihat_sertifikat(request, hewan_id):
    """Menampilkan sertifikat adopsi hewan"""
    # Untuk demo, kita anggap user adalah john_doe
    username = 'john_doe'
    
    # Cari adopter berdasarkan username
    adopter = next((a for a in DUMMY_ADOPTER if a['username_adopter'] == username), None)
    
    # Pastikan hewan ini memang diadopsi oleh adopter ini
    hewan_adopsi = None
    nama_adopter = ""
    
    if adopter:
        for adopsi in DUMMY_ADOPSI:
            if adopsi['id_adopter'] == adopter['id_adopter'] and adopsi['id_hewan'] == hewan_id and adopsi['tgl_berhenti_adopsi'] > datetime.now():
                hewan = next((h for h in DUMMY_HEWAN if h['id'] == hewan_id), None)
                if hewan:
                    hewan_adopsi = {
                        'id': hewan['id'],
                        'nama': hewan['nama'],
                        'spesies': hewan['spesies'],
                        'foto_url': hewan['url_foto'],
                        'tanggal_adopsi': adopsi['tgl_mulai_adopsi'].strftime('%d-%m-%Y'),
                        'tanggal_akhir': adopsi['tgl_berhenti_adopsi'].strftime('%d-%m-%Y')
                    }
                    break
        
        # Ambil nama adopter
        for ind in DUMMY_INDIVIDU:
            if ind['id_adopter'] == adopter['id_adopter']:
                nama_adopter = ind['nama']
                break
                
        if not nama_adopter:
            for org in DUMMY_ORGANISASI:
                if org['id_adopter'] == adopter['id_adopter']:
                    nama_adopter = org['nama_organisasi']
                    break
    
    if not hewan_adopsi:
        messages.error(request, "Hewan tidak ditemukan atau bukan adopsi Anda.")
        return redirect('adopsi:adopsi_saya')
    
    return render(request, 'pengunjung/sertifikat_adopsi.html', {
        'hewan': hewan_adopsi,
        'nama_adopter': nama_adopter
    })

def pantau_kondisi(request, hewan_id):
    """Menampilkan rekam medis dan kondisi hewan"""
    # Untuk demo, kita anggap user adalah john_doe
    username = 'john_doe'
    
    # Cari adopter berdasarkan username
    adopter = next((a for a in DUMMY_ADOPTER if a['username_adopter'] == username), None)
    
    # Pastikan hewan ini memang diadopsi oleh adopter ini
    hewan_adopsi = None
    tanggal_adopsi = None
    
    if adopter:
        for adopsi in DUMMY_ADOPSI:
            if adopsi['id_adopter'] == adopter['id_adopter'] and adopsi['id_hewan'] == hewan_id and adopsi['tgl_berhenti_adopsi'] > datetime.now():
                hewan = next((h for h in DUMMY_HEWAN if h['id'] == hewan_id), None)
                if hewan:
                    hewan_adopsi = {
                        'id': hewan['id'],
                        'nama': hewan['nama'],
                        'spesies': hewan['spesies'],
                        'kondisi': hewan['status_kesehatan'],
                        'habitat': hewan['asal_hewan'],
                        'foto_url': hewan['url_foto']
                    }
                    tanggal_adopsi = adopsi['tgl_mulai_adopsi']
                    break
    
    if not hewan_adopsi:
        messages.error(request, "Hewan tidak ditemukan atau bukan adopsi Anda.")
        return redirect('adopsi:adopsi_saya')
    
    # Filter rekam medis yang relevan (tanggal setelah adopsi)
    rekam_medis = []
    for medis in DUMMY_REKAM_MEDIS:
        if medis['id_hewan'] == hewan_id:
            tgl_periksa = datetime.strptime(medis['tanggal_pemeriksaan'], '%Y-%m-%d')
            if tgl_periksa >= tanggal_adopsi:
                rekam_medis.append(medis)
    
    # Urutkan rekam medis berdasarkan tanggal (terbaru dulu)
    rekam_medis.sort(key=lambda x: x['tanggal_pemeriksaan'], reverse=True)
    
    return render(request, 'pengunjung/kondisi_hewan.html', {
        'hewan': hewan_adopsi,
        'rekam_medis': rekam_medis
    })

def perpanjang_adopsi(request, hewan_id):
    """Memproses perpanjangan periode adopsi"""
    if request.method == 'POST':
        periode = request.POST.get('periode', 6)  # Default 6 bulan jika tidak ada
        nominal = request.POST.get('nominal', 500000)  # Default 500rb jika tidak ada
        
        try:
            periode = int(periode)
            nominal = int(nominal)
        except ValueError:
            messages.error(request, "Input tidak valid.")
            return redirect('adopsi:adopsi_saya')
        
        # Di sini akan ada logika untuk memperbarui data adopsi
        # ...
        
        messages.success(request, f"Berhasil memperpanjang adopsi untuk {periode} bulan berikutnya.")
    
    return redirect('adopsi:adopsi_saya')

def hentikan_adopsi_user(request, hewan_id):
    """Menghentikan adopsi (oleh adopter)"""
    if request.method == 'POST':
        # Di sini akan ada logika untuk menghentikan adopsi
        # ...
        
        messages.success(request, "Adopsi berhasil dihentikan. Terima kasih atas kontribusi Anda selama ini.")
    
    return redirect('adopsi:adopsi_saya')

def daftar_adopter(request):
    """Menampilkan daftar adopter dengan kontribusi tertinggi dan semua adopter"""
    # Memastikan yang mengakses adalah staf administrasi
    is_staff = True  # Untuk demo anggap selalu true
    
    if not is_staff:
        messages.error(request, "Anda tidak memiliki akses untuk halaman ini.")
        return redirect('adopsi:status_adopsi')
    
    # Ambil data semua adopter
    adopter_list = []
    for adopter_id in DUMMY_ADOPTER:
        total_kontribusi = adopter_id['total_kontribusi']
        nama_adopter = ""
        
        # Cek apakah individu atau organisasi
        for ind in DUMMY_INDIVIDU:
            if ind['id_adopter'] == adopter_id['id_adopter']:
                nama_adopter = ind['nama']
                break
                
        if not nama_adopter:
            for org in DUMMY_ORGANISASI:
                if org['id_adopter'] == adopter_id['id_adopter']:
                    nama_adopter = org['nama_organisasi']
                    break
        
        adopter_list.append({
            'id': adopter_id['id_adopter'],
            'nama': nama_adopter,
            'total_kontribusi': total_kontribusi
        })
    
    # Urutkan berdasarkan total kontribusi (tertinggi dulu)
    adopter_list.sort(key=lambda x: x['total_kontribusi'], reverse=True)
    
    # Ambil 5 teratas untuk ditampilkan secara khusus
    top_adopters = adopter_list[:5] if len(adopter_list) >= 5 else adopter_list
    
    return render(request, 'staff/daftar_adopter.html', {
        'adopters': adopter_list,
        'top_adopters': top_adopters
    })

def riwayat_adopsi(request, adopter_id):
    """Menampilkan riwayat adopsi dari seorang adopter"""
    # Memastikan yang mengakses adalah staf administrasi
    is_staff = True  # Untuk demo anggap selalu true
    
    if not is_staff:
        messages.error(request, "Anda tidak memiliki akses untuk halaman ini.")
        return redirect('adopsi:status_adopsi')
    
    # Cari informasi adopter
    adopter_info = None
    nama_adopter = ""
    
    for adopter in DUMMY_ADOPTER:
        if adopter['id_adopter'] == adopter_id:
            # Cek apakah individu atau organisasi
            for ind in DUMMY_INDIVIDU:
                if ind['id_adopter'] == adopter_id:
                    nama_adopter = ind['nama']
                    adopter_info = {
                        'id': adopter_id,
                        'nama': nama_adopter,
                        'alamat': 'Jl. Dummy No. 123, Jakarta',
                        'no_telepon': '081234567890'
                    }
                    break
                    
            if not adopter_info:
                for org in DUMMY_ORGANISASI:
                    if org['id_adopter'] == adopter_id:
                        nama_adopter = org['nama_organisasi']
                        adopter_info = {
                            'id': adopter_id,
                            'nama': nama_adopter,
                            'alamat': 'Jl. Corporate Dummy No. 456, Jakarta',
                            'no_telepon': '021-7654321'
                        }
                        break
            break
    
    if not adopter_info:
        messages.error(request, "Adopter tidak ditemukan.")
        return redirect('adopsi:daftar_adopter')
    
    # Ambil semua adopsi dari adopter ini
    daftar_adopsi = []
    for adopsi in DUMMY_ADOPSI:
        if adopsi['id_adopter'] == adopter_id:
            hewan = next((h for h in DUMMY_HEWAN if h['id'] == adopsi['id_hewan']), None)
            if hewan:
                # Cek apakah adopsi masih berlangsung
                is_active = adopsi['tgl_berhenti_adopsi'] > datetime.now()
                
                daftar_adopsi.append({
                    'id': uuid.uuid4(),  # Generate random ID for demo
                    'nama_hewan': hewan['nama'],
                    'jenis_hewan': hewan['spesies'],
                    'tanggal_mulai': adopsi['tgl_mulai_adopsi'].strftime('%d-%m-%Y'),
                    'tanggal_akhir': adopsi['tgl_berhenti_adopsi'].strftime('%d-%m-%Y'),
                    'nominal_kontribusi': adopsi['kontribusi_finansial'],
                    'is_active': is_active
                })
    
    # Urutkan berdasarkan tanggal mulai (terbaru dulu)
    daftar_adopsi.sort(key=lambda x: datetime.strptime(x['tanggal_mulai'], '%d-%m-%Y'), reverse=True)
    
    return render(request, 'staff/riwayat_adopsi.html', {
        'adopter': adopter_info,
        'daftar_adopsi': daftar_adopsi
    })

def hapus_adopter(request, adopter_id):
    """Menghapus data adopter beserta seluruh riwayat adopsinya"""
    if request.method == 'POST':
        # Di implementasi asli, proses hapus dari database
        messages.success(request, "Data adopter berhasil dihapus.")
    
    return redirect('adopsi:daftar_adopter')

def hapus_adopsi(request, adopsi_id):
    """Menghapus sebuah riwayat adopsi"""
    if request.method == 'POST':
        # Di implementasi asli, proses hapus dari database
        # Untuk demo kita redirect kembali ke halaman sebelumnya
        referer = request.META.get('HTTP_REFERER')
        if referer:
            messages.success(request, "Riwayat adopsi berhasil dihapus.")
            return redirect(referer)
    
    return redirect('adopsi:daftar_adopter')