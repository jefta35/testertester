import csv
import os
import customtkinter as ctk
from tkinter import messagebox
from models import Pasien

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

def simpan_pasien(entry_id, entry_nama, entry_keluhan, combo_gol, root):
    id_pasien = entry_id.get().strip()
    nama = entry_nama.get().strip()
    keluhan = entry_keluhan.get().strip()
    gol_darah = combo_gol.get().strip()

    if not id_pasien or not nama or not keluhan or gol_darah == "Pilih Golongan Darah":
        messagebox.showwarning("Peringatan", "Semua kolom wajib diisi dengan benar!")
        return

    pasien = Pasien(id_pasien, nama, keluhan, gol_darah)
    file_exists = os.path.exists("pasien.csv")

    with open("pasien.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["ID Pasien", "Nama", "Keluhan", "Gol. Darah", "Status"])
        writer.writerow(pasien.to_list())

    messagebox.showinfo("Berhasil", "Data pasien berhasil ditambahkan!")
    
    entry_id.delete(0, 'end')
    entry_nama.delete(0, 'end')
    entry_keluhan.delete(0, 'end')
    combo_gol.set("Pilih Golongan Darah")

def main():
    root = ctk.CTk()
    root.title("Tambah Data Pasien - Klinik Pratama")
    
    width, height = 460, 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_pos = (screen_width - width) // 2
    target_y = (screen_height - height) // 2
    current_y = target_y + 120

    root.geometry(f"{width}x{height}+{x_pos}+{current_y}")
    root.resizable(False, False)

    def animate_rise():
        nonlocal current_y
        if current_y > target_y:
            current_y -= 6
            root.geometry(f"{width}x{height}+{x_pos}+{current_y}")
            root.after(12, animate_rise)

    root.after(40, animate_rise)

    frame_main = ctk.CTkFrame(root, corner_radius=20, fg_color=("#f4f9f5", "#1a2621"))
    frame_main.pack(pady=25, padx=25, fill="both", expand=True)

    lbl_judul = ctk.CTkLabel(frame_main, text="📝 Form Tambah Pasien", font=ctk.CTkFont(family="Segoe UI", size=20, weight="bold"))
    lbl_judul.pack(pady=(25, 5))

    lbl_sub = ctk.CTkLabel(frame_main, text="Masukkan data medis pasien dengan lengkap", font=ctk.CTkFont(family="Segoe UI", size=12), text_color=("#52796f", "#84a98c"))
    lbl_sub.pack(pady=(0, 20))

    # Form Inputs
    entry_id = ctk.CTkEntry(frame_main, placeholder_text="🆔 ID Pasien (Cth: P001)", width=330, height=45, corner_radius=10, border_color="#52796f")
    entry_id.pack(pady=10)

    entry_nama = ctk.CTkEntry(frame_main, placeholder_text="👤 Nama Lengkap Pasien", width=330, height=45, corner_radius=10, border_color="#52796f")
    entry_nama.pack(pady=10)

    entry_keluhan = ctk.CTkEntry(frame_main, placeholder_text="🩺 Keluhan / Gejala Utama", width=330, height=45, corner_radius=10, border_color="#52796f")
    entry_keluhan.pack(pady=10)

    combo_gol = ctk.CTkComboBox(frame_main, values=["A", "B", "AB", "O"], width=330, height=45, corner_radius=10, border_color="#52796f", button_color="#2d6a4f", button_hover_color="#1b4332")
    combo_gol.pack(pady=10)
    combo_gol.set("Pilih Golongan Darah")

    # Tombol Simpan
    btn_simpan = ctk.CTkButton(
        frame_main, text="Simpan Data Pasien", 
        font=ctk.CTkFont(family="Segoe UI", size=13, weight="bold"),
        width=330, height=45, corner_radius=10, 
        fg_color="#2d6a4f", hover_color="#1b4332", text_color="white",
        command=lambda: simpan_pasien(entry_id, entry_nama, entry_keluhan, combo_gol, root)
    )
    btn_simpan.pack(pady=(15, 10))

    # Tombol Kembali (Hanya menutup window ini saja)
    btn_kembali = ctk.CTkButton(
        frame_main, text="⬅️ Kembali", 
        font=ctk.CTkFont(family="Segoe UI", size=12, weight="bold"),
        width=330, height=40, corner_radius=10, 
        fg_color="#6c757d", hover_color="#5a6268", text_color="white",
        command=root.destroy
    )
    btn_kembali.pack(pady=(0, 20))

    root.mainloop()

if __name__ == "__main__":
    main()