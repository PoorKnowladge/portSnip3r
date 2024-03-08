Scan Ports Vulnerability

Deskripsi:

Scan Ports Vulnerability adalah sebuah program Python yang dirancang untuk melakukan pemindaian port pada host tertentu untuk mengidentifikasi port yang terbuka dan potensial rentan terhadap serangan. Program ini menggunakan teknik socket programming dan threading untuk meningkatkan efisiensi dan kecepatan pemindaian port.

Fitur Utama:

1. Pemindaian Port: Program memungkinkan pengguna untuk memindai rentang port yang ditentukan pada host yang ditentukan.
2. Threaded Execution: Pemindaian port dilakukan menggunakan threading untuk meningkatkan efisiensi dan kecepatan pemindaian.
3. Penanganan Kesalahan: Program dilengkapi dengan penanganan kesalahan yang baik untuk mengatasi kondisi yang mungkin terjadi saat melakukan pemindaian port. 
4. Laporan Hasil: Setelah pemindaian selesai, program membuat laporan hasil yang mencakup informasi tentang host yang dipindai, dan daftar port yang terbuka.

Cara Penggunaan:

Pengguna diminta untuk memasukkan target yang ingin dipindai dan rentang port yang ingin diperiksa. Program akan melakukan pemindaian port menggunakan teknik threading. Setelah selesai, program akan menyimpan laporan hasil pemindaian dalam file teks.

Cara Menjalankan:
```html
git clone https://github.com/PoorKnowladge/portSnip3r.git
```

```html
cd porSnip3r
python3 scan_ports.py
```
7. Ikuti petunjuk yang muncul untuk memasukkan target, rentang port, dan nama file laporan.
8. Untuk alokasi waktu di sarankan 0.1, dan 1.0 kalau lebih akan terjadi error to many open files

Dengan menggunakan Scan Ports Vulnerability, pengguna dapat dengan mudah melakukan pemindaian port untuk mengidentifikasi potensi kerentanan keamanan dalam jaringan mereka dan meningkatkan tingkat keamanan sistem mereka.
