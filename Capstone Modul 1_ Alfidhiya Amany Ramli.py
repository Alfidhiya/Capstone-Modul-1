# Capstone Modul 1: Data Pasien Rumah Sakit
# POV Admin

from tabulate import tabulate
import datetime
import os
import platform


header_pasien = ['ID Pasien', 'Nama', 'Usia', 'Gender', 'Poli', 'Tanggal', 'Pembayaran']

data_pasien = [
                [1, 'Derielle', '22', 'Female', 'Gigi', '02/11/25', 'Umum'],
                [2, 'Gayuh', '21', 'Female', 'Obgyn', '02/11/25', 'Umum'],
                [3, 'Agus', '40', 'Male', 'Internis', '02/15/25', 'Asuransi'],
                [4, 'Omar', '36', 'Male', 'Onkologi', '02/15/25', 'Asuransi'],
                [5, 'Sunardi', '58', 'Male', 'Jantung', '02/17/25', 'Asuransi']
                ]

header_dokter = ['No. Poli', 'Poli', 'Nama Dokter', 'Jam Praktek']

jadwal_dokter = [
                [1, 'Umum', 'dr. Stella', '13.00 - 16.00'],
                [2, 'Obgyn', 'dr. Anwar, Sp.OG', '16.00 - 20.00'],
                [3, 'Anak', 'dr. Aisyah, Sp.A', '13.00 - 16.00'],
                [4, 'Gigi', 'drg. Faiz', '18.00 - 22.00'],
                [5, 'Jantung', 'dr. Hasan, Sp.JP', '16.00 - 20.00'],
                [6, 'Internis', 'dr. Tirta, Sp.PD', '16.00 - 20.00'],
                [7, 'Onkologi', 'dr. Karen, Sp.B(k)Onk', '16.00 - 20.00'],
                [8, 'Mata', 'dr. Fatimah, Sp.M', '16.00 - 20.00'],
                [9, 'Trauma Center', 'dr. Baek Kanghyuk, Sp.B(k)Trauma', '08.00 - 16.00']
                ]

# Clear Terminal --> Menghapus terminal saat kembali ke menuUtama()
def hapusTerminal():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


# Menu Read --> Melihat daftar seluruh pasien dan pasien berdasarkan ID pasien
def daftarPasien():
    global data_pasien
    global header_pasien
    while True:
        print()
        print("****** DAFTAR PASIEN HANKUK NATIONAL UNIVERSITY HOSPITAL ******")
        print()
        print("Menu:")
        print('1. Tampilkan Seluruh Data Pasien')
        print('2. Tampilkan Data Pasien Berdasarkan ID Pasien')
        print('3. Kembali ke Menu Utama')
        print()
        try:
            pilihmenu1 = int(input("Masukkan angka Menu yang ingin dijalankan: "))
            if pilihmenu1 == 1:
                    print()
                    print("===== DAFTAR SELURUH PASIEN HANKUK NATIONAL UNIVERSITY HOSPITAL =====")
                    print()
                    print(tabulate(data_pasien, headers = header_pasien))
                    print()
            elif pilihmenu1 == 2:
                while True:
                    try: 
                        input_ID_pasien = int(input("Masukkan ID Pasien Anda: "))
                        pasien_by_ID = [data_pasien[input_ID_pasien - 1]]   
                        print()
                        print("===== DAFTAR PASIEN HANKUK NATIONAL UNIVERSITY HOSPITAL =====")
                        print()
                        print(tabulate(pasien_by_ID, headers=header_pasien))
                        print()
                        break
                    except:
                        print('ID yang Anda Masukkan Tidak Valid')
                        print()
                        continue
            elif pilihmenu1 == 3:
                hapusTerminal()
                break
            else:
                print('Menu yang Anda Masukkan Tidak Valid')
                continue
        except:
             print('Menu yang Anda Masukkan Tidak Valid')

