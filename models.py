class Pasien:
    def __init__(self, id_pasien, nama, keluhan, gol_darah, status="Menunggu"):
        self.id = id_pasien
        self.nama = nama
        self.keluhan = keluhan
        self.gol_darah = gol_darah
        self.status = status

    def to_list(self):
        return [self.id, self.nama, self.keluhan, self.gol_darah, self.status]

    def __str__(self):
        return f"[{self.id}] {self.nama} - Keluhan: {self.keluhan} (Gol. Darah: {self.gol_darah}) - {self.status}"


class Dokter:
    def __init__(self, id_dokter, nama_dokter, spesialisasi):
        self.id_dokter = id_dokter
        self.nama_dokter = nama_dokter
        self.spesialisasi = spesialisasi

    def to_list(self):
        return [self.id_dokter, self.nama_dokter, self.spesialisasi]

    def __str__(self):
        return f"Dr. {self.nama_dokter} ({self.id_dokter}) - Spesialis: {self.spesialisasi}"