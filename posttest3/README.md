
# Sistem Manajemen Penyewaan Lapangan Futsal

## Deskripsi

Program ini merupakan aplikasi sederhana berbasis Python untuk mengelola penyewaan lapangan futsal. Program menerapkan konsep Object-Oriented Programming (OOP), meliputi class dan object, encapsulation, inheritance, abstraction, polymorphism, class method, static method, property, exception handling, serta operator overloading.

Fitur yang tersedia meliputi pengelolaan data lapangan, data penyewa, layanan penyewaan reguler dan VIP, perhitungan biaya, pembayaran, struk transaksi, validasi data, dan notifikasi transaksi.

## Struktur Class

- **Lapangan:** Mengelola informasi lapangan, harga, status ketersediaan, dan pemesanan.
- **Penyewa:** Menyimpan informasi penyewa, nomor HP, dan saldo.
- **Member:** Subclass `Penyewa` yang memiliki fitur poin member.
- **PelangganVIP:** Subclass `Penyewa` yang memiliki fitur diskon VIP.
- **LayananPenyewaan:** Abstract class yang menjadi dasar layanan penyewaan.
- **LayananReguler:** Subclass layanan dengan perhitungan biaya reguler.
- **LayananVIP:** Subclass layanan dengan perhitungan biaya VIP.
- **Penyewaan:** Mengelola transaksi penyewaan dan total pembayaran.
- **Struk:** Menampilkan informasi transaksi dalam format struk pembayaran.
- **NotifikasiPenyewa:** Mengirimkan notifikasi kepada penyewa.
- **LaporanTransaksi:** Menampilkan laporan transaksi melalui method yang sama dengan notifikasi.

## Class Diagram



### Relasi UML

**1. Association (Asosiasi)**

Class `Penyewaan` berhubungan dengan class `Penyewa` karena setiap transaksi menyimpan referensi ke objek penyewa yang melakukan pemesanan. Hubungan ini memungkinkan transaksi mengakses informasi penyewa.

**2. Aggregation (Agregasi)**

Class `Penyewaan` menggunakan objek `Lapangan` yang dibuat secara terpisah. Objek lapangan dapat tetap ada dan digunakan meskipun suatu transaksi penyewaan tidak lagi digunakan.

**3. Composition (Komposisi)**

Class `Penyewaan` membuat dan menyimpan objek `Struk` ketika method `tampilkan_struk()` dipanggil. Struk tersebut dibuat sebagai bagian dari proses transaksi penyewaan.

## Abstraction (Abstraksi)

Program menggunakan abstract class `LayananPenyewaan` yang mewarisi `ABC` dari modul `abc`. Class tersebut memiliki dua abstract method, yaitu `hitung_biaya()` dan `proses_pembayaran()`, serta method konkret `jalankan()`.

Class `LayananReguler` dan `LayananVIP` mengimplementasikan kedua abstract method tersebut dengan perilaku yang berbeda. Program juga mencoba membuat objek langsung dari `LayananPenyewaan` untuk membuktikan bahwa abstract class tidak dapat diinstansiasi dan menghasilkan `TypeError`.

## Polymorphism (Polimorfisme)

### 1. Polimorfisme via Pewarisan

Class `LayananReguler` dan `LayananVIP` meng-override method `hitung_biaya()` dan `proses_pembayaran()`. Kedua objek dipanggil melalui satu loop sehingga masing-masing objek menjalankan perilakunya sendiri tanpa memeriksa tipe objek menggunakan `type()`.

### 2. Duck Typing

Class `NotifikasiPenyewa` dan `LaporanTransaksi` tidak memiliki hubungan pewarisan satu sama lain, tetapi keduanya mempunyai method `kirim()`.

Kedua objek dipanggil melalui fungsi `kirim_pesan()` yang sama. Hal ini menunjukkan bahwa fungsi dapat menggunakan objek berdasarkan method yang tersedia tanpa harus mengetahui kelas objek tersebut.

### 3. Operator Overloading

Class `Struk` mengimplementasikan magic method `__str__()` untuk menentukan representasi teks objek struk. Dengan demikian, objek `Struk` dapat ditampilkan menggunakan `print()` dengan format informasi transaksi yang mudah dibaca.

### 4. Larangan Anti-Pattern

Program tidak menggunakan rantai `if/elif` yang memeriksa `type()` atau string jenis objek untuk menentukan perilaku polimorfisme. Setiap objek menjalankan perilakunya sendiri melalui method yang diimplementasikan pada class masing-masing.

## Encapsulation (Enkapsulasi)

Enkapsulasi diterapkan menggunakan atribut private dan protected. Contohnya, atribut `__harga` pada class `Lapangan`, `__saldo` pada class `Penyewa`, dan `__total` pada class `Penyewaan` tidak diakses secara langsung dari luar class.

Pengaksesan dan perubahan nilai dilakukan melalui property dan setter yang dilengkapi validasi. Jika harga atau saldo diberikan nilai yang tidak valid, program menghasilkan `ValueError`.

## Inheritance (Pewarisan)

Pewarisan diterapkan pada class `Member` dan `PelangganVIP` yang mewarisi class `Penyewa`. Keduanya menggunakan `super().__init__()` untuk memanggil constructor superclass dan memiliki atribut serta perilaku tambahan.

Kedua subclass juga meng-override method `tampilkan_info()` untuk menampilkan informasi sesuai jenis penyewa.

## Dependency Injection

Class `Penyewaan` menerima objek layanan melalui constructor. Dengan demikian, layanan reguler maupun VIP dapat diberikan sebagai dependency tanpa membuat objek layanan secara langsung di dalam class `Penyewaan`.

Pendekatan ini memudahkan penggantian layanan dan membantu mengurangi ketergantungan langsung antara transaksi dan implementasi layanan tertentu.

## Cara Menjalankan Program

Pastikan Python telah terinstal pada komputer. Simpan program utama sebagai `main.py`, kemudian jalankan perintah berikut pada terminal di folder proyek:

```bash
python main.py
```

## Bukti Output Program

Sertakan screenshot hasil eksekusi program pada laporan atau repository, meliputi:

1. Bukti `TypeError` saat abstract class diinstansiasi.
2. Hasil perhitungan layanan reguler dan VIP.
3. Tampilan struk pembayaran.
4. Hasil penerapan duck typing.
5. Pengujian validasi harga dan saldo.
6. Pengujian fitur member dan VIP.
7. Informasi jumlah lapangan, penyewa, dan transaksi.

## Teknologi

- Python 3
- Object-Oriented Programming (OOP)
- Modul `abc` untuk abstract class

## Kesimpulan

Program ini menerapkan konsep OOP melalui enkapsulasi, pewarisan, abstraksi, dan polimorfisme. Penerapan association, aggregation, composition, duck typing, dan operator overloading digunakan untuk menunjukkan hubungan antarclass dan perilaku objek dalam sistem penyewaan lapangan futsal.
