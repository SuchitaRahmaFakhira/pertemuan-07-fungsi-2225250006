# Pertemuan 07 Fungsi Python

Nama: Suchita Rahma Fakhira  
NIM: 2225250006  
Kelas: 3B

## Tujuan

Memahami penggunaan fungsi, parameter, return value, dan scope untuk membuat program Python yang modular, mudah dibaca, serta dapat digunakan kembali.

## Cara Menjalankan

Jalankan program melalui terminal dengan perintah:

    python3 praktik/utilitas_matematika.py

## Struktur Fungsi

- `luas_persegi_panjang(p, l)`: menghitung luas persegi panjang berdasarkan panjang dan lebar, kemudian mengembalikan hasilnya menggunakan return.
- `luas_segitiga(a, t)`: menghitung luas segitiga berdasarkan alas dan tinggi, kemudian mengembalikan hasilnya menggunakan return.
- `jumlah_n(n)`: menghitung jumlah bilangan dari 1 sampai n menggunakan perulangan.
- `faktorial(n)`: menghitung nilai faktorial menggunakan perulangan.
- `tampilkan_menu()`: menampilkan pilihan operasi matematika kepada pengguna.
- `input_n()`: menerima dan memvalidasi input berupa bilangan bulat nonnegatif.

## Hasil Pengujian

| Operasi | Input | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---:|---:|---|
| Luas persegi panjang | p = 8, l = 5 | 40 | 40.0 | Berhasil |
| Luas segitiga | a = 10, t = 6 | 30.0 | 30.0 | Berhasil |
| Jumlah 1 sampai n | n = 10 | 55 | 55 | Berhasil |
| Faktorial | n = 5 | 120 | 120 | Berhasil |
| Faktorial | n = 0 | 1 | 1 | Berhasil |

## Refleksi

Melalui praktik ini, saya memahami bahwa fungsi membuat program lebih terstruktur karena setiap fungsi memiliki tugas yang jelas. Parameter memungkinkan fungsi menerima data yang berbeda, sedangkan return membuat hasil perhitungan dapat digunakan kembali. Saya juga memahami perbedaan variabel lokal dan global serta pentingnya menggunakan variabel sesuai dengan cakupannya.