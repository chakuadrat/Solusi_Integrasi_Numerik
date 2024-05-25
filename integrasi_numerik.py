import time
import numpy as np

def f(x):
    """Fungsi yang akan diintegrasikan"""
    return 4 / (1 + x**2)

def simpson_integration(a, b, N):
    """Metode Integrasi Simpson 1/3"""
    if N % 2 != 0:
        raise ValueError("Jumlah titik harus genap.")
    
    h = (b - a) / N
    x = np.linspace(a, b, N+1)
    y = f(x)
    
    integral = h / 3 * (y[0] + y[-1] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-1:2]))
    return integral

def calculate_pi(N):
    """Menghitung nilai pi dengan metode Integrasi Simpson 1/3"""
    a = 0  # Batas bawah
    b = 1  # Batas atas
    integral = simpson_integration(a, b, N)
    return integral

def main():
    """Fungsi utama untuk menjalankan program."""
    print("\nNisrina Azka Salsabila")
    print("21120122130057")
    print ("Metode Numerik - Kelas C")
    print("Teknik Komputer")
    
    while True:
        print("\nIntegrasi Simpson 1/3")
        print("\nSelamat datang! Silahkan pilih penyelesaian yang anda inginkan pada menu dibawah ini:")
        print("1. Penghitungan nilai integral fungsi")
        print("2. Keluar")

        pilihan = int(input("Masukkan pilihan Anda (1-2): "))

        if pilihan == 1:
            # Meminta input dari pengguna untuk nilai N
            while True:
                try:
                    N = int(input("Masukkan jumlah titik (N) untuk menghitung integral: "))
                    break
                except ValueError:
                    print("Masukkan harus berupa bilangan bulat.")

            # Menghitung nilai pi
            start_time = time.time()
            pi_approx = calculate_pi(N)
            end_time = time.time()

            # Nilai referensi pi
            pi_ref = 3.14159265358979323846

            # Menghitung galat RMS
            rms_error = np.sqrt(np.mean((pi_ref - pi_approx)**2))

            print(f"N = {N}, Pi ≈ {pi_approx}, Galat RMS = {rms_error}, Waktu Eksekusi = {end_time - start_time} detik")

        elif pilihan == 2:
            print("Terima kasih telah menggunakan program ini.")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih antara 1 dan 2.")

if __name__ == "__main__":
    main()
