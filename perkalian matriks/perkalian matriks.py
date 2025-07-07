import numpy as np
import time
import os

def clear_screen():
    """Membersihkan layar konsol."""
    os.system('cls' if os.name == 'nt' else 'clear')

def animate_text(text, delay=0.03):
    """Menampilkan teks dengan efek animasi."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print() # New line after animation

def get_matrix_input(name):
    """
    Mendapatkan input matriks dari pengguna.
    """
    while True:
        try:
            rows = int(input(f"Masukkan jumlah baris untuk Matriks {name}: "))
            cols = int(input(f"Masukkan jumlah kolom untuk Matriks {name}: "))
            if rows <= 0 or cols <= 0:
                print("Jumlah baris dan kolom harus bilangan bulat positif. Coba lagi.")
                continue

            matrix = []
            print(f"Masukkan elemen untuk Matriks {name} (satu baris per input, pisahkan dengan spasi):")
            for i in range(rows):
                while True:
                    row_str = input(f"Baris {i+1}: ")
                    try:
                        row = list(map(float, row_str.split()))
                        if len(row) != cols:
                            print(f"Jumlah elemen di baris ini tidak sesuai dengan jumlah kolom ({cols}). Coba lagi.")
                        else:
                            matrix.append(row)
                            break
                    except ValueError:
                        print("Input tidak valid. Pastikan Anda memasukkan angka yang dipisahkan oleh spasi. Coba lagi.")
            return np.array(matrix)
        except ValueError:
            print("Input tidak valid. Pastikan Anda memasukkan bilangan bulat untuk baris dan kolom. Coba lagi.")

def display_matrix(matrix, name=""):
    """
    Menampilkan matriks dengan format yang rapi.
    """
    if name:
        print(f"\n--- Matriks {name} ---")
    else:
        print("\n--- Hasil Perkalian Matriks ---")
    
    # Menentukan lebar maksimum untuk setiap kolom
    max_lens = [max(len(f"{elem:.2f}") for elem in col) for col in matrix.T]
    
    for row in matrix:
        print("|", end=" ")
        for i, elem in enumerate(row):
            print(f"{elem:>{max_lens[i]}.2f}", end=" ") # Format 2 angka di belakang koma
        print("|")

def explain_matrix_multiplication_formula():
    """
    Menjelaskan rumus perkalian matriks.
    """
    clear_screen()
    print("\n" + "="*50)
    animate_text("## 📚 Rumus Perkalian Matriks 📚")
    print("="*50)
    animate_text("Misalkan kita punya dua matriks, Matriks A dan Matriks B.")
    animate_text("Matriks A berukuran $m \\times n$ (m baris, n kolom).")
    animate_text("Matriks B berukuran $n \\times p$ (n baris, p kolom).")
    animate_text("Hasil perkalian A x B akan menghasilkan Matriks C berukuran $m \\times p$.")
    print("\nElemen $C_{ij}$ (elemen di baris i dan kolom j dari Matriks C) dihitung dengan rumus:")
    print("$$ C_{ij} = \\sum_{k=1}^{n} A_{ik} \\cdot B_{kj} $$")
    animate_text("\nIni berarti, untuk mendapatkan setiap elemen di matriks hasil:")
    animate_text("1. Ambil *baris ke-i* dari Matriks A.")
    animate_text("2. Ambil *kolom ke-j* dari Matriks B.")
    animate_text("3. Kalikan elemen pertama dari baris A dengan elemen pertama dari kolom B.")
    animate_text("4. Kalikan elemen kedua dari baris A dengan elemen kedua dari kolom B, dan seterusnya.")
    animate_text("5. *Jumlahkan* semua hasil perkalian tersebut.")
    print("\nContoh sederhana:")
    print("Jika $A = \\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix}$ dan $B = \\begin{pmatrix} e & f \\\\ g & h \\end{pmatrix}$")
    print("\nMaka $A \\cdot B = \\begin{pmatrix} (ae + bg) & (af + bh) \\\\ (ce + dg) & (cf + dh) \\end{pmatrix}$")
    animate_text("\nPenting: Jumlah kolom matriks pertama harus sama dengan jumlah baris matriks kedua.")
    animate_text("Jika tidak, perkalian matriks tidak dapat dilakukan.")
    print("="*50 + "\n")
    input("Tekan Enter untuk melanjutkan ke kalkulator...")
    clear_screen()

def main():
    """
    Fungsi utama untuk menjalankan kalkulator perkalian matriks.
    """
    clear_screen()
    print("\n" + "="*50)
    animate_text("        ✨ SELAMAT DATANG DI KALKULATOR ✨")
    animate_text("        ➕➖ PERKALIAN MATRIKS ✖➗")
    print("="*50)
    time.sleep(1)

    # 1. Panduan Penggunaan
    print("\n---")
    animate_text("## 💡 Panduan Penggunaan:")
    animate_text("1. Program ini akan meminta Anda untuk memasukkan *jumlah baris dan kolom* untuk dua matriks (Matriks A dan Matriks B).")
    animate_text("2. Kemudian, masukkan *elemen-elemen matriks baris per baris*, pisahkan setiap angka dengan spasi.")
    animate_text("3. Pastikan *jumlah kolom matriks pertama (Matriks A) sama dengan jumlah baris matriks kedua (Matriks B)* agar perkalian bisa dilakukan.")
    animate_text("4. Hasil perkalian akan ditampilkan dalam bentuk matriks yang rapi.")
    animate_text("5. Anda juga bisa menemukan *rumus perkalian matriks* di program ini!")
    time.sleep(1)

    # 2. Contoh Soal
    print("\n---")
    animate_text("## 📝 Contoh Soal:")
    animate_text("Mari kita coba kalikan Matriks A (2x2) dengan Matriks B (2x2) berikut:")
    print("   Matriks A:")
    print("   | 1  2 |")
    print("   | 3  4 |")
    print("   Matriks B:")
    print("   | 5  6 |")
    print("   | 7  8 |")
    animate_text("\nHasil perkalian A x B seharusnya:")
    print("   | (1*5 + 2*7)  (1*6 + 2*8) |   => | 19  22 |")
    print("   | (3*5 + 4*7)  (3*6 + 4*8) |   => | 43  50 |")
    animate_text("\nSekarang, mari kita buktikan dengan kalkulator!")
    time.sleep(2)

    choice = input("\nApakah Anda ingin melihat *rumus perkalian matriks* terlebih dahulu? (ya/tidak): ").lower()
    if choice == 'ya':
        explain_matrix_multiplication_formula()
    else:
        clear_screen()
        animate_text("Baik, mari langsung ke perhitungan!")
        time.sleep(1)

    print("\n" + "~"*50)
    animate_text("    🚀 Mari Masukkan Matriks Anda Sekarang! 🚀")
    print("~"*50)

    matrix_a = get_matrix_input("A")
    display_matrix(matrix_a, "A")

    matrix_b = get_matrix_input("B")
    display_matrix(matrix_b, "B")

    # Memeriksa apakah perkalian matriks bisa dilakukan
    print("\nMemproses perkalian...")
    time.sleep(1)
    if matrix_a.shape[1] != matrix_b.shape[0]:
        print("\n--- Error ---")
        animate_text("⛔ Perkalian tidak dapat dilakukan! ⛔")
        animate_text(f"Jumlah kolom Matriks A ({matrix_a.shape[1]}) TIDAK SAMA dengan jumlah baris Matriks B ({matrix_b.shape[0]}).")
        animate_text("Silakan coba lagi dengan dimensi matriks yang sesuai dengan aturan perkalian matriks.")
    else:
        result_matrix = np.dot(matrix_a, matrix_b)
        display_matrix(result_matrix)
        animate_text("\n🎉 Perkalian Matriks Selesai! 🎉")

    print("\n" + "="*50)
    animate_text("  Terima kasih telah menggunakan Kalkulator Perkalian Matriks!")
    print("="*50)

if _name_ == "_main_":
    main()
