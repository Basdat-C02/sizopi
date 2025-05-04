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
            WHEN PENG.username_p IS NOT NULL THEN 'pengunjung'
            WHEN DH.username_dh IS NOT NULL THEN 'dokter_hewan'
            WHEN pjh.username_jh IS NOT NULL THEN 'penjaga_hewan'
            WHEN plh.username_lh IS NOT NULL THEN 'pelatih_hewan'
            WHEN sa.username_sa IS NOT NULL THEN 'staf_admin'
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
        result["is_pengunjung"] = role == "pengunjung"
        result["is_dokter_hewan"] = role == "dokter_hewan"
        result["is_penjaga_hewan"] = role == "penjaga_hewan"
        result["is_pelatih_hewan"] = role == "pelatih_hewan"
        result["is_staf_admin"] = role == "staf_admin"
        
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
        AuthService.create_pengguna(data)
        sql = """
        INSERT INTO PENGUNJUNG (username_p, alamat, tgl_lahir)
        VALUES (%s, %s, %s)
        """
        execute_query(sql, [data["username"], data["alamat"], data["tgl_lahir"]])
    
    @staticmethod
    def create_dokter_hewan(data: dict):
        AuthService.create_pengguna(data)
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
        AuthService.create_pengguna(data)
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
        AuthService.update_pengguna(data)
        sql = """
        UPDATE PENGUNJUNG
        SET alamat = %s,
            tgl_lahir = %s
        WHERE username_p = %s
        """
        execute_query(sql, [data["alamat"], data["tgl_lahir"], data["username"]])
    
    @staticmethod
    def update_dokter_hewan(data: dict):
        AuthService.update_pengguna(data)
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
        AuthService.update_pengguna(data)
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