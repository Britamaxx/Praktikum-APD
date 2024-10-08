import os
os.system ('cls')

#deklarasi variabel
width=30
statuslogin = False
kesempatan = 3

#dataset
akun = [
    ['adminganteng', 'admin123', 'admin'],
    ['tama', 'tama123', 'guest']
]

datapasien = [
    ['nadhif', 'Maag', 'Cempaka']
]

while statuslogin == False:
    print ('='*width)
    print ('Menu'.center(width))
    print ('='*width)
    print ('1. Login')
    print ('2. Buat Akun')
    print ('3. Keluar')
    print ('='*width)

    menu = input("Pilih Menu : ")

    if menu == '1':
        os.system ('cls')
        print ("="*width)
        print ("Login".center(width))
        print ("="*width)
        username = input("Masukkan Username : ")
        password = input("Masukkan Password : ")
        for i in range(len(akun)):
            if username == akun[i][0] and password == akun[i][1]:
                os.system ('cls')
                statuslogin = True
                print ("Login Berhasil")
                print ("Selamat Datang,", akun[i][0], "!")
                break
        else:
            os.system ('cls')
            print ("Login Gagal! Username atau password salah")
            kesempatan -= 1
            if kesempatan == 0:
                os.system ('cls')
                print ("Silahkan coba lagi dalam beberapa menit :)")
                exit()
    elif menu == '2':
        os.system ('cls')
        print ("="*width)
        print ('Buat Akun'.center(width))
        print ("="*width)
        username = input("Masukkan Username : ")
        password = input("Masukkan Password : ")
        level = "guest"
        akun.append([username, password, level])
        os.system ('cls')
        print ("Akun anda telah dibuat!")
    elif menu == '3':
        os.system ('cls')
        print ("Terima Kasih Sudah Menggunakan Aplikasi!")
        break
    else:
        os.system ('cls')
        print ("Menu Tidak Tersedia!")
        continue


while statuslogin:
    if akun[i][2]=='admin':
        print ('='*width)
        print ('Menu Admin'.center(width))
        print ('='*width)
        print ('1. Lihat Data')
        print ('2. Tambah Data')
        print ('3. Ubah Data')
        print ('4. Hapus Data')
        print ('5. Keluar')
        print ('='*width)
        
        menuadmin = input("Pilih Menu : ")
        
        if menuadmin == '1':
            os.system ('cls')
            print ("="*width)
            print ('Lihat Data'.center(width))
            print ("="*width)
            print ("Data Pasien:")
            for i in range(len(datapasien)):
                print (f"{i+1}. {datapasien[i][0]} - {datapasien[i][1]} - {datapasien[i][2]}")
            print ("="*width)
        elif menuadmin == '2':
            os.system ('cls')
            print ("="*width)
            print ('Tambah Data'.center(width))
            print ("="*width)
            nama = input("Masukkan Nama Pasien : ")
            penyakit = input("Masukkan Penyakit Pasien : ")
            ruangan = input("Masukkan Ruangan Pasien : ")
            datapasien.append([nama, penyakit, ruangan])
            os.system ('cls')
            print ("Data Pasien Baru Telah Ditambahkan!")
            print ("="*width)
        elif menuadmin == '3':
            os.system ('cls')
            print ("="*width)
            print ('Ubah Data'.center(width))
            print ("="*width)
            print ("Data Pasien:")
            for i in range(len(datapasien)):
                print (f"{i+1}. {datapasien[i][0]} - {datapasien[i][1]} - {datapasien[i][2]}")
                print ("="*width)
            index = int(input("Pilih Index Data yang Akan Diubah : ")) - 1
            if index >= 0 and index < len(datapasien):
                nama = input("Masukkan Nama Pasien Baru : ")
                penyakit = input("Masukkan Penyakit Pasien Baru : ")
                ruangan = input("Masukkan Ruangan Pasien Baru : ")
                datapasien[index] = [nama, penyakit, ruangan]
                os.system ('cls')
                print ("Data Pasien Berhasil Diubah!")
                print ("="*width)
        elif menuadmin == '4':
            os.system ('cls')
            print ("="*width)
            print ('Hapus Data'.center(width))
            print ("="*width)
            print ("Data Pasien:")
            for i in range(len(datapasien)):
                print (f"{i+1}. {datapasien[i][0]} - {datapasien[i][1]} - {datapasien[i][2]}")
                print ("="*width)
            index = int(input("Pilih Index Data yang Akan Dihapus : ")) - 1
            if index >= 0 and index < len(datapasien):
                del datapasien[index]
                os.system ('cls')
                print ("Data Pasien Berhasil Dihapus!")
                print ("="*width)
            else:
                os.system ('cls')
                print ("Data Pasien Tidak Ditemukan!")
                print ("="*width)
        elif menuadmin == '5':
            os.system ('cls')
            print ("Terima Kasih Sudah Menggunakan Aplikasi!")
            break

        else:
            os.system ('cls')
            print ("Menu Tidak Tersedia!")
            continue
        ulang = input ('Kembali (ya/tidak) : ')
        if ulang == 'ya':
            os.system ('cls')
            continue
        else:
            break

    elif akun[i][2] == 'guest':
        print ('='*width)
        print ('Menu'.center(width))
        print ('='*width)
        print ('1. Lihat Data')
        print ('2. Keluar')
        print ('='*width)
        
        menuguest = input("Pilih Menu : ")
        
        if menuguest == '1':
            os.system ('cls')
            print ("="*width)
            print ('Lihat Data'.center(width))
            print ("="*width)
            print ("Data Pasien:")
            for i in range(len(datapasien)):
                print (f"{i+1}. {datapasien[i][0]} - {datapasien[i][1]} - {datapasien[i][2]}")
            print ("="*width)
            ulang = input ('Kembali (ya/tidak) : ')
            if ulang == 'ya':
                os.system ('cls')
                break
            else:
                break
        elif menuguest == '2':
            os.system ('cls')
            print ("Terima Kasih Sudah Menggunakan Aplikasi!")
            break
        else:
            os.system ('cls')
            print ("Menu Tidak Tersedia!")
            continue