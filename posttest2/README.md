# Sistem Manajemen Penyewaan Lapangan Futsal

## Deskripsi

Program ini merupakan sistem sederhana untuk mengelola penyewaan lapangan futsal menggunakan bahasa pemrograman Python. Program dibuat dengan menerapkan konsep Object-Oriented Programming (OOP), khususnya class dan object, attribute dan method, encapsulation, serta pengembangan konsep inheritance dan relasi antar-class sesuai kebutuhan Posttest.

Program dapat mengelola data lapangan, data penyewa, transaksi penyewaan, perhitungan total pembayaran, serta fitur khusus untuk Member dan Pelanggan VIP.

## Tujuan

Program ini dibuat untuk menerapkan konsep OOP dalam sebuah sistem penyewaan lapangan futsal serta menerapkan:

* Inheritance
* Superclass dan Subclass
* `super().__init__()`
* Method Overriding
* Protected Attribute
* Private Attribute
* Asosiasi
* Agregasi
* Komposisi

## Struktur Class

Program terdiri dari beberapa class utama:

```text
Penyewa
├── Member
└── PelangganVIP

Lapangan

Penyewaan

Struk
```

### 1. Class Penyewa

`Penyewa` merupakan superclass yang menyimpan data dasar penyewa seperti nama, nomor HP, dan saldo.

Class ini memiliki atribut protected `_nama` dan atribut private `__saldo`.

Method yang terdapat pada class ini antara lain:

* `tampilkan_info()`
* `tambah_saldo()`
* `ubah_status_member()`
* `validasi_no_hp()`

### 2. Class Member

`Member` merupakan subclass dari `Penyewa`.

Class ini menggunakan:

```python
super().__init__(nama, no_hp)
```

untuk memanggil constructor dari superclass.

Member memiliki atribut khusus:

```python
poin
```

Selain itu, method `tampilkan_info()` di-override untuk menampilkan informasi poin member.

### 3. Class PelangganVIP

`PelangganVIP` merupakan subclass dari `Penyewa`.

Class ini menggunakan:

```python
super().__init__(nama, no_hp)
```

dan memiliki atribut khusus:

```python
diskon_vip
```

Method `tampilkan_info()` juga di-override untuk menampilkan informasi diskon VIP.

### 4. Class Lapangan

Class `Lapangan` digunakan untuk menyimpan data lapangan futsal, seperti nama lapangan, jenis lapangan, harga, dan status.

Class ini memiliki fitur:

* Getter dan setter harga
* Method pemesanan lapangan
* Validasi nama lapangan
* Perubahan nama tempat
* Atribut kelas untuk menghitung jumlah lapangan

Harga disimpan sebagai atribut private:

```python
__harga
```

### 5. Class Penyewaan

Class `Penyewaan` digunakan untuk mengelola transaksi penyewaan.

Class ini menerima objek `Penyewa` dan `Lapangan`, kemudian menghitung total pembayaran berdasarkan harga lapangan dan lama sewa.

Class ini memiliki fitur:

* Menghitung total pembayaran
* Menampilkan struk
* Mengatur pajak
* Menghitung diskon
* Menghitung jumlah transaksi

### 6. Class Struk

Class `Struk` digunakan untuk menyimpan dan menampilkan informasi pembayaran dari sebuah transaksi.

Class ini dibuat dari dalam class `Penyewaan` sehingga digunakan untuk menerapkan konsep komposisi.

## Penerapan Inheritance

Inheritance diterapkan dengan menjadikan `Penyewa` sebagai superclass dan `Member` serta `PelangganVIP` sebagai subclass.

```text
              Penyewa
              /     \
             /       \
        Member     PelangganVIP
```

Kedua subclass menggunakan `super().__init__()` untuk memanggil constructor superclass.

Setiap subclass juga mempunyai atribut unik:

* `Member` memiliki `poin`
* `PelangganVIP` memiliki `diskon_vip`

## Penerapan Method Overriding

