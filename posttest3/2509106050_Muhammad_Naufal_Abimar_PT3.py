
from abc import ABC, abstractmethod


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
        print(f"\nNama Tempat: {cls.nama_tempat}")

    def tampilkan_info(self):
        print(f"\nLapangan\t: {self.nama}")
        print(f"Jenis\t\t: {self.jenis}")
        print(f"Harga\t\t: Rp{self.harga:,.0f}")
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
        self._nama = nama
        self.no_hp = no_hp
        self.__saldo = 0
        Penyewa.total_penyewa += 1

    @property
    def nama(self):
        return self._nama

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
        print(f"\nNama\t\t: {self._nama}")
        print(f"No. HP\t\t: {self.no_hp}")
        print(f"Saldo\t\t: Rp{self.saldo:,.0f}")

    @classmethod
    def ubah_status_member(cls, status):
        cls.status_member = status
        print(f"\nStatus Member\t: {cls.status_member}")

    @staticmethod
    def validasi_no_hp(no_hp):
        return no_hp.isdigit() and len(no_hp) >= 10


class Member(Penyewa):
    def __init__(self, nama, no_hp, poin):
        super().__init__(nama, no_hp)
        self.poin = poin

    def tambah_poin(self, jumlah):
        if jumlah > 0:
            self.poin += jumlah

    def tampilkan_info(self):
        print(f"\nNama\t\t: {self._nama}")
        print(f"No. HP\t\t: {self.no_hp}")
        print(f"Saldo\t\t: Rp{self.saldo:,.0f}")
        print(f"Poin Member\t: {self.poin}")


class PelangganVIP(Penyewa):
    def __init__(self, nama, no_hp, diskon_vip):
        super().__init__(nama, no_hp)
        self.diskon_vip = diskon_vip

    def hitung_diskon_vip(self, total):
        return total * self.diskon_vip / 100

    def tampilkan_info(self):
        print(f"\nNama\t\t: {self._nama}")
        print(f"No. HP\t\t: {self.no_hp}")
        print(f"Saldo\t\t: Rp{self.saldo:,.0f}")
        print(f"Diskon VIP\t: {self.diskon_vip}%")


class LayananPenyewaan(ABC):
    pajak = 0.10

    def __init__(self, nama_layanan):
        self._nama_layanan = nama_layanan

    @abstractmethod
    def hitung_biaya(self, penyewaan):
        pass

    @abstractmethod
    def proses_pembayaran(self, total):
        pass

    def jalankan(self, penyewaan):
        total = self.hitung_biaya(penyewaan)
        penyewaan.total = total

        print(f"\nLayanan\t\t: {self._nama_layanan}")
        print(f"Total Bayar\t: Rp{total:,.0f}")
        print(f"Pembayaran\t: {self.proses_pembayaran(total)}")

        return total


class LayananReguler(LayananPenyewaan):
    def __init__(self, biaya_admin):
        super().__init__("Layanan Reguler")
        self.biaya_admin = biaya_admin

    def hitung_biaya(self, penyewaan):
        harga = penyewaan.lapangan.harga * penyewaan.jam
        pajak = harga * self.pajak
        return harga + pajak + self.biaya_admin

    def proses_pembayaran(self, total):
        return "Pembayaran reguler berhasil diproses"


class LayananVIP(LayananPenyewaan):
    def __init__(self, diskon_layanan):
        super().__init__("Layanan VIP")
        self.diskon_layanan = diskon_layanan

    def hitung_biaya(self, penyewaan):
        harga = penyewaan.lapangan.harga * penyewaan.jam
        harga_pajak = harga + (harga * self.pajak)
        diskon = harga_pajak * self.diskon_layanan / 100
        return harga_pajak - diskon

    def proses_pembayaran(self, total):
        return "Pembayaran VIP berhasil diproses"


class Struk:
    def __init__(self, penyewa, lapangan, jam, total):
        self.penyewa = penyewa
        self.lapangan = lapangan
        self.jam = jam
        self.total = total

    def __str__(self):
        return (
            "\n=== STRUK PEMBAYARAN ===\n"
            f"Penyewa\t\t: {self.penyewa.nama}\n"
            f"Lapangan\t: {self.lapangan.nama}\n"
            f"Lama Sewa\t: {self.jam} jam\n"
            f"Total Bayar\t: Rp{self.total:,.0f}"
        )


