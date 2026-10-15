import subprocess
import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")  # Menggunakan aksen hijau segar

def buka_tambah_pasien():
    subprocess.run(["python", "tambah_pasien.py"])

def buka_tampil_pasien():
    subprocess.run(["python", "tampil_pasien.py"])

def menu_utama():
    root = ctk.CTk()
    root.title("Sistem Klinik Pratama Sehat")
    
    width, height = 440, 480
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

    # Frame Utama dengan sudut lebih melengkung dan kontras estetik
    frame_main = ctk.CTkFrame(root, corner_radius=20, fg_color=("#f4f9f5", "#1a2621"))
    frame_main.pack(pady=25, padx=25, fill="both", expand=True)

    # Header / Title Banner
    lbl_judul = ctk.CTkLabel(frame_main, text="🏥 KLINIK PRATAMA SEHAT", font=ctk.CTkFont(family="Segoe UI", size=20, weight="bold"))
    lbl_judul.pack(pady=(30, 5))

    lbl_sub = ctk.CTkLabel(frame_main, text="Sistem Manajemen Data Pasien Terpadu", font=ctk.CTkFont(family="Segoe UI", size=12), text_color=("#52796f", "#84a98c"))
    lbl_sub.pack(pady=(0, 25))

    # Tombol Menu Navigasi dengan warna hidup
    btn_tambah = ctk.CTkButton(
        frame_main, text="➕ Tambah Data Pasien", 
        font=ctk.CTkFont(family="Segoe UI", size=13, weight="bold"),
        width=300, height=48, corner_radius=10, 
        fg_color="#40916c", hover_color="#2d6a4f", text_color="white",
        command=buka_tambah_pasien
    )
    btn_tambah.pack(pady=10)

    btn_tampil = ctk.CTkButton(
        frame_main, text="📋 Tampilkan Daftar Pasien", 
        font=ctk.CTkFont(family="Segoe UI", size=13, weight="bold"),
        width=300, height=48, corner_radius=10, 
        fg_color="#40916c", hover_color="#2d6a4f", text_color="white",
        command=buka_tampil_pasien
    )
    btn_tampil.pack(pady=10)

    btn_keluar = ctk.CTkButton(
        frame_main, text="🚪 Keluar Aplikasi", 
        font=ctk.CTkFont(family="Segoe UI", size=13, weight="bold"),
        width=300, height=48, corner_radius=10, 
        fg_color="#e07a5f", hover_color="#bc4749", text_color="white",
        command=root.destroy
    )
    btn_keluar.pack(pady=(10, 25))

    root.mainloop()

if __name__ == "__main__":
    menu_utama()