# Menu Create --> Menambah daftar pasien
def registrasiPasienBaru():
    global data_pasien
    global header_pasien
    global jadwal_dokter
    global header_dokter
    while True:
        print()
        print("****** REGISTRASI PASIEN BARU HANKUK NATIONAL UNIVERSITY HOSPITAL ******")
        print()
        print("Menu:")
        print('1. Registrasi Pasien Baru')
        print('2. Kembali ke Menu Utama')
        print()
        try:
            pilihmenu2 = int(input("Masukkan angka Menu yang ingin dijalankan: "))
            if pilihmenu2 == 1:
                IDpasienbaru = data_pasien[-1][0]+1
                nama = str(input("Masukkan Nama Pasien: ")).title()
                while True:
                    try:
                        usia = int(input("Masukkan Usia Pasien (tahun): "))
                        break
                    except:
                        print("Masukkan usia dalam bentuk angka")
                        print()
                        continue
                while True:
                    gender = str(input("Masukkan Gender Pasien (Male/Female): ")).title()
                    if (gender == 'Male') or (gender == 'Female'):
                        break
                    else:
                        print('Gender tersebut tidak ada')
                        continue
                print()
                print("===== JADWAL DOKTER HANKUK NATIONAL UNIVERSITY HOSPITAL =====")
                print()
                print(tabulate(jadwal_dokter, headers=header_dokter))
                print()
                while True:
                    try:
                        poli = int(input("Masukkan Nomor Poli Tujuan: "))
                        if poli == jadwal_dokter[poli-1][0]:
                            break
                        else:
                            print('Nomor Poli yang Dipilih Tidak Ada')
                            continue
                    except:
                        print('Nomor Poli yang Dipilih Tidak Ada')
                        continue
                tanggal = datetime.datetime.now().strftime("%x")
                while True:
                    pembayaran = str(input("Masukkan Cara Pembayaran yang Diinginkan (Umum/Asuransi): ")).title()
                    if (pembayaran == 'Umum') or (pembayaran == 'Asuransi'):
                        break
                    else:
                        print('Cara Pembayaran tersebut tidak ada')
                        continue
                data_pasien_baru = [[IDpasienbaru, nama, str(usia), gender, jadwal_dokter[poli-1][1], tanggal, pembayaran]]
                print()
                print(tabulate(data_pasien_baru, headers=header_pasien))
                print()
                while True:
                    keputusan = str(input('Apakah ingin menyimpan data tersebut? (Ya/Tidak): ')).title()
                    if keputusan == 'Ya':
                        for addpasien in data_pasien_baru:
                            data_pasien.append(addpasien)
                        print()
                        print("===== DAFTAR PASIEN HANKUK NATIONAL UNIVERSITY HOSPITAL =====")
                        print()
                        print(tabulate(data_pasien, headers=header_pasien))
                        print()
                        print("Data Anda Telah Tersimpan")
                        break
                    elif keputusan == 'Tidak':
                        break
                    else:
                        print('Input yang Anda Masukkan Tidak Valid')
                        continue    
            elif pilihmenu2 == 2:
                hapusTerminal()
                break
            else:
                print('Menu yang Anda Masukkan Tidak Valid')
                continue 
        except:
            print('Menu yang Anda Masukkan Tidak Valid')
            continue


# Menu Update --> Registrasi Pasien Lama
def registrasiPasienLama():
    global data_pasien
    global header_pasien
    global jadwal_dokter
    global header_dokter
    while True:
        try:
            print()
            print("****** REGISTRASI PASIEN LAMA HANKUK NATIONAL UNIVERSITY HOSPITAL ******")
            print()
            print("Menu:")
            print('1. Registrasi Pasien Lama')
            print('2. Kembali ke Menu Utama')
            print()
            pilihmenu3 = int(input("Masukkan angka Menu yang ingin dijalankan: "))
            if pilihmenu3 == 1:
                while True:
                    print()
                    try:
                        IDpasienlama = int(input("Masukkan ID Pasien Lama (Angka): "))
                        if IDpasienlama == data_pasien[IDpasienlama-1][0]:
                            break
                        else:
                            print('Tidak Ada Pasien dengan ID Tersebut')
                            continue
                    except:
                        print('Tidak Ada Pasien dengan ID Tersebut')
                        continue
                pasien_lama = [data_pasien[IDpasienlama - 1]]
                print()
                print("===== DATA PASIEN LAMA HANKUK NATIONAL UNIVERSITY HOSPITAL =====")
                print()
                print(tabulate(pasien_lama, headers=header_pasien))
                print()
                while True:
                    keputusan = str(input("Lanjutkan Pendaftaran Pasien Lama? (Ya/Tidak): ")).title()
                    if keputusan == 'Ya':
                        print("===== JADWAL DOKTER HANKUK NATIONAL UNIVERSITY HOSPITAL =====")
                        print()
                        print(tabulate(jadwal_dokter, headers=header_dokter))
                        print()
                        while True:
                            try:
                                poli_baru = int(input("Masukkan Nomor Poli Tujuan: "))
                                if poli_baru == jadwal_dokter[poli_baru-1][0]:
                                    break
                                else:
                                    print('Nomor Poli yang Dipilih Tidak Ada')
                                    continue
                            except:
                                print('Nomor Poli yang Dipilih Tidak Ada')
                                continue
                        tanggal = datetime.datetime.now().strftime("%x")
                        while True:
                            pembayaran = str(input("Masukkan Cara Pembayaran yang Diinginkan (Umum/Asuransi): ")).title()
                            if (pembayaran == 'Umum') or (pembayaran == 'Asuransi'):
                                break
                            else:
                                print('Cara Pembayaran tersebut tidak ada')
                                continue
                        final = [IDpasienlama,
                                data_pasien[IDpasienlama - 1][1],
                                data_pasien[IDpasienlama - 1][2],
                                data_pasien[IDpasienlama - 1][3],
                                jadwal_dokter[poli_baru-1][1],
                                tanggal,
                                pembayaran]
                        tampung = []
                        tampung.append(final)
                        print()
                        print("===== DATA TERBARU PASIEN LAMA HANKUK NATIONAL UNIVERSITY HOSPITAL =====")
                        print(tabulate(tampung, headers=header_pasien))
                        print()
                        while True:
                            simpan_data = str(input("Ingin Menyimpan Data Pasien? (Ya/Tidak): ")).title()
                            if simpan_data == 'Ya':
                                data_pasien[IDpasienlama - 1] = final
                                print()
                                print("===== DAFTAR PASIEN HANKUK NATIONAL UNIVERSITY HOSPITAL =====")
                                print()
                                print(tabulate(data_pasien, headers=header_pasien))
                                print()
                                print("Data Telah Tersimpan")
                                break
                            elif simpan_data == 'Tidak':
                                break
                            else:
                                print('Input yang Anda Masukkan Tidak Valid')
                                print()
                                continue
                    elif keputusan == 'Tidak':
                        break
                    else:
                        print('Input yang Anda Masukkan Tidak Valid')
                        continue
            elif pilihmenu3 == 2:
                hapusTerminal()
                break
            else:
                print('Menu yang Anda Masukkan Tidak Valid')
                continue
        except:
            print('Menu yang Anda Masukkan Tidak Valid')
            continue


