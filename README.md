# UDP DDoS Simulation Script

Simulasi serangan **UDP Denial of Service (DDoS)** menggunakan Python yang dirancang untuk tujuan **pembelajaran** di lingkungan **lab komputer**. Script ini memungkinkan untuk melakukan pengujian terhadap server atau perangkat yang ada dalam **jaringan lokal**.

**Perhatian!**: Simulasi ini hanya untuk digunakan di lingkungan uji yang sah dan tidak boleh digunakan untuk merusak atau mengganggu sistem yang tidak dimiliki atau tanpa izin eksplisit.

## Fitur
- **Interaktif**: Script meminta input dari pengguna untuk menentukan IP target, port, dan jumlah thread.
- **Multi-threaded**: Menggunakan banyak thread untuk mengirim paket UDP secara simultan ke target.
- **Tangkapan `Ctrl + C`**: Menampilkan pesan ketika script dihentikan oleh pengguna.
- **Loop untuk Pengujian Ulang**: Setelah satu simulasi selesai, pengguna dapat memilih untuk menjalankan ulang atau keluar dari program.

## Persyaratan
- Python 3.x
- Tidak ada dependensi luar (hanya menggunakan library bawaan Python)

## Cara Penggunaan
1. **Clone repositori ini**:
   ```bash
   git clone https://github.com/Icanskk9/UDP_FloodLAN.git
   cd UDP_FloodLAN
   python ddos.py
