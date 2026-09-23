Untuk menguji program ini, jalankan file Python melalui terminal dengan perintah python futsal.py. Pada bagian bawah program akan menghasilkan output berdasarkan pengujian, dengan urutan pengujian:

1. Uji Class Method
Program menggunakan fungsi ubah_nama_tempat() untuk mengubah nama tempat dari "Futsal Arena" menjadi "Golden Futsal". Selain itu, fungsi ubah_pajak() digunakan untuk mengatur pajak penyewaan menjadi 10%. Karena menggunakan @classmethod, perubahan tersebut berlaku pada class secara keseluruhan.

2. Uji Static Method
Program menggunakan validasi_nama() untuk memeriksa apakah nama lapangan valid dan validasi_no_hp() untuk memeriksa nomor HP penyewa. Hasil pengujian ditampilkan dengan status True jika data memenuhi aturan validasi.

3. Uji Instance Method
Dibuat dua objek lapangan, yaitu Lapangan A dan Lapangan B, serta dua objek penyewa yaitu Naufal dan Andi. Kemudian dibuat dua transaksi penyewaan. Fungsi hitung_total() menghitung biaya berdasarkan harga lapangan dan lama sewa, sedangkan tampilkan_struk() menampilkan detail transaksi dan total pembayaran.

4. Uji Encapsulation
Getter digunakan untuk mengambil harga Lapangan A dan saldo Naufal. Kemudian setter digunakan untuk mengubah harga dan saldo menggunakan data yang valid. Setelah itu dilakukan pengujian dengan data negatif untuk membuktikan bahwa validasi setter bekerja. Data yang tidak valid akan ditolak dan menghasilkan ValueError, kemudian error ditangani menggunakan try-except sehingga program tetap berjalan.

5. Uji Atribut Kelas
Program menampilkan jumlah lapangan, jumlah penyewa, dan jumlah transaksi yang telah dibuat. Data tersebut menggunakan atribut kelas sehingga dapat menghitung jumlah objek yang terdaftar dalam sistem.