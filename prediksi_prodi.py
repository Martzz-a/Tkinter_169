# Import tkinter dan buat jendela utama dengan latar biru
import tkinter as tk
 
BG = "#2f4a9a"        # biru latar
ENTRY_BG = "#4a63b0"  # biru muda untuk kolom input
 
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("420x620")
root.config(bg=BG)

# Tambah label judul (putih, tebal) di bagian atas
judul = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan",
                 font=("Arial", 16, "bold"), bg=BG, fg="white")
judul.pack(pady=25)