class Penyewaan:
    nama_sistem = "Sistem Manajemen Penyewaan"
    total_transaksi = 0

    def __init__(self, penyewa, lapangan, jam, layanan):
        self.penyewa = penyewa
        self.lapangan = lapangan
        self.jam = jam
        self.layanan = layanan
        self.__total = 0
        self.__struk = None
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
        return self.layanan.jalankan(self)

    def tampilkan_struk(self):
        self.__struk = Struk(
            self.penyewa,
            self.lapangan,
            self.jam,
            self.total
        )
        print(self.__struk)

    @classmethod
    def ubah_pajak(cls, pajak_baru):
        if pajak_baru >= 0:
            LayananPenyewaan.pajak = pajak_baru
            print(f"\nPajak Baru\t: {pajak_baru * 100:.0f}%")

    @staticmethod
    def hitung_diskon(total, persen):
        return total * persen / 100


class NotifikasiPenyewa:
    def kirim(self, pesan):
        print(f"Notifikasi kepada penyewa: {pesan}")


class LaporanTransaksi:
    def kirim(self, pesan):
        print(f"Laporan transaksi: {pesan}")


def kirim_pesan(penerima, pesan):
    penerima.kirim(pesan)


print("=== BUKTI ABSTRAKSI ===")

try:
    layanan_abstrak = LayananPenyewaan("Layanan Umum")
except TypeError as error:
    print("Abstract class tidak dapat dibuat menjadi objek.")
    print(f"Pesan Python: {error}")


print("\n=== PENGATURAN SISTEM ===")

Lapangan.ubah_nama_tempat("Golden Futsal")
Penyewaan.ubah_pajak(0.10)

lapangan1 = Lapangan("Lapangan A", "Vinyl", 100000)
lapangan2 = Lapangan("Lapangan B", "Sintetis", 120000)

naufal = Member("Naufal", "081234567890", 150)
andi = PelangganVIP("Andi", "082345678901", 20)

naufal.saldo = 500000
andi.saldo = 300000

print("\n=== DATA LAPANGAN ===")
lapangan1.tampilkan_info()
lapangan2.tampilkan_info()

print("\n=== DATA PENYEWA ===")
naufal.tampilkan_info()
andi.tampilkan_info()

print("\n=== VALIDASI DATA ===")
print(
    "Nama Lapangan:",
    "Valid" if Lapangan.validasi_nama(lapangan1.nama)
    else "Invalid"
)
print(
    "No. HP Naufal:",
    "Valid" if Penyewa.validasi_no_hp(naufal.no_hp)
    else "Invalid"
)

layanan_reguler = LayananReguler(biaya_admin=5000)
layanan_vip = LayananVIP(diskon_layanan=15)

sewa1 = Penyewaan(naufal, lapangan1, 2, layanan_reguler)
sewa2 = Penyewaan(andi, lapangan2, 3, layanan_vip)

print("\n=== POLIMORFISME VIA PEWARISAN ===")

for layanan, transaksi in [
    (layanan_reguler, sewa1),
    (layanan_vip, sewa2)
]:
    layanan.jalankan(transaksi)

print("\n=== STRUK PEMBAYARAN ===")
sewa1.tampilkan_struk()
sewa2.tampilkan_struk()

print("\n=== FITUR MEMBER ===")
naufal.tambah_poin(50)
print(f"Poin Naufal setelah ditambah: {naufal.poin}")

print("\n=== FITUR VIP ===")
print(
    f"Diskon VIP Andi: "
    f"Rp{andi.hitung_diskon_vip(sewa2.total):,.0f}"
)

print("\n=== PEMESANAN LAPANGAN ===")
if lapangan1.pesan():
    print("Lapangan A berhasil dipesan")
else:
    print("Lapangan A tidak tersedia")

print("\n=== SETTER VALID ===")
print(f"Harga awal: Rp{lapangan1.harga:,.0f}")
lapangan1.harga = 110000
print(f"Harga baru: Rp{lapangan1.harga:,.0f}")

print(f"Saldo awal Naufal: Rp{naufal.saldo:,.0f}")
naufal.saldo = 600000
print(f"Saldo baru Naufal: Rp{naufal.saldo:,.0f}")

print("\n=== SETTER INVALID ===")
try:
    lapangan1.harga = -50000
except ValueError as error:
    print(f"Error harga: {error}")

try:
    naufal.saldo = -100000
except ValueError as error:
    print(f"Error saldo: {error}")

print("\n=== DUCK TYPING ===")
notifikasi = NotifikasiPenyewa()
laporan = LaporanTransaksi()

for penerima in [notifikasi, laporan]:
    kirim_pesan(penerima, "Transaksi penyewaan selesai")

print("\n=== STATIC METHOD ===")
diskon = Penyewaan.hitung_diskon(500000, 10)
print(f"Diskon 10%: Rp{diskon:,.0f}")

print("\n=== ATRIBUT KELAS ===")
print(f"Total Lapangan: {Lapangan.total_lapangan}")
print(f"Total Penyewa: {Penyewa.total_penyewa}")
print(f"Total Transaksi: {Penyewaan.total_transaksi}")
