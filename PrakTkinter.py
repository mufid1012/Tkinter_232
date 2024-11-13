import tkinter as tk  # Mengimpor tkinter untuk membuat GUI
from tkinter import messagebox  # Mengimpor messagebox untuk menampilkan pesan error

# Fungsi untuk menghitung prediksi program studi berdasarkan nilai rata-rata
def hasil_prediksi():
    try:
        total_nilai = 0  # Menginisialisasi total nilai
        for entry in entries:
            # Mendapatkan nilai dari setiap entry field dan mengonversinya ke integer
            nilai = int(entry.get())
            # Memeriksa apakah nilai berada dalam rentang 0 hingga 100
            if not (0 <= nilai <= 100):
                raise ValueError("Nilai harus antara 0 dan 100.")
            total_nilai += nilai  # Menambahkan nilai ke total nilai

        # Menghitung nilai rata-rata
        rata_rata = total_nilai / len(entries)
        
        # Menentukan program studi berdasarkan nilai rata-rata
        if rata_rata >= 80:
            prodi = "Teknologi Informasi"
        elif 60 <= rata_rata < 80:
            prodi = "Pendidikan Bahasa"
        elif 50 <= rata_rata < 60:
            prodi = "Pertanian"
        else:
            prodi = "Tidak ada prodi yang cocok"
        
        # Menampilkan hasil prediksi di label hasil_label
        hasil_label.config(text=f"Prediksi Prodi: {prodi} (Rata-rata: {rata_rata:.2f})")
        
    except ValueError as ve:
        # Menampilkan pesan error jika input tidak valid
        messagebox.showerror("Input Error", "Pastikan semua input adalah angka antara 0 dan 100.")

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")  # Mengatur judul jendela
root.geometry("500x600")  # Mengatur ukuran jendela
root.configure(bg="#f0f0f0")  # Mengatur warna latar belakang

# Label judul di bagian atas jendela
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 18, "bold"), bg="#f0f0f0")
judul_label.pack(pady=20)  # Menambahkan jarak di sekitar label judul

# Frame untuk menampung input nilai
frame_input = tk.Frame(root, bg="#f0f0f0")
frame_input.pack(pady=10)

entries = []  # List untuk menyimpan widget entry nilai
for i in range(10):
    # Label untuk setiap input nilai mata pelajaran
    label = tk.Label(frame_input, text=f"Nilai Mata Pelajaran {i + 1}:", font=("Arial", 12), bg="#f0f0f0")
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
    
    # Entry field untuk setiap nilai mata pelajaran
    entry = tk.Entry(frame_input, width=10, font=("Arial", 12))
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)  # Menambahkan setiap entry ke dalam list entries

# Tombol untuk menjalankan perhitungan prediksi
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi, font=("Arial", 12, "bold"), bg="#4CAF50", fg="black")
prediksi_button.pack(pady=30)  # Menambahkan jarak di sekitar tombol

# Label untuk menampilkan hasil prediksi
hasil_label = tk.Label(root, text="", font=("Arial", 14, "italic", "bold"), fg="blue", bg="#f0f0f0")
hasil_label.pack(pady=20)

# Menjalankan loop utama aplikasi
root.mainloop()
