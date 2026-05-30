# UTS-KRYPTOGRAFI-Integrity-Checking-Using-Hashing
## 🧪 Skenario Pengujian & Simulasi

### ⏱️ Langkah-Langkah Simulasi
1. **Membuat File Asli:** Buat file bernama `rahasia.txt` berisi teks:  
   `Halo ini file asli`
2. **Eksekusi Awal:** Jalankan program dan masukkan file `rahasia.txt` untuk mendapatkan nilai *hash* awal.
3. **Manipulasi Data:** Buka kembali file tersebut, tambahkan karakter titik `.` di akhir kalimat (`Halo ini file asli.`), lalu simpan.
4. **Validasi Akhir:** Tekan **Enter** pada program untuk melihat perubahan nilai hash secara drastis.

### 📊 Tabel Hasil Pengujian (Efek Longsoran / *Avalanche Effect*)

| Kondisi File | Isi Konten | Hash MD5 (128-bit) | Hash SHA-256 (256-bit) | Status Integritas |
| :--- | :--- | :--- | :--- | :--- |
| **File Asli** | `Halo ini file asli` | `4f88b56012...` *(contoh)* | `8a5c2b3e...` *(contoh)* | ✅ **Original** |
| **Modifikasi** | `Halo ini file asli.` | `9e10fa42bb...` *(berubah total)*| `2f7d8a9c...` *(berubah total)*| ❌ **Terubah!** |


### ❌ Mengapa MD5 Tidak Lagi Direkomendasikan?

1. **Kerentanan *Cryptographic Collision* (Tabrakan Hash):** MD5 memiliki cacat desain yang fatal. Dua file yang memiliki isi konten berbeda secara matematis dapat menghasilkan nilai hash MD5 yang **persis sama**.
2. **Sangat Rentan terhadap Manipulasi:** Penyerang dapat memanfaatkan teknik *chosen-prefix collisions* untuk menyisipkan *malware* ke dalam file legal tanpa mengubah nilai MD5-nya. Oleh karena itu, sejak tahun 2011, **IETF** telah melarang penggunaan MD5 untuk fungsi keamanan dan otentikasi data.

---

### 🛡️ Keunggulan & Ketangguhan SHA-256
* **Ruang Kombinasi yang Masif (256-bit):** SHA-256 menghasilkan output sepanjang 256 bit (64 karakter heksadesimal). Ini menghasilkan kombinasi kemungkinan sebanyak $2^{256}$—sebuah angka yang sangat besar sehingga hampir mustahil ditebak dengan metode *brute-force* tercepat sekalipun.
* **Resistensi Tinggi Terhadap *Collision*:** Hingga detik ini, belum ada komputer atau serangan praktis di dunia yang berhasil menjebol atau menemukan dua file berbeda dengan hash SHA-256 yang sama.
* **Standardisasi Global:** Menjadi pondasi utama dalam protokol keamanan modern, mulai dari enkripsi sertifikat SSL/TLS web, tanda tangan digital (Digital Signature), hingga keamanan jaringan terdesentralisasi seperti **Blockchain dan Bitcoin**.

---
