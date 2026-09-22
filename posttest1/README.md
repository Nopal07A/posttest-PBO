1. Class Lapangan
- Menyimpan data lapangan futsal.
- Memiliki atribut nama dan harga sewa per jam.
- Menggunakan atribut private __harga_per_jam.
- Memiliki getter dan setter untuk mengatur harga.
- Memiliki instance method untuk menampilkan informasi lapangan.
- Memiliki class method untuk mengubah jenis lapangan.
- Memiliki static method untuk validasi nama lapangan.

2. Class Penyewa
- Menyimpan data pelanggan yang menyewa lapangan.
- Memiliki atribut nama, nomor HP, dan saldo.
- Menggunakan atribut private __saldo.
- Memiliki getter dan setter untuk mengatur saldo dengan validasi.
- Memiliki instance method untuk menambah saldo dan menampilkan data penyewa.
- Memiliki class method untuk mengubah status member.
- Memiliki static method untuk memvalidasi nomor HP.

3. Class Penyewaan
- Menghubungkan objek Penyewa dengan objek Lapangan.
- Menyimpan data lama waktu penyewaan dan total pembayaran.
- Menggunakan atribut private __total_bayar.
- Memiliki getter dan setter untuk total pembayaran.
- Memiliki instance method untuk menghitung total biaya dan menampilkan struk.
- Memiliki class method untuk mengubah persentase pajak.
- Memiliki static method untuk menghitung diskon.