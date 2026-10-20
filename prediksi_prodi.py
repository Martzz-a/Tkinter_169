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
 
# Buat frame untuk menampung 10 baris input nilai
frame_input = tk.Frame(root, bg=BG)
frame_input.pack()
 
# Buat 10 label "Nilai Mata Pelajaran N:" rata kanan dengan grid dan 10 kolom input (Entry) di samping label dan simpan ke daftar
daftar_entry = []
for i in range(10):
    label = tk.Label(frame_input, text="Nilai Mata Pelajaran " + str(i + 1) + ":",
                     font=("Arial", 10, "bold"), bg=BG, fg="white")
    label.grid(row=i, column=0, sticky="e", padx=10, pady=6)
 
    entry = tk.Entry(frame_input, width=18, bg=ENTRY_BG, fg="white",
                     bd=0, insertbackground="white")
    entry.grid(row=i, column=1, padx=10, pady=6)
    daftar_entry.append(entry)
 
# Tambah teks "Pilihan Jurusan Anda:" di bawah daftar input
label_pilihan = tk.Label(root, text="Pilihan Jurusan Anda:",
                         font=("Arial", 10, "bold"), bg=BG, fg="white")
label_pilihan.pack(pady=(25, 5))
 
# Buat dropdown pilihan prodi dengan OptionMenu, bawaan "Teknologi Informasi"
daftar_prodi = ["Teknologi Informasi", "Teknik Sipil", "Teknik Mesin",
                "Teknik Elektro", "Arsitektur"]
pilihan = tk.StringVar()
pilihan.set("Teknologi Informasi")
 
dropdown = tk.OptionMenu(root, pilihan, *daftar_prodi)
dropdown.config(bg=ENTRY_BG, fg="white", width=18, bd=0)
dropdown.pack()
