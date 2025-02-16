# **Manajemen Data Pasien Rumah Sakit**
## **A. Pendahuluan**
Program ini merupakan program sederhana berbasis CRUD (Create, Read, Update, dan Delete) yang dirancang untuk memanajemen data pasien Hankuk National University Hospital. Program ini memungkinkan admin rumah sakit untuk dapat melihat data pasien, menginput data pasien baru, menginput data pasien lama, serta menghapus data pasien. Program dibuat dengan menggunakan bahasa pemrograman Python dengan melibatkan library tabulate, module datetime, module platform, dan module os. 
## **B. Fitur**
Program manajemen data pasien Hankuk National University Hospital memiliki beberapa fitur dalam menu utama antara lain:
1. Daftar Pasien : `daftarPasien()` --> Untuk melihat data pasien rumah sakit
2. Registrasi Pasien Baru : `registrasiPasienBaru()` --> Untuk membuat data pasien baru yang belum terdaftar
3. Registrasi Pasien Lama : `registrasiPasienLama()` --> Untuk membuat data/update data pasien lama yang telah terdaftar sebelumnya
4. Menghapus Data Pasien : `hapusPasien()` --> Untuk menghapus data pasien bila diperlukan.
## **C. CRUD Function**
**1. Read (Daftar Pasien)**

- Dibuat dengan menggunakan regular function `daftarPasien()`
- Memiliki sub menu melihat seluruh data pasien, sub menu melihat data pasien berdasarkan ID pasien, dan sub menu kembali ke menu utama.
- Data pasien yang disajikan ditabulasi dengan menggunakan library tabulate.
- Data pasien yang disajikan meliputi **ID Pasien**, **Nama** Pasien, **Usia** Pasien, **Gender** Pasien, **Poli** Tujuan, **Tanggal** Kunjungan, dan **Cara Pembayaran**

**2. Create (Registrasi Pasien Baru)**

- Dibuat dengan menggunakan regular function `registrasiPasienBaru()`
- Function ini memerlukan beberapa **input** data pasien seperti **nama**, **usia**, **gender**, **poli tujuan**, dan **cara pembayaran**.
- Pasien yang berhasil terdaftar akan mendapatkan tampilan tabulasi datanya yang telah tertambahkan ke dalam data pasien keseluruhan serta mendapatkan notifikasi apabila data berhasil tersimpan. 
- Tampilan data pasien baru yang telah tertabulasi akan otomatis memiliki ID lanjutan dari pasien terakhir serta memiliki tanggal kunjungan yang otomatis tertulis sesuai tanggal kunjungan pasien di hari tersebut.

**3. Update (Registrasi Pasien Lama)**

- Dibuat dengan menggunakan regular function `registrasiPasienLama()`
- Function ini memerlukan **input** data pasien antara lain **poli tujuan** dan **cara pembayaran**.
- Pasien yang berhasil terdaftar ulang akan mendapatkan tampilan tabulasi datanya yang telah ter-update dalam data pasien keseluruhan serta mendapatkan notifikasi apabila data berhasil tersimpan. 
- Tampilan data pasien yang telah ter-update ditabulasi dan otomatis memiliki tanggal kunjungan sesuai tanggal kunjungan pasien di hari tersebut.

**4. Delete (Hapus Pasien)**

- Dibuat dengan menggunakan regular function `hapusPasien()`
- Memiliki sub menu menghapus data pasien berdasarkan ID pasien, sub menu menghapus data seluruh pasien dan sub menu kembali ke menu utama.
- Untukdapat mengakses sub menu Hapus Seluruh Data Pasien, memerlukan password sehingga tidak setiap orang dapat melakukan penghapusan seluruh data yang ada.

## **D. Data Structure**
- `data_pasien` --> List 2D
- `header_pasien` --> List 1D
- `jadwal_dokter` --> List 2 D
- `header_dokter` --> List 1D
- `input_ID_pasien` --> int
- `nama` --> str
- `usia` --> str
- `gender` --> str
- `poli` --> str
- `pembayaran` --> str
- `password` --> str

## **E. Flow Chart Program**
### 1. Menu Utama
![menu_utama](https://github.com/user-attachments/assets/3436bc0c-6e35-4f67-81f8-8ccb1966a0b1)

### 2. Menu Melihat Data Pasien (Read)
![menu_1](https://github.com/user-attachments/assets/dd26acc5-45be-442d-b923-e5bf638e8793)

### 3. Menu Registrasi Pasien Baru (Create)
![menu_2](https://github.com/user-attachments/assets/70c0791b-8d60-4081-ad91-2e309b61e3cf)

### 4. Menu Registrasi Pasien Lama (Update)
![menu_3](https://github.com/user-attachments/assets/83f7da8b-fc77-42c2-90ad-fea333d54392)

### 5. Menu Hapus Data Pasien (Delete)
![menu_4](https://github.com/user-attachments/assets/9e64d067-3932-4122-8ab7-9a26d98c219c)
