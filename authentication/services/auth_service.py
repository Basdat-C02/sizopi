import uuid
from django.contrib.auth.hashers import check_password, make_password
from utils.query_helper import execute_query, fetch_dict_all, fetch_dict_one

class AuthService:
    PENGGUNA_FIELDS = """
        P.username AS username,
        P.email AS email,
        P.password AS password,
        P.nama_depan AS nama_depan,
        P.nama_tengah AS nama_tengah,
        P.nama_belakang AS nama_belakang,
        P.no_telepon AS no_telepon,
        PENG.alamat AS alamat,
        PENG.tgl_lahir AS tgl_lahir,
        DH.no_str AS no_str,
        pjh.id_staf AS id_staf_penjaga,
        plh.id_staf AS id_staf_pelatih,
        sa.id_staf AS id_staf_admin,
        CASE
            WHEN PENG.username_p IS NOT NULL THEN 'Pengunjung'
            WHEN DH.username_dh IS NOT NULL THEN 'Dokter Hewan'
            WHEN pjh.username_jh IS NOT NULL THEN 'Penjaga Hewan'
            WHEN plh.username_lh IS NOT NULL THEN 'Pelatih Hewan'
            WHEN sa.username_sa IS NOT NULL THEN 'Staf Admin'
            ELSE 'unknown'
        END AS role
    """
    
    @staticmethod
    def get_all_user():
        sql = f"""
        SELECT {AuthService.PENGGUNA_FIELDS}
        FROM PENGGUNA P
        LEFT JOIN PENGUNJUNG PENG ON P.username = PENG.username_p
        LEFT JOIN DOKTER_HEWAN DH ON P.username = DH.username_dh
        LEFT JOIN PENJAGA_HEWAN pjh ON P.username = pjh.username_jh
        LEFT JOIN PELATIH_HEWAN plh ON P.username = plh.username_lh
        LEFT JOIN STAF_ADMIN sa ON P.username = sa.username_sa
        """
        return fetch_dict_all(sql)
    
    @staticmethod
    def get_user_by_username(username: str) :
        sql = f"""
        SELECT {AuthService.PENGGUNA_FIELDS}
        FROM PENGGUNA P
        LEFT JOIN PENGUNJUNG PENG ON P.username = PENG.username_p
        LEFT JOIN DOKTER_HEWAN DH ON P.username = DH.username_dh
        LEFT JOIN PENJAGA_HEWAN pjh ON P.username = pjh.username_jh
        LEFT JOIN PELATIH_HEWAN plh ON P.username = plh.username_lh
        LEFT JOIN STAF_ADMIN sa ON P.username = sa.username_sa
        WHERE P.username = %s
        """
        result = fetch_dict_one(sql, [username])
        if not result:
            return None

        role = result.get("role")

        result["is_pengguna"] = bool(role)
        result["is_pengunjung"] = role == "Pengunjung"
        result["is_dokter_hewan"] = role == "Dokter Hewan"
        result["is_penjaga_hewan"] = role == "Penjaga Hewan"
        result["is_pelatih_hewan"] = role == "Pelatih Hewan"
        result["is_staf_admin"] = role == "Staf Admin"
        
        return result
    
    @staticmethod
    def hash_password(password):
        """Hashes the given password."""
        return make_password(password)

    @staticmethod
    def check_password(password, hashed_password):
        """Checks if the given password matches the hashed password."""
        return check_password(password, hashed_password)
    
    @staticmethod
    def create_profile(data: dict):
        AuthService.create_pengguna(data)
        role = data.get("role")
        if role == "pengunjung":
            AuthService.create_pengunjung(data)
        elif role == "dokter_hewan":
            AuthService.create_dokter_hewan(data)
        else:
            AuthService.create_staff_member(data)
    
    @staticmethod
    def create_pengguna(data: dict):
        sql = """
        INSERT INTO PENGGUNA (username, email, password, nama_depan, nama_tengah, nama_belakang, no_telepon)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        hashed_password = AuthService.hash_password(data["password"])
        params = [
            data["username"], data["email"], hashed_password,
            data["nama_depan"], data.get("nama_tengah"),
            data["nama_belakang"], data["no_telepon"]
        ]
        execute_query(sql, params)
    
    @staticmethod
    def create_pengunjung(data: dict):
        sql = """
        INSERT INTO PENGUNJUNG (username_p, alamat, tgl_lahir)
        VALUES (%s, %s, %s)
        """
        execute_query(sql, [data["username"], data["alamat"], data["tgl_lahir"]])
    
    @staticmethod
    def create_dokter_hewan(data: dict):
        sql = """
        INSERT INTO DOKTER_HEWAN (username_dh, no_str)
        VALUES (%s, %s)
        """
        execute_query(sql, [data["username"], data["no_str"]])
        
        for spesialis in data["spesialisasi"]:
            execute_query(
                "INSERT INTO SPESIALISASI (username_sh, nama_spesialisasi) VALUES (%s, %s)",
                [data["username"], spesialis]
            )
    
    @staticmethod
    def create_staff_member(data: dict):
        sql = ""
        if data["role"] == "staf_admin":
            sql = """
            INSERT INTO STAF_ADMIN (username_sa, id_staf)
            VALUES (%s, %s)
            """
        elif data["role"] == "penjaga_hewan":
            sql = """
            INSERT INTO PENJAGA_HEWAN (username_jh, id_staf)
            VALUES (%s, %s)
            """
        elif data["role"] == "pelatih_hewan":
            sql = """
            INSERT INTO PELATIH_HEWAN (username_lh, id_staf)
            VALUES (%s, %s)
            """
        execute_query(sql, [data["username"], data["id_staf"]])
    
    @staticmethod
    def update_profile(data: dict):
        AuthService.update_pengguna(data)
        role = data.get("role")
        if role == "pengunjung":
            AuthService.update_pengunjung(data)
        elif role == "dokter_hewan":
            AuthService.update_dokter_hewan(data)
        else:
            AuthService.update_staff_member(data)
    
    @staticmethod
    def update_password(username: str, new_password: str):
        hashed = AuthService.hash_password(new_password)
        sql = """
        UPDATE PENGGUNA
        SET password = %s
        WHERE username = %s
        """
        execute_query(sql, [hashed, username])

    @staticmethod
    def update_pengguna(data: dict):
        sql = """
        UPDATE PENGGUNA
        SET email = %s,
            nama_depan = %s,
            nama_tengah = %s,
            nama_belakang = %s,
            no_telepon = %s
        WHERE username = %s
        """
        params = [
            data["email"], data["nama_depan"], data.get("nama_tengah"),
            data["nama_belakang"], data["no_telepon"], data["username"]
        ]
        execute_query(sql, params)
    
    @staticmethod
    def update_pengunjung(data: dict):
        sql = """
        UPDATE PENGUNJUNG
        SET alamat = %s,
            tgl_lahir = %s
        WHERE username_p = %s
        """
        execute_query(sql, [data["alamat"], data["tgl_lahir"], data["username"]])
    
    @staticmethod
    def update_dokter_hewan(data: dict):
        sql = """
        UPDATE DOKTER_HEWAN
        SET no_str = %s
        WHERE username_dh = %s
        """
        execute_query(sql, [data["no_str"], data["username"]])
        
        execute_query("DELETE FROM SPESIALISASI WHERE username_sh = %s", [data["username"]])
        for spesialis in data.get("spesialisasi", []):
            execute_query(
                "INSERT INTO SPESIALISASI (username_sh, nama_spesialisasi) VALUES (%s, %s)",
                [data["username"], spesialis]
            )
    
    @staticmethod
    def update_staff_member(data: dict):
        sql = ""
        if data["role"] == "staf_admin":
            sql = """
            UPDATE STAF_ADMIN
            SET id_staf = %s
            WHERE username_sa = %s
            """
        elif data["role"] == "penjaga_hewan":
            sql = """
            UPDATE PENJAGA_HEWAN
            SET id_staf = %s
            WHERE username_jh = %s
            """
        elif data["role"] == "pelatih_hewan":
            sql = """
            UPDATE PELATIH_HEWAN
            SET id_staf = %s
            WHERE username_lh = %s
            """
        execute_query(sql, [data["id_staf"], data["username"]])
    
    @staticmethod
    def get_user_detail(username:str):
        user = AuthService.get_user_by_username(username)
        if not user:
            return None
        if user["is_pengunjung"]:
            AuthService.get_pengunjung_detail(user)
        elif user["is_dokter_hewan"]:
            AuthService.get_dokter_hewan_detail(user)
        elif user["is_penjaga_hewan"]:
            AuthService.get_penjaga_hewan_detail(user)
        elif user["is_pelatih_hewan"]:
            AuthService.get_pelatih_hewan_detail(user)
        elif user["is_staf_admin"]:
            AuthService.get_staf_admin_detail(user)
    
    @staticmethod
    def get_pengunjung_detail(data: dict):
        username = data["username"]
        
        reservasi = fetch_dict_all("""
            SELECT R.tanggal_kunjungan, A.nama_atraksi, A.lokasi, R.status
            FROM RESERVASI R
            JOIN ATRAKSI A ON R.nama_atraksi = A.nama_atraksi
            WHERE R.username_p = %s
            ORDER BY R.tanggal_kunjungan DESC
        """, [username])
        
        tiket = fetch_dict_all("""
            SELECT R.nama_atraksi, SUM(R.jumlah_tiket) AS jumlah_tiket
            FROM RESERVASI R
            WHERE R.username_p = %s
            GROUP BY R.nama_atraksi
        """, [username])
        
        data["riwayat_kunjungan"] = reservasi
        data["informasi_tiket_dibeli"] = tiket
        return data

    @staticmethod
    def get_dokter_hewan_detail(data: dict):
        username = data["username"]
        
        spesialisasi = fetch_dict_all("""
            SELECT nama_spesialisasi FROM SPESIALISASI WHERE username_sh = %s
        """, [username])
        
        jumlah_hewan = fetch_dict_all("""
            SELECT COUNT(DISTINCT id_hewan) AS jumlah_hewan FROM CATATAN_MEDIS WHERE username_dh = %s
        """, [username])
        
        data["spesialisasi"] = [s["nama_spesialisasi"] for s in spesialisasi]
        data["jumlah_hewan"] = jumlah_hewan[0]["jumlah_hewan"] if jumlah_hewan else 0
        return data
    
    @staticmethod
    def get_penjaga_hewan_detail(data: dict):
        username = data["username"]
        
        jumlah_hewan = fetch_dict_one("""
            SELECT COUNT(DISTINCT id_hewan) AS total FROM MEMBERI WHERE username_jh = %s
        """, [username])
        
        data["jumlah_hewan_diberi_pakan"] = jumlah_hewan["total"] if jumlah_hewan else 0
        return data
    
    @staticmethod
    def get_pelatih_hewan_detail(data: dict):
        username = data["username"]
        
        jadwal_penugasan = fetch_dict_all("""
            SELECT tgl_penugasan AS waktu, nama_atraksi AS nama_pertunjukan
            FROM JADWAL_PENUGASAN
            WHERE username_lh = %s
        """, [username])
        
        hewan_dilatih = fetch_dict_all("""
            SELECT DISTINCT H.nama
            FROM BERPARTISIPASI B
            JOIN HEWAN H ON B.id_hewan = H.id
            JOIN JADWAL_PENUGASAN JP ON B.nama_fasilitas = JP.nama_atraksi
            WHERE JP.username_lh = %s
        """, [username])
        
        data["jadwal_pertunjukan"] = jadwal_penugasan
        data["daftar_hewan_dilatih"] = [h["nama"] for h in hewan_dilatih]
        return data
    
    @staticmethod
    def get_staf_admin_detail(data: dict):
        username = data["username"]
        
        jumlah_pengunjung = fetch_dict_one("""
            SELECT COUNT(DISTINCT username_p) AS jumlah
            FROM RESERVASI
        """)
        
        laporan_pendapatan = fetch_dict_one("""
            SELECT COALESCE(SUM(jumlah_tiket * 25000), 0) AS total
            FROM RESERVASI
        """)

        data["jumlah_pengunjung"] = jumlah_pengunjung["jumlah"] if jumlah_pengunjung else 0
        data["ringkasan_penjualan_tiket"] = laporan_pendapatan["total"] if laporan_pendapatan else 0
        return data