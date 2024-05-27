import time
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    """Fungsi yang akan diintegrasikan"""
    return 4 / (1 + x**2)

def riemann_integration(a, b, N):
    """Metode Integrasi Riemann"""
    h = (b - a) / N
    x = np.linspace(a, b, N, endpoint=False) + h/2
    integral = np.sum(f(x)) * h
    return integral, x, h

def calculate_pi(N):
    """Menghitung nilai pi dengan metode Integrasi Riemann"""
    a = 0  # Batas bawah
    b = 1  # Batas atas
    integral, x, h = riemann_integration(a, b, N)
    return integral, x, h

def plot_riemann_integration(x, h):
    """Plot grafik integrasi Riemann"""
    plt.figure(figsize=(10, 6))
    x_plot = np.linspace(0, 1, 1000)
    y_plot = f(x_plot)
    plt.plot(x_plot, y_plot, 'b-', label='f(x) = 4 / (1 + x^2)')
    
    for i in range(len(x)):
        plt.bar(x[i], f(x[i]), width=h, alpha=0.3, align='center', edgecolor='black')
    
    plt.title("Visualisasi Integrasi Riemann")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    """Fungsi utama untuk menjalankan program."""
    print("\nNisrina Azka Salsabila")
    print("21120122130057")
    print("Metode Numerik - Kelas C")
    print("Teknik Komputer")
    
    while True:
        print("\nIntegrasi Riemann")
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
            pi_approx, x, h = calculate_pi(N)
            end_time = time.time()

            # Nilai referensi pi
            pi_ref = 3.14159265358979323846

            # Menghitung galat RMS
            rms_error = np.sqrt(np.mean((pi_ref - pi_approx)**2))

            print(f"N = {N}, Pi ≈ {pi_approx}, Galat RMS = {rms_error}, Waktu Eksekusi = {end_time - start_time} detik")

            # Menampilkan grafik
            plot_riemann_integration(x, h)

        elif pilihan == 2:
            print("Terima kasih telah menggunakan program ini.")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih antara 1 dan 2.")

if __name__ == "__main__":
    main()
