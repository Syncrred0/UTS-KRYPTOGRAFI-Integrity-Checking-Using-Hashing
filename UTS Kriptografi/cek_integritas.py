import hashlib
import os

def hitung_hash(nama_file):
    """Fungsi untuk menghitung hash MD5 dan SHA-256 dari sebuah file"""
    hash_md5 = hashlib.md5()
    hash_sha256 = hashlib.sha256()
    
    try:
        # Membaca file dalam bentuk biner (rb) per blok agar hemat memori
        with open(nama_file, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
                hash_sha256.update(chunk)
                
        return hash_md5.hexdigest(), hash_sha256.hexdigest()
    except FileNotFoundError:
        print(f"Error: File '{nama_file}' tidak ditemukan.")
        return None, None

def main():
    print("=== APLIKASI PENGECEK INTEGRITAS FILE ===")
    file_target = input("Masukkan nama atau jalur (path) file: ")
    
    if not os.path.exists(file_target):
        print("File tidak ditemukan. Pastikan nama dan lokasinya benar.")
        return
        
    # 1. Menghasilkan hash awal
    md5_awal, sha256_awal = hitung_hash(file_target)
    
    print("\n--- HASIL HASH FILE ---")
    print(f"Nama File : {file_target}")
    print(f"MD5       : {md5_awal}")
    print(f"SHA-256   : {sha256_awal}")
    print("-" * 23)
    
    # 2. Simulasi Pengecekan Perubahan
    input("\n[Simulasi] Silakan ubah isi file tersebut sekarang, lalu tekan Enter untuk cek ulang...")
    
    md5_baru, sha256_baru = hitung_hash(file_target)
    
    print("\n--- HASIL PENGECEKAN ULANG ---")
    print(f"MD5 Baru    : {md5_baru}")
    print(f"SHA-256 Baru: {sha256_baru}")
    
    print("\n--- ANALISIS INTEGRITAS ---")
    if md5_awal == md5_baru and sha256_awal == sha256_baru:
        print("✅ INTEGRITAS AMAN: File TIDAK mengalami perubahan.")
    else:
        print("❌ PERINGATAN: File TELAH DIMODIFIKASI / BERUBAH!")
        if md5_awal != md5_baru:
            print("   -> Perubahan terdeteksi oleh MD5")
        if sha256_awal != sha256_baru:
            print("   -> Perubahan terdeteksi oleh SHA-256")

if __name__ == "__main__":
    main()