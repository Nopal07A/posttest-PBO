class Lapangan:
    nama_tempat = "Futsal Arena"
    jumlah_lapangan = 0
    jenis_lapangan = "Indoor"

    def __init__(self, nama, harga_per_jam):
        self.nama = nama
        self.__harga_per_jam = harga_per_jam
        Lapangan.jumlah_lapangan += 1

    @property
    def harga_per_jam(self):
        return self.__harga_per_jam

    @harga_per_jam.setter
    def harga_per_jam(self, harga):
        if harga <= 0:
            raise ValueError("Harga sewa harus lebih dari 0.")
        self.__harga_per_jam = harga

    def tampilkan_info(self):
        print(f"Nama Lapangan : {self.nama}")
        print(f"Harga/Jam     : Rp{self.harga_per_jam:,}")
        print(f"Jenis         : {Lapangan.jenis_lapangan}")

    @classmethod
    def ubah_jenis_lapangan(cls, jenis_baru):
        if jenis_baru.strip() == "":
            print("Jenis lapangan tidak boleh kosong.")
        else:
            cls.jenis_lapangan = jenis_baru

    @staticmethod
    def validasi_nama(nama):
        return len(nama.strip()) >= 3


class Penyewa:
    nama_instansi = "Futsal Arena"
    jumlah_penyewa = 0
    status_member = "Aktif"

    def __init__(self, nama, nomor_hp):
        self.nama = nama
        self.nomor_hp = nomor_hp
        self.__saldo = 0
        Penyewa.jumlah_penyewa += 1

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, jumlah):
        if jumlah < 0:
            raise ValueError("Saldo tidak boleh negatif.")
        self.__saldo = jumlah

    def tambah_saldo(self, jumlah):
        if jumlah <= 0:
            print("Jumlah saldo harus lebih dari 0.")
        else:
            self.__saldo += jumlah
            print(f"Saldo {self.nama} berhasil ditambah.")

    def tampilkan_info(self):
        print(f"Nama Penyewa : {self.nama}")
        print(f"Nomor HP     : {self.nomor_hp}")
        print(f"Saldo        : Rp{self.saldo:,}")

    @classmethod
    def ubah_status_member(cls, status):
        cls.status_member = status

    @staticmethod
    def validasi_nomor_hp(nomor):
        return nomor.isdigit() and len(nomor) >= 10


class Penyewaan:
    nama_sistem = "Sistem Penyewaan Futsal"
    total_transaksi = 0
    pajak = 0.10

    def __init__(self, penyewa, lapangan, jam_sewa):
        self.penyewa = penyewa
        self.lapangan = lapangan
        self.jam_sewa = jam_sewa
        self.__total_bayar = 0
        Penyewaan.total_transaksi += 1

    @property
    def total_bayar(self):
        return self.__total_bayar

    @total_bayar.setter
    def total_bayar(self, jumlah):
        if jumlah < 0:
            raise ValueError("Total pembayaran tidak boleh negatif.")
        self.__total_bayar = jumlah

    def hitung_total(self):
        harga = self.lapangan.harga_per_jam * self.jam_sewa
        pajak = harga * Penyewaan.pajak
        self.total_bayar = harga + pajak
        return self.total_bayar

    def tampilkan_struk(self):
        print("\n===== STRUK PENYEWAAN =====")
        print(f"Penyewa       : {self.penyewa.nama}")
        print(f"Lapangan      : {self.lapangan.nama}")
        print(f"Lama Sewa     : {self.jam_sewa} jam")
        print(f"Harga/Jam     : Rp{self.lapangan.harga_per_jam:,}")
        print(f"Total Bayar   : Rp{self.total_bayar:,}")
        print("============================")

    @classmethod
    def ubah_pajak(cls, pajak_baru):
        if pajak_baru < 0:
            print("Pajak tidak boleh negatif.")
        else:
            cls.pajak = pajak_baru

    @staticmethod
    def hitung_diskon(total, persen):
        if total < 0 or persen < 0:
            return 0
        return total * persen / 100


print("==========================================")
print(" SISTEM MANAJEMEN PENYEWAAN LAPANGAN FUTSAL")
print("==========================================")

lapangan1 = Lapangan("Lapangan A", 100000)
lapangan2 = Lapangan("Lapangan B", 120000)

print("\n--- DATA LAPANGAN ---")
lapangan1.tampilkan_info()
print()
lapangan2.tampilkan_info()

penyewa1 = Penyewa("Muhammad", "081234567890")
penyewa2 = Penyewa("Andi", "082345678901")

penyewa1.saldo = 500000
penyewa2.saldo = 300000

print("\n--- DATA PENYEWA ---")
penyewa1.tampilkan_info()
print()
penyewa2.tampilkan_info()

sewa1 = Penyewaan(penyewa1, lapangan1, 2)
sewa2 = Penyewaan(penyewa2, lapangan2, 3)

print("\n--- PERHITUNGAN PENYEWAAN ---")

sewa1.hitung_total()
sewa2.hitung_total()

sewa1.tampilkan_struk()
sewa2.tampilkan_struk()

print("\n--- INSTANCE METHOD ---")

penyewa1.tambah_saldo(100000)
print(f"Saldo baru {penyewa1.nama}: Rp{penyewa1.saldo:,}")

print("\n--- CLASS METHOD ---")

Lapangan.ubah_jenis_lapangan("Vinyl Indoor")
print(f"Jenis lapangan: {Lapangan.jenis_lapangan}")

Penyewa.ubah_status_member("Aktif Premium")
print(f"Status member: {Penyewa.status_member}")

Penyewaan.ubah_pajak(0.05)
print(f"Pajak baru: {Penyewaan.pajak * 100}%")

print("\n--- STATIC METHOD ---")

print(
    "Validasi nama lapangan:",
    Lapangan.validasi_nama("Lapangan C")
)

print(
    "Validasi nomor HP:",
    Penyewa.validasi_nomor_hp("081234567890")
)

diskon = Penyewaan.hitung_diskon(500000, 10)
print(f"Diskon 10% dari Rp500.000: Rp{diskon:,.0f}")

print("\n--- SETTER VALID ---")

lapangan1.harga_per_jam = 110000
print(f"Harga baru lapangan 1: Rp{lapangan1.harga_per_jam:,}")

penyewa1.saldo = 750000
print(f"Saldo baru penyewa 1: Rp{penyewa1.saldo:,}")

sewa1.total_bayar = 250000
print(f"Total bayar baru: Rp{sewa1.total_bayar:,}")

print("\n--- SETTER TIDAK VALID ---")

try:
    lapangan1.harga_per_jam = -50000
except ValueError as e:
    print("Error:", e)

try:
    penyewa1.saldo = -100000
except ValueError as e:
    print("Error:", e)

try:
    sewa1.total_bayar = -200000
except ValueError as e:
    print("Error:", e)

print("\n--- ATRIBUT KELAS ---")

print(f"Nama Tempat       : {Lapangan.nama_tempat}")
print(f"Jumlah Lapangan   : {Lapangan.jumlah_lapangan}")
print(f"Jumlah Penyewa    : {Penyewa.jumlah_penyewa}")
print(f"Total Transaksi   : {Penyewaan.total_transaksi}")