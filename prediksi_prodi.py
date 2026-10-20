# Import tkinter dan buat jendela utama dengan latar biru
import tkinter as tk
 
BG = "#2f4a9a"        # biru latar
ENTRY_BG = "#4a63b0"  # biru muda untuk kolom input
 
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("420x620")
root.config(bg=BG)