# Menu Delete --> Menghapus data pasien
def hapusPasien():
    global data_pasien
    global header_pasien
    while True:
        print()
        print("****** HAPUS DAFTAR PASIEN HANKUK NATIONAL UNIVERSITY HOSPITAL ******")
        print()
        print("Menu:")
        print('1. Hapus Daftar Pasien Berdasarkan ID Pasien')
        print('2. Hapus Daftar Seluruh Pasien')
        print('3. Kembali ke Menu Utama')
        print()
        try:
            pilihmenu4 = int(input("Masukkan angka Menu yang ingin dijalankan: "))
            if pilihmenu4 == 1:
                while True:
                    print()
                    try:
                        input_ID_pasien = int(input("Masukkan ID Pasien Anda: "))
                        pasien_by_ID = data_pasien[input_ID_pasien - 1]
                        if input_ID_pasien == pasien_by_ID[0]:
                            break
                        else:
                            print('Tidak Ada Pasien dengan ID Tersebut')
                            continue
                    except:
                        print('Tidak Ada Pasien dengan ID Tersebut')
                        continue
                print()
                print("===== DATA PASIEN LAMA HANKUK NATIONAL UNIVERSITY HOSPITAL =====")
                print()
                tabel_pasien_by_ID = [pasien_by_ID]
                print(tabulate(tabel_pasien_by_ID, headers=header_pasien))
                print()
                while True:
                    jadihapus = str(input("Apakah Ingin Menghapus Data Pasien Tersebut(Ya/Tidak): ")).title()
                    if jadihapus == 'Ya':
                        del data_pasien[input_ID_pasien - 1]
                        print()
                        print("===== DAFTAR PASIEN HANKUK NATIONAL UNIVERSITY HOSPITAL =====")
                        print()
                        print(tabulate(data_pasien, headers=header_pasien))
                        print()
                        print("Data Pasien Berhasil di Hapus")
                        break
                    elif jadihapus == 'Tidak':
                        break
                    else:
                        print('Input yang Anda Masukkan Tidak Valid')
                        continue
            elif pilihmenu4 == 2:
                print()
                hapus_semua = str(input("Apakah Ingin Menghapus Seluruh Data Pasien (Ya/Tidak): ")).title()
                if hapus_semua == 'Ya':
                    while True:
                        print()
                        password = str(input("Masukkan Password Untuk Konfirmasi: "))
                        if password == 'DrBaekILoveYou1122':
                            del data_pasien[0:]
                            print()
                            print("===== DAFTAR PASIEN HANKUK NATIONAL UNIVERSITY HOSPITAL =====")
                            print()
                            print(tabulate(data_pasien, headers=header_pasien))
                            print()
                            print("Data Pasien Terhapus Semua")
                            break
                        else:
                            print("Password Salah")
                            continue
                elif hapus_semua =='Tidak':
                    continue
                else:
                    print('Input yang Anda Masukkan Tidak Valid')
                    continue
            elif pilihmenu4 == 3:
                hapusTerminal()
                break
            else:
                print('Menu yang Anda Masukkan Tidak Valid')
                continue
        except:
            print('Menu yang Anda Masukkan Tidak Valid')
            continue

def menuUtama():
    while True:
        print()
        print(">>>>>>> HANKUK NATIONAL UNIVERSITY HOSPITAL <<<<<<<")
        print()
        print("Menu Utama: ") 
        print()
        print('1. Melihat Data Pasien')
        print('2. Registrasi Pasien Baru')
        print('3. Registrasi Pasien Lama')
        print('4. Menghapus Data Pasien')
        print('5. Exit Program')
        print()
        try:
            mau_apa = int(input("Masukkan Menu yang Ingin Dijalankan: "))
            if mau_apa == 1:
                daftarPasien()
                continue
            elif mau_apa == 2:
                registrasiPasienBaru()
                continue
            elif mau_apa == 3:
                registrasiPasienLama()
                continue
            elif mau_apa == 4:
                hapusPasien()
                continue
            elif mau_apa == 5:
                hapusTerminal()
                break
            else:
                hapusTerminal()
                print('Menu yang Anda Masukkan Tidak Valid')
        except:
            hapusTerminal()
            print('Menu yang Anda Masukkan Tidak Valid')
menuUtama()