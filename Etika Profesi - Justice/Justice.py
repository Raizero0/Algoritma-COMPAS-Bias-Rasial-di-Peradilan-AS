import customtkinter as ctk
import random
import tkinter as tk
# Setup Dasar
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class JusticeLens(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("JusticeLens")
        self.geometry("1400x800")
        self.selected_mode = None

        # 1. Bikin Canvas untuk Background Melayang
        self.main_container = ctk.CTkFrame(self, fg_color="#121212")
        self.main_container.pack(fill="both", expand=True)

        # 2. Data kata-kata dan biner
        self.words = ["Keadilan", "Peradilan", "Hukum", "Kesetaraan", "Hak Asasi", "Integritas", "Transparansi"]
        self.binary = ["01011001", "11001010", "10101011", "00110011"]
        self.floating_items = []
        self.setup_floating_text()

        # Mulai animasi
        self.animate()
        self.show_halaman_satu()
        

    def setup_floating_text(self):
        # Gabungin kata & biner, looping biar rame
        all_pool = self.words * 3 + self.binary * 5 
        
        for text in all_pool:
            x = random.randint(0, 1400)
            y = random.randint(0, 800)
            dx = random.uniform(-0.5, 0.5) # Kecepatan pelan biar estetik
            dy = random.uniform(-0.5, 0.5)
            
            lbl = ctk.CTkLabel(
                self.main_container, 
                text=text, 
                text_color="#244D61", 
                font=ctk.CTkFont(family="Courier", size=14, weight="bold")
            )
            lbl.place(x=x, y=y)
            
            self.floating_items.append({"lbl": lbl, "x": x, "y": y, "dx": dx, "dy": dy})

    def animate(self):
        # Cek dulu apakah canvas masih ada, buat jaga-jaga kalau program ditutup
        if not self.winfo_exists():
            return

        w = self.winfo_width()
        h = self.winfo_height()
        
        if w < 10 or h < 10:
            w, h = 1400, 800

        for item in self.floating_items:
            # Update koordinat x dan y
            item["x"] += item["dx"]
            item["y"] += item["dy"]
            
            # Pantulan ke ujung layar
            if item["x"] <= 0 or item["x"] >= w:
                item["dx"] *= -1
            if item["y"] <= 0 or item["y"] >= h:
                item["dy"] *= -1
                
            # Terapkan posisi baru ke label
            item["lbl"].place(x=item["x"], y=item["y"])
                
        self.after(20, self.animate)

    def clear_frame(self):
        """Menghapus semua widget di container sebelum ganti halaman"""
        floating_widgets = [item["lbl"] for item in self.floating_items]
        
        for widget in self.main_container.winfo_children():
            if widget not in floating_widgets:
                widget.destroy()
    
    def set_background_theme(self, tema):
        if tema == "default":
            bg_color = "#121212"
            text_color = "#244D61"
            pool_teks = self.words * 3 + self.binary * 5
            
        elif tema == "compas":
            bg_color = "#1A0505"
            text_color = "#661111"
            pool_teks = ["RISK", "CRIMINAL", "BIAS", "PREDICTION", "DANGER", "SOCIETY", "ZIP-CODE"]
            
        elif tema == "justice":
            bg_color = "#051A11"
            text_color = "#116644"
            pool_teks = ["EQUITY", "FAIRNESS", "MERIT", "NEUTRAL", "TRANSPARENT", "BALANCE", "JUSTICE"]

        # 1. Update warna background full screen
        self.main_container.configure(fg_color=bg_color)
        
        # 2. Update warna dan isi teks yang melayang
        for item in self.floating_items:
            item["lbl"].configure(text_color=text_color, text=random.choice(pool_teks))

    # ==========================================
    # HALAMAN 1: HOME
    # ==========================================
    def show_halaman_satu(self):
        self.clear_frame()
        
        self.set_background_theme("default")

        # Judul Program
        label_judul = ctk.CTkLabel(
            self.main_container, 
            text="JusticeLens", 
            font=ctk.CTkFont(size=60, weight="bold"),
            text_color="#00D4FF" # Cyan Default
        )
        label_judul.pack(pady=(120, 5))

        # Tagline (Kata-kata kecil tipis)
        label_tagline = ctk.CTkLabel(
            self.main_container, 
            text="Peeling back the layers of algorithmic bias.", 
            font=ctk.CTkFont(size=16, slant="italic"),
            text_color="#666666" # Abu-abu tipis
        )
        label_tagline.pack(pady=(0, 60))

        # Button Mulai
        btn_mulai = ctk.CTkButton(
            self.main_container, 
            text="MULAI", 
            width=280,
            height=50,
            fg_color="#00D4FF",
            text_color="#121212",
            font=ctk.CTkFont(size=18, weight="bold"),
            hover_color="#00AACC",
            command=self.show_halaman_dua # Pindah ke Hal 2
        )
        btn_mulai.pack(pady=10)

        # Button Sejarah Kasus
        btn_sejarah = ctk.CTkButton(
            self.main_container, 
            text="SEJARAH KASUS", 
            width=280,
            height=50,
            border_width=2,
            fg_color="transparent",
            border_color="#00D4FF",
            text_color="#00D4FF",
            font=ctk.CTkFont(size=18, weight="bold"),
            hover_color="#1E1E26",
            command=self.show_sejarah # Pop-up atau halaman sejarah
        )
        btn_sejarah.pack(pady=10)

        # Button Credits (Taruh di bawah btn_sejarah)
        btn_credits = ctk.CTkButton(
            self.main_container, 
            text="CREDITS", 
            width=280,
            height=50,
            border_width=2,
            fg_color="transparent",
            border_color="#00FFA3", # Pake warna hijau neon biar beda dikit
            text_color="#00FFA3",
            font=ctk.CTkFont(size=18, weight="bold"),
            hover_color="#142D24",
            command=self.show_credits # Fungsi yang akan kita buat
        )
        btn_credits.pack(pady=10)

        # Button Keluar
        btn_keluar = ctk.CTkButton(
            self.main_container, 
            text="KELUAR", 
            width=280,
            height=50,
            fg_color="#333333",
            text_color="white",
            font=ctk.CTkFont(size=18, weight="bold"),
            hover_color="#FF4D4D",
            command=self.quit
        )
        btn_keluar.pack(pady=50)

    
    # ==========================================
    # HALAMAN: SEJARAH KASUS (COMPREHENSIVE)
    # ==========================================
    def show_sejarah(self):
        self.clear_frame()
        self.set_background_theme("default")

        # Judul Program
        label_judul = ctk.CTkLabel(
            self.main_container, 
            text="JusticeLens", 
            font=ctk.CTkFont(size=40, weight="bold"),
            text_color="#00D4FF"
        )
        label_judul.pack(pady=(30, 5))

        # Subtitle Sejarah
        label_subtitle = ctk.CTkLabel(
            self.main_container, 
            text="RIWAYAT LENGKAP: SKANDAL BIAS ALGORITMA COMPAS", 
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color="#FFFFFF"
        )
        label_subtitle.pack(pady=(0, 15))

        # Border/Frame Scrollable untuk Sejarah
        scroll_frame = ctk.CTkScrollableFrame(
            self.main_container,
            width=850,
            height=380,
            fg_color="#1E1E26",
            border_width=2,
            border_color="#00D4FF"
        )
        scroll_frame.pack(pady=10, padx=20)

        # Narasi Sejarah Lengkap
        sejarah_lengkap = (
            "1. KELAHIRAN DAN AMBISI AWAL (1998 - 2000-an)\n"
            "COMPAS dikembangkan oleh Northpointe (sekarang bernama Equivant) pada tahun 1998. "
            "Tujuan awalnya mulia: membantu sistem peradilan pidana di Amerika Serikat yang "
            "kewalahan untuk menentukan terdakwa mana yang paling mungkin melakukan kejahatan lagi "
            "(residivisme) dan mana yang bisa diberikan alternatif hukuman selain penjara.\n\n"
            
            "2. IMPLEMENTASI MASIF DI PERADILAN\n"
            "Memasuki tahun 2010-an, algoritma ini telah digunakan di ribuan yurisdiksi di berbagai negara bagian, "
            "termasuk New York, Wisconsin, California, dan Florida. Hakim mengandalkan skor 1-10 yang dihasilkan "
            "COMPAS untuk menentukan masa depan seseorang tanpa mengetahui bagaimana skor itu dihitung karena "
            "logika algoritmanya dianggap sebagai 'Rahasia Dagang' perusahaan.\n\n"
            
            "3. MEI 2016: INVESTIGASI 'MACHINE BIAS' OLEH PROPUBLICA\n"
            "Titik balik terjadi pada 23 Mei 2016. Organisasi jurnalisme investigasi ProPublica merilis "
            "laporan mendalam berjudul 'Machine Bias'. Mereka menganalisis skor risiko COMPAS terhadap "
            "lebih dari 7.000 orang yang ditangkap di Broward County, Florida, selama tahun 2013-2014.\n\n"
            
            "4. TEMUAN DATA STATISTIK YANG MENGERIKAN\n"
            "Setelah memantau terdakwa tersebut selama 2 tahun, ProPublica menemukan pola rasisme sistemik:\n"
            "• Kesalahan Prediksi Kulit Hitam: Terdakwa kulit hitam dua kali lebih sering salah diklasifikasikan "
            "sebagai 'High Risk' (44.9%) dibandingkan kulit putih (23.5%). Mereka dicap berbahaya padahal tidak "
            "pernah melakukan pelanggaran lagi.\n"
            "• Kesalahan Prediksi Kulit Putih: Terdakwa kulit putih yang sebenarnya berbahaya justru sering "
            "mendapatkan label 'Low Risk' (47.7%) dibandingkan kulit hitam (28.0%).\n\n"
            
            "5. TERBONGKARNYA 'KEY PROXY FEATURES'\n"
            "Penyelidikan mengungkap bahwa meskipun pertanyaan 'Apa ras Anda?' tidak digunakan, algoritma "
            "ini menggunakan 137 pertanyaan kuesioner yang mencakup:\n"
            "• 'Apakah ada orang tua Anda yang pernah dipenjara?'\n"
            "• 'Berapa banyak teman Anda yang menggunakan obat terlarang?'\n"
            "• Alamat tinggal (Zip Code) dan status ekonomi.\n"
            "Di Amerika, variabel ini sangat berkorelasi dengan sejarah segregasi rasial, sehingga variabel tersebut "
            "menjadi 'Proxy' (perwakilan) yang secara tidak langsung menghukum ras tertentu.\n\n"
            
            "6. KASUS STATE V. LOOMIS (2016)\n"
            "Salah satu kasus hukum paling terkenal adalah Eric Loomis di Wisconsin. Ia menantang skor COMPAS-nya, "
            "berargumen bahwa haknya untuk diadili secara adil terlanggar karena ia tidak bisa meninjau metodologi "
            "algoritma yang menghukumnya. Namun, Mahkamah Agung Wisconsin tetap mengizinkan penggunaan COMPAS "
            "dengan catatan: hakim harus diingatkan akan potensi bias dan tidak boleh menjadikannya faktor penentu tunggal.\n\n"
            
            "7. DAMPAK DUNIA SAAT INI\n"
            "Hingga hari ini, kasus COMPAS menjadi studi kasus utama di seluruh universitas hukum dan informatika "
            "di dunia tentang bahaya 'Black Box AI'. Kasus ini memaksa banyak negara untuk mulai menyusun regulasi "
            "mengenai transparansi algoritma agar teknologi tidak memperkuat ketidakadilan masa lalu.\n\n"
            
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "SUMBER REFERENSI DATA:\n"
            "• ProPublica Investigative Report: 'Machine Bias' (Angwin et al., 2016).\n"
            "• Harvard Law Review: 'State v. Loomis' (2017).\n"
            "• MIT Technology Review: 'The real problem with algorithmic bias'.\n"
            "• Equivant/Northpointe Technical Manual for COMPAS."
        )

        label_isi_sejarah = ctk.CTkLabel(
            scroll_frame,
            text=sejarah_lengkap,
            font=ctk.CTkFont(size=14),
            text_color="#E1E1E1",
            justify="left",
            wraplength=800
        )
        label_isi_sejarah.pack(pady=10, padx=15)

        # Button Kembali ke Halaman 1
        btn_kembali = ctk.CTkButton(
            self.main_container, 
            text="KEMBALI KE MENU UTAMA", 
            width=250,
            height=45,
            fg_color="#333333",
            text_color="white",
            font=ctk.CTkFont(size=16, weight="bold"),
            hover_color="#00D4FF",
            command=self.show_halaman_satu
        )
        btn_kembali.pack(pady=20)
        

    # ==========================================
    # HALAMAN: CREDITS (NEW LOOK 2-3 FORMATION)
    # ==========================================
    def show_credits(self):
        self.clear_frame()
        self.set_background_theme("default")

        # Judul Halaman
        label_judul = ctk.CTkLabel(
            self.main_container, 
            text="JusticeLens", 
            font=ctk.CTkFont(size=45, weight="bold"),
            text_color="#00D4FF"
        )
        label_judul.pack(pady=(40, 5))

        label_tim = ctk.CTkLabel(
            self.main_container, 
            text="ANGGOTA TIM JUSTICE", 
            font=ctk.CTkFont(size=22, weight="bold"),
            text_color="#FFFFFF"
        )
        label_tim.pack(pady=(0, 30))

        # Data Anggota
        anggota = [
            ("Railene Akbillah Ramadhan Haryanto*", "4524210081"),
            ("M Hafiz Saputra", "4524210115"),
            ("Syalva Kirania Kresti", "4524210101"),
            ("Zoeffanya Cianda Larasati Akbar", "4524210106"),
            ("Nabila Khoirun Nisaa’", "4524210116")
        ]

        # Container Utama untuk Baris
        cards_container = ctk.CTkFrame(self.main_container, fg_color="transparent")
        cards_container.pack(expand=True, fill="both", padx=50)

        # Baris Atas (2 Orang)
        row_top = ctk.CTkFrame(cards_container, fg_color="transparent")
        row_top.pack(pady=10)

        # Baris Bawah (3 Orang)
        row_bottom = ctk.CTkFrame(cards_container, fg_color="transparent")
        row_bottom.pack(pady=10)

        def create_member_card(parent, name, npm):
            # Frame Utama Card - Default ada aksen biru
            card = ctk.CTkFrame(
                parent, 
                width=280, 
                height=140, 
                corner_radius=20,
                border_width=2,
                border_color="#00D4FF", # Aksen biru default
                fg_color="#1E1E26"
            )
            card.pack(side="left", padx=20)
            card.pack_propagate(False)

            # Label Nama
            name_label = ctk.CTkLabel(
                card, 
                text=name, 
                font=ctk.CTkFont(size=14, weight="bold"),
                text_color="#00D4FF",
                wraplength=240
            )
            name_label.place(relx=0.5, rely=0.4, anchor="center")

            # Label NPM
            npm_label = ctk.CTkLabel(
                card, 
                text=npm, 
                font=ctk.CTkFont(size=13),
                text_color="#AAAAAA"
            )
            npm_label.place(relx=0.5, rely=0.7, anchor="center")

            # Efek Hover Neon Menyala
            def on_enter(_):
                card.configure(border_color="#00FFFF", border_width=4, fg_color="#252533") # Neon & Tebal
                name_label.configure(text_color="#FFFFFF")

            def on_leave(_):
                card.configure(border_color="#00D4FF", border_width=2, fg_color="#1E1E26") # Balik default
                name_label.configure(text_color="#00D4FF")

            # Bind event biar smooth
            card.bind("<Enter>", on_enter)
            card.bind("<Leave>", on_leave)
            # Bind juga ke labelnya biar hover nggak putus
            name_label.bind("<Enter>", on_enter)
            npm_label.bind("<Enter>", on_enter)

        # Masukin data ke formasi 2-3
        for i, (nama, npm) in enumerate(anggota):
            if i < 2:
                create_member_card(row_top, nama, npm)
            else:
                create_member_card(row_bottom, nama, npm)

        # Button Kembali ke Halaman 1
        btn_kembali = ctk.CTkButton(
            self.main_container, 
            text="KEMBALI KE MENU UTAMA", 
            width=280,
            height=50,
            fg_color="#333333",
            text_color="white",
            font=ctk.CTkFont(size=16, weight="bold"),
            hover_color="#00D4FF",
            command=self.show_halaman_satu
        )
        btn_kembali.pack(pady=(20, 40))
        
    # ==========================================
    # HALAMAN 2: PILIH MODE (ALGORITMA)
    # ==========================================
    def show_halaman_dua(self):
        self.clear_frame()
        
        self.set_background_theme("default")
        
        # Inisialisasi variabel pilihan jika belum ada
        if not hasattr(self, 'selected_mode'):
            self.selected_mode = None

        # Judul Program
        label_judul = ctk.CTkLabel(
            self.main_container, 
            text="JusticeLens", 
            font=ctk.CTkFont(size=45, weight="bold"),
            text_color="#00D4FF"
        )
        label_judul.pack(pady=(60, 10))

        # Instruksi
        label_instruksi = ctk.CTkLabel(
            self.main_container, 
            text="Pilih algoritma yang ingin dijalankan:", 
            font=ctk.CTkFont(size=20),
            text_color="#FFFFFF"
        )
        label_instruksi.pack(pady=(0, 40))

        # Container Tombol Mode (Side by Side)
        mode_frame = ctk.CTkFrame(self.main_container, fg_color="transparent")
        mode_frame.pack(pady=20)

        # Fungsi Internal untuk Update Visual Tombol saat Dipilih
        def set_selection(mode):
            self.selected_mode = mode
            if mode == "compas":
                btn_compas.configure(border_color="#FF4D4D", border_width=4, text_color="#FF4D4D")
                btn_justice.configure(border_color="#00D4FF", border_width=2, text_color="#00D4FF")
            else:
                btn_justice.configure(border_color="#00FFA3", border_width=4, text_color="#00FFA3")
                btn_compas.configure(border_color="#00D4FF", border_width=2, text_color="#00D4FF")

        # Tombol Mode COMPAS
        btn_compas = ctk.CTkButton(
            mode_frame, 
            text="COMPAS\n(Risk Assessment)", 
            width=300,
            height=150,
            corner_radius=20,
            border_width=2,
            border_color="#00D4FF",
            fg_color="#1E1E26",
            text_color="#00D4FF",
            font=ctk.CTkFont(size=20, weight="bold"),
            hover_color="#252533",
            command=lambda: set_selection("compas")
        )
        btn_compas.pack(side="left", padx=20)

        # Tombol Mode JUSTICE
        btn_justice = ctk.CTkButton(
            mode_frame, 
            text="JUSTICE\n(Fair Algorithm)", 
            width=300,
            height=150,
            corner_radius=20,
            border_width=2,
            border_color="#00D4FF",
            fg_color="#1E1E26",
            text_color="#00D4FF",
            font=ctk.CTkFont(size=20, weight="bold"),
            hover_color="#252533",
            command=lambda: set_selection("justice")
        )
        btn_justice.pack(side="left", padx=20)

        # Container Tombol Navigasi (Bawah)
        nav_frame = ctk.CTkFrame(self.main_container, fg_color="transparent")
        nav_frame.pack(side="bottom", pady=80)

        # Tombol Kembali
        btn_kembali = ctk.CTkButton(
            nav_frame, 
            text="KEMBALI", 
            width=150,
            height=45,
            fg_color="#333333",
            text_color="white",
            font=ctk.CTkFont(size=16, weight="bold"),
            hover_color="#555555",
            command=self.show_halaman_satu
        )
        btn_kembali.pack(side="left", padx=10)

        # Tombol Lanjut
        btn_lanjut = ctk.CTkButton(
            nav_frame, 
            text="LANJUT", 
            width=150,
            height=45,
            fg_color="#00D4FF",
            text_color="#121212",
            font=ctk.CTkFont(size=16, weight="bold"),
            hover_color="#00AACC",
            command=self.proses_lanjut # Logika pindah halaman
        )
        btn_lanjut.pack(side="left", padx=10)

    # ==========================================
    # LOGIKA PINDAH HALAMAN BERDASARKAN MODE
    # ==========================================
    def proses_lanjut(self):
        if self.selected_mode == "compas":
            print("Navigasi ke Halaman 3 (Selection COMPAS)")
            self.show_halaman_tiga()
        elif self.selected_mode == "justice":
            print("Navigasi ke Halaman 5 (Selection JUSTICE)")
            self.show_halaman_lima()
        else:
            # Opsional: Tambahin notifikasi kalau belum pilih mode
            print("Tolong pilih salah satu algoritma dulu, bro!")

    # ==========================================
    # HALAMAN 3: COMPAS SELECTION (KING PROXY: ZIP CODE)
    # ==========================================
    def show_halaman_tiga(self):
        self.clear_frame()
        
        self.set_background_theme("compas")

        # Judul Halaman
        label_judul = ctk.CTkLabel(
            self.main_container, 
            text="JusticeLens", 
            font=ctk.CTkFont(size=45, weight="bold"),
            text_color="#FF4D4D"
        )
        label_judul.pack(pady=(20, 5))

        label_mode = ctk.CTkLabel(
            self.main_container, 
            text="ALGORITMA COMPAS: SELEKSI PROFIL TERDAKWA", 
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color="#FFFFFF"
        )
        label_mode.pack(pady=(0, 10))

        # DATASET SEIMBANG (Proxy: Kode Pos / Zip Code)
        # 4 Atas: Black Proxy Area (33311/33313) | 4 Bawah: White Proxy Area (33301/33308)
        self.terdakwa_list = [
            {"id": "USR-001", "nama": "Marcus J.", "umur": 24, "gender": "Laki-laki", "alamat": "North Broward", "zip": "33311", "kasus": "Kepemilikan Obat Terlarang", "riwayat": "1 Prior"}, # ini algoritma key proxy feature dipakenya disini
            {"id": "USR-002", "nama": "Darnell T.", "umur": 29, "gender": "Laki-laki", "alamat": "Lauderhill", "zip": "33311", "kasus": "Memasuki wilayah tanpa izin", "riwayat": "0 Prior"},    # ini algoritma key proxy feature dipakenya disini
            {"id": "USR-003", "nama": "Andre L.", "umur": 32, "gender": "Laki-laki", "alamat": "Pompano Beach", "zip": "33313", "kasus": "Pencurian Ringan", "riwayat": "2 Priors"},   # ini algoritma key proxy feature dipakenya disini
            {"id": "USR-004", "nama": "Tyrone W.", "umur": 21, "gender": "Laki-laki", "alamat": "Fort Lauderdale", "zip": "33311", "kasus": "Mengemudi ugal ugalan", "riwayat": "0 Prior"}, # ini algoritma key proxy feature dipakenya disini
            
            {"id": "USR-005", "nama": "Dylan S.", "umur": 25, "gender": "Laki-laki", "alamat": "Coral Springs", "zip": "33301", "kasus": "Kepemilikan Obat Terlarang", "riwayat": "1 Prior"}, # zip elit
            {"id": "USR-006", "nama": "Branden M.", "umur": 28, "gender": "Laki-laki", "alamat": "Boca Raton", "zip": "33308", "kasus": "Memasuki wilayah tanpa izin", "riwayat": "0 Prior"},    # zip elit
            {"id": "USR-007", "nama": "Scott P.", "umur": 35, "gender": "Laki-laki", "alamat": "Parkland", "zip": "33301", "kasus": "Pencurian Ringan", "riwayat": "3 Priors"},      # zip elit
            {"id": "USR-008", "nama": "Cody R.", "umur": 22, "gender": "Laki-laki", "alamat": "Weston", "zip": "33301", "kasus": "Mengemudi ugal ugalan", "riwayat": "0 Prior"},     # zip elit
        ]

        # Container Scrollable
        scroll_container = ctk.CTkScrollableFrame(self.main_container, width=1150, height=450, fg_color="transparent", scrollbar_button_color="#441111")
        scroll_container.pack(pady=10, padx=20)

        grid_frame = ctk.CTkFrame(scroll_container, fg_color="transparent")
        grid_frame.pack()

        self.selected_terdakwa = None
        self.card_frames = []

        def select_card(idx, frame):
            self.selected_terdakwa = self.terdakwa_list[idx]
            for f in self.card_frames:
                f.configure(border_color="#441111", border_width=2)
            frame.configure(border_color="#FF4D4D", border_width=4)

        for i in range(4):
            grid_frame.grid_columnconfigure(i, weight=1, uniform="kolom_kartu")
    
        for i, data in enumerate(self.terdakwa_list):
            row, col = i // 4, i % 4
            
            # 2. Ukuran Card dibikin ideal: 260x290
            card = ctk.CTkFrame(grid_frame, width=260, height=290, corner_radius=18, border_width=2, border_color="#441111", fg_color="#2A0A0A")
            card.grid(row=row, column=col, padx=10, pady=10)
            card.grid_propagate(False)

            # 3. Tambahin padx=15 di semua label biar ngga mepet border
            ctk.CTkLabel(card, text=data['id'], font=ctk.CTkFont(size=10), text_color="#888888").pack(pady=(15, 0), padx=15)
            ctk.CTkLabel(card, text=data['nama'].upper(), font=ctk.CTkFont(size=17, weight="bold"), text_color="#FF4D4D").pack(pady=(0, 10), padx=15)

            def add_row(parent, txt, color="#BBBBBB", weight="normal"): 
                lbl = ctk.CTkLabel(parent, text=txt, font=ctk.CTkFont(size=12, weight=weight), text_color=color)
                # Tambah padx=15 disini bro!
                lbl.pack(pady=2, padx=15) 

            add_row(card, f"{data['umur']} Thn | {data['gender']}")
            add_row(card, f"Kasus: {data['kasus']}")
            add_row(card, f"Riwayat: {data['riwayat']}")
            
            # Footer juga ditambahin padx
            footer = ctk.CTkFrame(card, fg_color="transparent")
            footer.pack(side="bottom", fill="x", pady=(5, 15))
            ctk.CTkLabel(
                footer, 
                text=f"{data['alamat']}\nZip Code: {data['zip']}", 
                font=ctk.CTkFont(size=11, weight="bold"), 
                text_color="#FFD700" if data['zip'] in ["33311", "33313"] else "#666666"
            ).pack(padx=15)

            # Logic Klik
            idx_now = i
            def on_click(_, idx=idx_now, f=card): select_card(idx, f)
            
            card.bind("<Button-1>", on_click)
            for child in card.winfo_children():
                child.bind("<Button-1>", on_click)
                if isinstance(child, ctk.CTkFrame):
                    for sub in child.winfo_children():
                        sub.bind("<Button-1>", on_click)

            self.card_frames.append(card)

        # Navigasi Bawah
        nav_frame = ctk.CTkFrame(self.main_container, fg_color="transparent")
        nav_frame.pack(side="bottom", pady=20)

        ctk.CTkButton(nav_frame, text="KEMBALI", width=160, height=45, fg_color="#333333", command=self.show_halaman_dua).pack(side="left", padx=10)
        ctk.CTkButton(nav_frame, text="PROSES SKOR", width=160, height=45, fg_color="#FF4D4D", font=ctk.CTkFont(weight="bold"), command=self.show_halaman_empat).pack(side="left", padx=10)

    # ==========================================
    # HALAMAN 4: COMPAS RESULT (PURE ZIP-CODE BIAS)
    # ==========================================
    def show_halaman_empat(self):
        if not self.selected_terdakwa: return
        self.clear_frame()
        self.set_background_theme("compas")

        result_frame = ctk.CTkFrame(self.main_container, fg_color="#2A0A0A", border_width=2, border_color="#FF4D4D", width=850, height=450)
        result_frame.pack(pady=60)
        result_frame.pack_propagate(False)

        self.loading_label = ctk.CTkLabel(result_frame, text="SCANNING ZIP-CODE PROXY...", font=ctk.CTkFont(size=24, weight="bold"), text_color="#FF4D4D")
        self.loading_label.place(relx=0.5, rely=0.5, anchor="center")

        self.after(1500, lambda: self.tampilkan_hasil_skor(result_frame))

    def tampilkan_hasil_skor(self, frame):
        self.loading_label.destroy()
        data = self.selected_terdakwa
        
        # --- LOGIKA HITUNG SKOR COMPAS (Zip Code Bias) ---
        try: prior_count = int(data['riwayat'].split()[0])
        except: prior_count = 0
        
        skor = 1 + prior_count

        # RAJA PROXY: Kode Pos (Zip Code)
        # ini algoritma key proxy feature dipakenya disini
        if data['zip'] in ["33311", "33313"]:
            skor += 6  # Penalti sangat berat untuk kode pos pemukiman tertentu
        
        if data['umur'] < 25:
            skor += 2

        skor = max(1, min(10, skor))

        # Penentuan Warna
        if skor <= 4: warna_skor, kategori = "#00FF00", "LOW RISK"
        elif skor <= 7: warna_skor, kategori = "#FFFF00", "MEDIUM RISK"
        else: warna_skor, kategori = "#FF0000", "HIGH RISK"

        # Tampilan Data
        data_text = f"NAMA: {data['nama'].upper()}\nID: {data['id']}\nKASUS: {data['kasus']}\nRIWAYAT: {data['riwayat']}\nLOKASI: {data['alamat']}\nZIP: {data['zip']}"
        ctk.CTkLabel(frame, text=data_text, font=ctk.CTkFont(size=16), text_color="#BBBBBB", justify="left").place(relx=0.1, rely=0.5, anchor="w")

        ctk.CTkLabel(frame, text=str(skor), font=ctk.CTkFont(size=120, weight="bold"), text_color=warna_skor).place(relx=0.75, rely=0.5, anchor="center")
        ctk.CTkLabel(frame, text=kategori, font=ctk.CTkFont(size=22, weight="bold"), text_color=warna_skor).place(relx=0.75, rely=0.75, anchor="center")

        # Navigasi
        nav_frame = ctk.CTkFrame(self.main_container, fg_color="transparent")
        nav_frame.pack(side="bottom", pady=20)
        ctk.CTkButton(nav_frame, text="ULANGI SELEKSI", width=180, fg_color="#333333", command=self.show_halaman_tiga).pack(side="left", padx=10)
        ctk.CTkButton(nav_frame, text="MENU UTAMA", width=180, fg_color="#441111", command=self.show_halaman_satu).pack(side="left", padx=10)
        
    def show_halaman_lima(self):
        self.clear_frame()
        
        self.set_background_theme("justice")

        # Judul Halaman
        label_judul = ctk.CTkLabel(
            self.main_container, 
            text="JusticeLens", 
            font=ctk.CTkFont(size=45, weight="bold"),
            text_color="#00FFA3" # Hijau Emerald
        )
        label_judul.pack(pady=(20, 5))

        label_mode = ctk.CTkLabel(
            self.main_container, 
            text="ALGORITMA JUSTICE: EVALUASI BERDASARKAN MERIT", 
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color="#FFFFFF"
        )
        label_mode.pack(pady=(0, 10))

        # DATASET IDENTIK (Sama dengan Halaman 3)
        self.terdakwa_list = [
            {"id": "USR-001", "nama": "Marcus J.", "umur": 24, "gender": "Laki-laki", "alamat": "North Broward", "zip": "33311", "kasus": "Kepemilikan Obat Terlarang", "riwayat": "1 Prior"},
            {"id": "USR-002", "nama": "Darnell T.", "umur": 29, "gender": "Laki-laki", "alamat": "Lauderhill", "zip": "33311", "kasus": "Memasuki wilayah tanpa izin", "riwayat": "0 Prior"},
            {"id": "USR-003", "nama": "Andre L.", "umur": 32, "gender": "Laki-laki", "alamat": "Pompano Beach", "zip": "33313", "kasus": "Pencurian Ringan", "riwayat": "2 Priors"},
            {"id": "USR-004", "nama": "Tyrone W.", "umur": 21, "gender": "Laki-laki", "alamat": "Fort Lauderdale", "zip": "33311", "kasus": "Mengemudi ugal ugalan", "riwayat": "0 Prior"},
            {"id": "USR-005", "nama": "Dylan S.", "umur": 25, "gender": "Laki-laki", "alamat": "Coral Springs", "zip": "33301", "kasus": "Kepemilikan Obat Terlarang", "riwayat": "1 Prior"},
            {"id": "USR-006", "nama": "Branden M.", "umur": 28, "gender": "Laki-laki", "alamat": "Boca Raton", "zip": "33308", "kasus": "Memasuki wilayah tanpa izin", "riwayat": "0 Prior"},
            {"id": "USR-007", "nama": "Scott P.", "umur": 35, "gender": "Laki-laki", "alamat": "Parkland", "zip": "33301", "kasus": "Pencurian Ringan", "riwayat": "3 Priors"},
            {"id": "USR-008", "nama": "Cody R.", "umur": 22, "gender": "Laki-laki", "alamat": "Weston", "zip": "33301", "kasus": "Mengemudi ugal ugalan", "riwayat": "0 Prior"},
        ]

        # Container Scrollable
        scroll_container = ctk.CTkScrollableFrame(
            self.main_container, 
            width=1150, 
            height=450, 
            fg_color="transparent", 
            scrollbar_button_color="#114433"
        )
        scroll_container.pack(pady=10, padx=20)

        grid_frame = ctk.CTkFrame(scroll_container, fg_color="transparent")
        grid_frame.pack()

        for col in range(4):
            grid_frame.grid_columnconfigure(col, weight=1, uniform="kolom_justice")

        self.selected_terdakwa = None
        self.card_frames = []

        def select_card(idx, frame):
            self.selected_terdakwa = self.terdakwa_list[idx]
            for f in self.card_frames:
                f.configure(border_color="#114433", border_width=2)
            frame.configure(border_color="#00FFA3", border_width=4)

        for i, data in enumerate(self.terdakwa_list):
            row, col = i // 4, i % 4
            
            # 2. Samain ukuran Card Halaman 3 (width=260, height=290)
            card = ctk.CTkFrame(
                grid_frame, width=260, height=290, 
                corner_radius=18, border_width=2, 
                border_color="#114433", fg_color="#0A1A14"
            )
            card.grid(row=row, column=col, padx=10, pady=10)
            card.grid_propagate(False)

            # 3. Kasih jarak pinggir (padx=15)
            ctk.CTkLabel(card, text=data['id'], font=ctk.CTkFont(size=10), text_color="#888888").pack(pady=(15, 0), padx=15)
            ctk.CTkLabel(card, text=data['nama'].upper(), font=ctk.CTkFont(size=17, weight="bold"), text_color="#00FFA3").pack(pady=(0, 10), padx=15)

            def add_row(parent, txt, color="#BBBBBB"): 
                # Tambah padx=15 disini
                ctk.CTkLabel(parent, text=txt, font=ctk.CTkFont(size=12), text_color=color).pack(pady=2, padx=15)

            add_row(card, f"{data['umur']} Thn | {data['gender']}")
            add_row(card, f"Kasus: {data['kasus']}")
            add_row(card, f"Riwayat: {data['riwayat']}")
            
            # Footer juga ditambahin padx
            footer = ctk.CTkFrame(card, fg_color="transparent")
            footer.pack(side="bottom", fill="x", pady=(5, 15))
            ctk.CTkLabel(
                footer, 
                text=f"{data['alamat']}\nZip Code: {data['zip']}", 
                font=ctk.CTkFont(size=11), 
                text_color="#666666" 
            ).pack(padx=15)

            # Logic Klik
            idx_now = i
            def on_click(_, idx=idx_now, f=card): select_card(idx, f)
            card.bind("<Button-1>", on_click)
            for child in card.winfo_children():
                child.bind("<Button-1>", on_click)
                if isinstance(child, ctk.CTkFrame):
                    for sub in child.winfo_children():
                        sub.bind("<Button-1>", on_click)

            self.card_frames.append(card)

        # Navigasi Bawah
        nav_frame = ctk.CTkFrame(self.main_container, fg_color="transparent")
        nav_frame.pack(side="bottom", pady=20)

        ctk.CTkButton(
            nav_frame, text="KEMBALI", width=160, height=45, 
            fg_color="#333333", command=self.show_halaman_dua
        ).pack(side="left", padx=10)

        ctk.CTkButton(
            nav_frame, text="PROSES KEADILAN", width=160, height=45, 
            fg_color="#00FFA3", text_color="#121212", 
            font=ctk.CTkFont(weight="bold"), 
            command=self.show_halaman_enam # Lanjut ke Hasil Adil
        ).pack(side="left", padx=10)

    def show_halaman_enam(self):
        if not self.selected_terdakwa: return
        self.clear_frame()
        self.set_background_theme("justice")

        # Judul
        label_judul = ctk.CTkLabel(
            self.main_container, 
            text="JusticeLens", 
            font=ctk.CTkFont(size=40, weight="bold"),
            text_color="#00FFA3"
        )
        label_judul.pack(pady=(20, 10))

        # Container Hasil
        result_frame = ctk.CTkFrame(
            self.main_container, 
            fg_color="#0A1A14", 
            border_width=2, 
            border_color="#00FFA3", 
            width=850, 
            height=480
        )
        result_frame.pack(pady=10)
        result_frame.pack_propagate(False)

        # Animasi Loading yang Tenang
        self.loading_label = ctk.CTkLabel(
            result_frame, 
            text="PERFORMING NEUTRAL ANALYSIS...", 
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color="#00FFA3"
        )
        self.loading_label.place(relx=0.5, rely=0.5, anchor="center")

        # Jeda biar dramatis
        self.after(1500, lambda: self.tampilkan_hasil_justice(result_frame))

    def tampilkan_hasil_justice(self, frame):
        self.loading_label.destroy()
        data = self.selected_terdakwa
        
        # --- LOGIKA HITUNG SKOR JUSTICE (Merit + Severity) ---
        # 1. Skor Dasar dari Riwayat (Priors)
        try:
            prior_count = int(data['riwayat'].split()[0])
        except:
            prior_count = 0
        skor = 1 + prior_count

        # 2. Tambahan Skor berdasarkan Beratnya Kasus (Case Severity)
        # Kita kasih bobot berbeda biar terasa lebih adil
        if "Kepemilikan Obat Terlarang" in data['kasus']:
            skor += 1  # Pelanggaran ringan/menengah
        elif "Pencurian Ringan" in data['kasus']:
            skor += 2  # Pelanggaran terhadap hak milik orang lain
        elif "Mengemudi ugal ugalan" in data['kasus']:
            skor += 1  # Pelanggaran keselamatan
        elif "Memasuki wilayah tanpa izin" in data['kasus']:
            skor += 0  # Pelanggaran sangat ringan

        # 3. Faktor Umur (Tanpa Bias Lokasi)
        if data['umur'] < 21: 
            skor += 1 

        # Tetap abaikan total ZIP CODE dan EKONOMI
        # Karena kita fokus pada 'Merit' (apa yang dia perbuat)
        
        skor = max(1, min(10, skor))

        # Kategori & Alasan (Reasoning)
        if skor <= 3:
            warna_skor, kategori = "#00FF00", "VERY LOW RISK"
            alasan = "Skor rendah diberikan karena riwayat kriminal minimal. Sistem mengabaikan variabel lokasi (Zip Code) untuk menjamin kesetaraan di depan hukum."
        elif skor <= 6:
            warna_skor, kategori = "#00FFA3", "MODERATE RISK"
            alasan = "Skor menengah berdasarkan riwayat pelanggaran sebelumnya. Keputusan murni bersifat teknis hukum tanpa dipengaruhi faktor demografi lingkungan."
        else:
            warna_skor, kategori = "#FFFF00", "OBSERVATION REQUIRED"
            alasan = "Skor mencerminkan riwayat residivisme yang ada. Analisis tetap objektif dengan menutup akses data terhadap latar belakang ekonomi terdakwa."

        # --- TAMPILAN ---
        # Kolom Kiri: Detail Terdakwa
        data_text = (
            f"NAMA: {data['nama'].upper()}\n"
            f"ID: {data['id']}\n"
            f"KASUS: {data['kasus']}\n"
            f"RIWAYAT: {data['riwayat']}\n"
            f"ZIP CODE: {data['zip']} (DATA DIABAIKAN)"
        )
        ctk.CTkLabel(
            frame, text=data_text, font=ctk.CTkFont(size=16), 
            text_color="#BBBBBB", justify="left"
        ).place(relx=0.1, rely=0.4, anchor="w")

        # Kolom Kanan: Skor Besar
        ctk.CTkLabel(frame, text="JUSTICE FAIR SCORE", font=ctk.CTkFont(size=14), text_color="#888888").place(relx=0.75, rely=0.25, anchor="center")
        ctk.CTkLabel(frame, text=str(skor), font=ctk.CTkFont(size=120, weight="bold"), text_color=warna_skor).place(relx=0.75, rely=0.5, anchor="center")
        ctk.CTkLabel(frame, text=kategori, font=ctk.CTkFont(size=22, weight="bold"), text_color=warna_skor).place(relx=0.75, rely=0.75, anchor="center")

        # BOX ALASAN (Reasoning) - Bagian yang lo minta
        reason_frame = ctk.CTkFrame(frame, fg_color="#142D24", corner_radius=10)
        reason_frame.place(relx=0.5, rely=0.9, anchor="center", relwidth=0.9, relheight=0.15)
        
        ctk.CTkLabel(
            reason_frame, 
            text=f"JUSTICE ANALYSIS: {alasan}", 
            font=ctk.CTkFont(size=12, slant="italic"), 
            text_color="#00FFA3",
            wraplength=750
        ).pack(expand=True, padx=20)

        # Navigasi
        nav_frame = ctk.CTkFrame(self.main_container, fg_color="transparent")
        nav_frame.pack(side="bottom", pady=20)

        ctk.CTkButton(nav_frame, text="ULANGI SELEKSI", width=180, height=45, fg_color="#333333", command=self.show_halaman_lima).pack(side="left", padx=10)
        ctk.CTkButton(nav_frame, text="MENU UTAMA", width=180, height=45, fg_color="#114433", command=self.show_halaman_satu).pack(side="left", padx=10)

if __name__ == "__main__":
    app = JusticeLens()
    app.mainloop()