class Lapangan:
    nama_tempat = "Futsal Arena"
    lokasi = "Samarinda"
    total_lapangan = 0

    def __init__(self, nama, jenis, harga):
        self.nama = nama
        self.jenis = jenis
        self.status = "Tersedia"
        self.__harga = harga
        Lapangan.total_lapangan += 1

    @property
    def harga(self):
        return self.__harga

    @harga.setter
    def harga(self, harga_baru):
        if harga_baru <= 0:
            raise ValueError("Harga lapangan invalid")
        self.__harga = harga_baru

    @classmethod
    def ubah_nama_tempat(cls, nama_baru):
        cls.nama_tempat = nama_baru
        print(f"\nNama Tempat : {cls.nama_tempat}")

    def tampilkan_info(self):
        print(f"\nLapangan\t: {self.nama}")
        print(f"Jenis\t\t: {self.jenis}")
        print(f"Harga\t\t: Rp{self.harga:,}")
        print(f"Status\t\t: {self.status}")

    def pesan(self):
        if self.status == "Tersedia":
            self.status = "Terisi"
            return True
        return False

    @staticmethod
    def validasi_nama(nama):
        return len(nama.strip()) >= 3


class Penyewa:
    nama_sistem = "Sistem Penyewaan Futsal"
    status_member = "Aktif"
    total_penyewa = 0

    def __init__(self, nama, no_hp):
        self.nama = nama
        self.no_hp = no_hp
        self.__saldo = 0
        Penyewa.total_penyewa += 1

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo_baru):
        if saldo_baru < 0:
            raise ValueError("Saldo tidak boleh negatif")
        self.__saldo = saldo_baru

    def tambah_saldo(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah

    def tampilkan_info(self):
        print(f"\nNama\t\t: {self.nama}")
        print(f"No. HP\t\t: {self.no_hp}")
        print(f"Saldo\t\t: Rp{self.saldo:,}")

    @classmethod
    def ubah_status_member(cls, status):
        cls.status_member = status
        print(f"\nStatus Member\t: {cls.status_member}")

    @staticmethod
    def validasi_no_hp(no_hp):
        return no_hp.isdigit() and len(no_hp) >= 10


class Penyewaan:
    nama_sistem = "Sistem Manajemen Penyewaan"
    pajak = 0.10
    total_transaksi = 0

    def __init__(self, penyewa, lapangan, jam):
        self.penyewa = penyewa
        self.lapangan = lapangan
        self.jam = jam
        self.__total = 0
        Penyewaan.total_transaksi += 1

    @property
    def total(self):
        return self.__total

    @total.setter
    def total(self, total_baru):
        if total_baru < 0:
            raise ValueError("Total pembayaran invalid")
        self.__total = total_baru

    def hitung_total(self):
        harga = self.lapangan.harga * self.jam
        self.total = harga + (harga * Penyewaan.pajak)
        return self.total

    def tampilkan_struk(self):
        print(f"\nPenyewa\t\t: {self.penyewa.nama}")
        print(f"Lapangan\t: {self.lapangan.nama}")
        print(f"Lama Sewa\t: {self.jam} jam")
        print(f"Total Bayar\t: Rp{self.total:,.0f}")

    @classmethod
    def ubah_pajak(cls, pajak_baru):
        if pajak_baru >= 0:
            cls.pajak = pajak_baru
            print(f"\nPajak Baru\t: {cls.pajak * 100:.0f}%")

    @staticmethod
    def hitung_diskon(total, persen):
        return total * persen / 100


lapangan1 = Lapangan("Lapangan A", "Vinyl", 100000)
lapangan2 = Lapangan("Lapangan B", "Sintetis", 120000)

naufal = Penyewa("Naufal", "081234567890")
andi = Penyewa("Andi", "082345678901")

Penyewaan.ubah_pajak(0.10)
Lapangan.ubah_nama_tempat("Golden Futsal")

print("\n=== VALIDASI DATA ===")

print(
    f"Nama Lapangan\t: "
    f"{'Valid' if Lapangan.validasi_nama(lapangan1.nama) else 'Invalid'}"
)

print(
    f"No. HP Naufal\t: "
    f"{'Valid' if Penyewa.validasi_no_hp(naufal.no_hp) else 'Invalid'}"
)

print("\n=== DATA LAPANGAN ===")
lapangan1.tampilkan_info()
lapangan2.tampilkan_info()

print("\n=== DATA PENYEWA ===")
naufal.saldo = 500000
andi.saldo = 300000

naufal.tampilkan_info()
andi.tampilkan_info()

print("\n=== TRANSAKSI PENYEWAAN ===")

sewa1 = Penyewaan(naufal, lapangan1, 2)
sewa2 = Penyewaan(andi, lapangan2, 3)

sewa1.hitung_total()
sewa2.hitung_total()

sewa1.tampilkan_struk()
sewa2.tampilkan_struk()

print("\n=== SETTER VALID ===")

print(f"Harga Awal\t: Rp{lapangan1.harga:,}")
lapangan1.harga = 110000
print(f"Harga Baru\t: Rp{lapangan1.harga:,}")

print(f"\nSaldo Awal\t: Rp{naufal.saldo:,}")
naufal.saldo = 600000
print(f"Saldo Baru\t: Rp{naufal.saldo:,}")

print("\n=== SETTER INVALID ===")

try:
    lapangan1.harga = -50000
except ValueError as error:
    print(f"Error Harga\t: {error}")

try:
    naufal.saldo = -100000
except ValueError as error:
    print(f"Error Saldo\t: {error}")

print("\n=== STATIC METHOD ===")

diskon = Penyewaan.hitung_diskon(500000, 10)
print(f"Diskon 10%\t: Rp{diskon:,.0f}")

print("\n=== ATRIBUT KELAS ===")
print(f"Total Lapangan\t: {Lapangan.total_lapangan}")
print(f"Total Penyewa\t: {Penyewa.total_penyewa}")
print(f"Total Transaksi\t: {Penyewaan.total_transaksi}")