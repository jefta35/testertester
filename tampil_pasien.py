import csv
import os
import customtkinter as ctk
from tkinter import ttk, messagebox
from models import Pasien

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

def muat_data(tree):
    for item in tree.get_children():
        tree.delete(item)

    if not os.path.exists("pasien.csv"):
        return

    with open("pasien.csv", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader, None)  
        for row in reader:
            tree.insert("", "end", values=row)

def main():
    root = ctk.CTk()
    root.title("Daftar Pasien - Klinik Pratama")
    
    # Perbesar ukuran jendela agar lebih lega
    width, height = 980, 620
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
    frame_main.pack(pady=20, padx=20, fill="both", expand=True)

    lbl_judul = ctk.CTkLabel(frame_main, text="📊 Daftar Pasien Klinik Pratama", font=ctk.CTkFont(family="Segoe UI", size=20, weight="bold"))
    lbl_judul.pack(pady=(20, 5))

    lbl_sub = ctk.CTkLabel(frame_main, text="Rekapitulasi data pasien aktif yang terdaftar dalam sistem", font=ctk.CTkFont(family="Segoe UI", size=12), text_color=("#52796f", "#84a98c"))
    lbl_sub.pack(pady=(0, 15))

    style = ttk.Style()
    style.theme_use("clam")
    
    is_dark = ctk.get_appearance_mode() == "Dark"
    bg_color = "#24342e" if is_dark else "#ffffff"
    fg_color = "#ffffff" if is_dark else "#2b2b2b"
    header_bg = "#2d6a4f"
    
    # Perbesar ukuran font tabel dan tinggi baris (rowheight) agar tidak terpotong
    style.configure(
        "Treeview", 
        background=bg_color,
        foreground=fg_color,
        rowheight=42, 
        fieldbackground=bg_color,
        font=("Segoe UI", 11)
    )
    style.configure(
        "Treeview.Heading", 
        font=("Segoe UI", 12, "bold"), 
        background=header_bg, 
        foreground="white",
        relief="flat"
    )
    style.map("Treeview", background=[('selected', '#40916c')])

    frame_tabel = ctk.CTkFrame(frame_main, corner_radius=12, fg_color=("#ffffff", "#121b17"))
    frame_tabel.pack(pady=5, padx=20, fill="both", expand=True)

    columns = ("ID Pasien", "Nama Pasien", "Keluhan", "Gol. Darah", "Status")
    tree = ttk.Treeview(frame_tabel, columns=columns, show="headings", height=8)

    # Perlebar ukuran kolom agar teks panjang tidak terpotong
    col_widths = [140, 220, 300, 110, 130]
    for col, width_col in zip(columns, col_widths):
        tree.heading(col, text=col)
        tree.column(col, width=width_col, anchor="center")

    tree.pack(side="left", fill="both", expand=True, padx=10, pady=10)

    scrollbar = ctk.CTkScrollbar(frame_tabel, command=tree.yview, button_color="#2d6a4f", button_hover_color="#1b4332")
    scrollbar.pack(side="right", fill="y", pady=10)
    tree.configure(yscrollcommand=scrollbar.set)

    muat_data(tree)

    # Frame Tombol Aksi di Bawah (Refresh & Tombol Kembali yang lengkap)
    frame_btn = ctk.CTkFrame(frame_main, fg_color="transparent")
    frame_btn.pack(pady=15)

    btn_refresh = ctk.CTkButton(
        frame_btn, text="🔄 Refresh Data", 
        font=ctk.CTkFont(family="Segoe UI", size=12, weight="bold"),
        width=200, height=42, corner_radius=10, 
        fg_color="#2d6a4f", hover_color="#1b4332", text_color="white",
        command=lambda: muat_data(tree)
    )
    btn_refresh.pack(side="left", padx=15)

    # Tombol Kembali (Menutup window ini saja)
    btn_kembali = ctk.CTkButton(
        frame_btn, text="⬅️ Kembali", 
        font=ctk.CTkFont(family="Segoe UI", size=12, weight="bold"),
        width=200, height=42, corner_radius=10, 
        fg_color="#6c757d", hover_color="#5a6268", text_color="white",
        command=root.destroy
    )
    btn_kembali.pack(side="left", padx=15)

    root.mainloop()

if __name__ == "__main__":
    main()