Method `tampilkan_info()` yang terdapat pada `Penyewa` di-override oleh `Member` dan `PelangganVIP`.

Hal ini membuat setiap jenis penyewa dapat menampilkan informasi tambahan sesuai dengan karakteristiknya.

## Penerapan Protected dan Private

Protected attribute diterapkan pada:

```python
_nama
```

Atribut tersebut dapat digunakan oleh subclass.

Private attribute diterapkan pada:

```python
__saldo
__harga
__total
__struk
```

Atribut private digunakan untuk membatasi akses langsung terhadap data tertentu.

## Penerapan Relasi UML

### 1. Asosiasi

Asosiasi terjadi antara `Penyewa` dan `Penyewaan`.

`Penyewaan` menerima objek `Penyewa` sebagai bagian dari transaksi.

```python
sewa1 = Penyewaan(naufal, lapangan1, 2)
```

Hubungan:

```text
Penyewa ───────── Penyewaan
       Asosiasi
```

### 2. Agregasi

Agregasi terjadi antara `Penyewaan` dan `Lapangan`.

Objek `Lapangan` dibuat terlebih dahulu di luar `Penyewaan`, kemudian diberikan sebagai parameter ke `Penyewaan`.

```python
lapangan1 = Lapangan("Lapangan A", "Vinyl", 100000)

sewa1 = Penyewaan(naufal, lapangan1, 2)
```

Hubungan:

```text
Penyewaan ◇──────── Lapangan
          Agregasi
```

### 3. Komposisi

Komposisi terjadi antara `Penyewaan` dan `Struk`.

Objek `Struk` dibuat langsung di dalam method `tampilkan_struk()` pada class `Penyewaan`.

```python
self.__struk = Struk(
    self.penyewa,
    self.lapangan,
    self.jam,
    self.total
)
```

Hubungan:

```text
Penyewaan ◆──────── Struk
           Komposisi
```

## Fitur Program

Program memiliki beberapa fitur utama:

1. Menampilkan data lapangan.
2. Menampilkan data penyewa.
3. Membedakan Member dan Pelanggan VIP.
4. Mengelola saldo penyewa.
5. Mengubah harga lapangan.
6. Memesan lapangan.
7. Menghitung total biaya penyewaan.
8. Menghitung pajak.
9. Menghitung diskon.
10. Memberikan poin kepada Member.
11. Memberikan diskon khusus kepada Pelanggan VIP.
12. Menampilkan struk pembayaran.
13. Melakukan validasi data.
14. Menggunakan encapsulation melalui atribut protected dan private.

## Contoh Penggunaan

Program membuat dua lapangan:

```python
lapangan1 = Lapangan("Lapangan A", "Vinyl", 100000)
lapangan2 = Lapangan("Lapangan B", "Sintetis", 120000)
```

Kemudian membuat dua jenis penyewa:

```python
naufal = Member("Naufal", "081234567890", 150)
andi = PelangganVIP("Andi", "082345678901", 20)
```

Selanjutnya dibuat transaksi penyewaan:

```python
sewa1 = Penyewaan(naufal, lapangan1, 2)
sewa2 = Penyewaan(andi, lapangan2, 3)
```

Total pembayaran kemudian dihitung menggunakan:

```python
sewa1.hitung_total()
sewa2.hitung_total()
```

dan struk ditampilkan menggunakan:

```python
sewa1.tampilkan_struk()
sewa2.tampilkan_struk()
```

## Kesimpulan

Program Sistem Manajemen Penyewaan Lapangan Futsal menerapkan konsep Object-Oriented Programming menggunakan Python. Pada versi Posttest ini, program dikembangkan dengan menerapkan inheritance melalui superclass `Penyewa` dan dua subclass yaitu `Member` dan `PelangganVIP`. Selain itu, program juga menerapkan method overriding, `super().__init__()`, protected attribute, private attribute, serta tiga jenis relasi UML yaitu asosiasi, agregasi, dan komposisi.
