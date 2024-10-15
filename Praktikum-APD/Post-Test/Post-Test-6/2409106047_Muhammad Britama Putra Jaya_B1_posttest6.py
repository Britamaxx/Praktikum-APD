import os
os.system ('cls')

#deklarasi variabel
width=30
statuslogin = False
kesempatan = 3

akun = {
    "adminganteng" : {"password" : "admin123", "level" : "admin"},
}

datapasien = {
    "pasien1" : {"Nama" : "nadhif", "Penyakit" : "maag", "Ruangan" : "cempaka"},
}

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
        
        if username in akun and akun[username]['password'] == password:
            os.system ('cls')
            statuslogin = True
            print ("Login Berhasil")
            print ("Selamat Datang,", username, "!")
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
        
        if username not in akun:
            akun[username] = {"password" : password, "level" : level}
            os.system ('cls')
            print ("Akun anda telah dibuat!")
        else:
            os.system ('cls')
            print ("Username sudah ada!")
    
    elif menu == '3':
        os.system ('cls')
        print ("Terima Kasih Sudah Menggunakan Aplikasi!")
        break
    else:
        os.system ('cls')
        print ("Menu Tidak Tersedia!")
        continue

while statuslogin:
    if akun[username]['level']=='admin':
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
            for pasien in datapasien:
                print (f"{datapasien[pasien]['Nama']} - {datapasien[pasien]['Penyakit']} - {datapasien[pasien]['Ruangan']}")
            print ("="*width)

        elif menuadmin == '2':
            os.system ('cls')
            print ("="*width)
            print ('Tambah Data'.center(width))
            print ("="*width)
            nama = input("Masukkan Nama Pasien : ")
            penyakit = input("Masukkan Penyakit Pasien : ")
            ruangan = input("Masukkan Ruangan Pasien : ")
            
            if nama not in datapasien:
                datapasien[nama] = {"Nama" : nama, "Penyakit" : penyakit, "Ruangan" : ruangan}
                os.system ('cls')
                print ("Data Pasien Baru Telah Ditambahkan!")
                print ("="*width)
            else:
                os.system ('cls')
                print ("Pasien sudah ada!")
            
        elif menuadmin == '3':
            os.system ('cls')
            print ("="*width)
            print ('Ubah Data'.center(width))
            print ("="*width)
            nama = input("Masukkan Nama Pasien yang ingin diubah : ")
            
            if nama in datapasien:
                os.system ('cls')
                print ("Detail Pasien:")
                print (f"{datapasien[nama]['Nama']} - {datapasien[nama]['Penyakit']} - {datapasien[nama]['Ruangan']}")
                print ("="*width)
                
                nama_baru = input("Masukkan Nama Baru Pasien : ")
                penyakit_baru = input("Masukkan Penyakit Baru Pasien : ")
                ruangan_baru = input("Masukkan Ruangan Baru Pasien : ")
                
                if nama_baru not in datapasien:
                    datapasien[nama_baru] = {"Nama" : nama_baru, "Penyakit" : penyakit_baru, "Ruangan" : ruangan_baru}
                    del datapasien[nama]
                    os.system ('cls')
                    print ("Data Pasien Berhasil Diubah!")
                    print ("="*width)
        elif menuadmin == '4':
            os.system ('cls')
            print ("="*width)
            print ('Hapus Data'.center(width))
            print ("="*width)
            nama = input("Masukkan Nama Pasien yang ingin dihapus : ")
            
            if nama in datapasien:
                del datapasien[nama]
                os.system ('cls')
                print ("Data Pasien Berhasil Dihapus!")
                print ("="*width)
            else:
                os.system ('cls')
                print ("Pasien Tidak Ditemukan!")   
        elif menuadmin == '5':
            os.system ('cls')
            print ("Terima Kasih Sudah Menggunakan Aplikasi!")
            statuslogin = False
            break
        else:
            os.system ('cls')
            print ("Menu Tidak Tersedia!")
            continue
        ulang = input ('Kembali (ya/tidak) : ')
        if ulang == "ya":
            os.system ('cls')
            continue
        else:
            os.system ('cls')
            print ("Terima Kasih Sudah Menggunakan Aplikasi!")
            statuslogin = False
            break

    elif akun[username]['level']=='guest':
        print ('='*width)
        print ('Menu Guest'.center(width))
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
            for pasien in datapasien:
                print (f"{datapasien[pasien]['Nama']} - {datapasien[pasien]['Penyakit']} - {datapasien[pasien]['Ruangan']}")
            print ("="*width)
        elif menuguest == '2':
            os.system ('cls')
            print ("Terima Kasih Sudah Menggunakan Aplikasi")
            break
        else:
            os.system ('cls')
            print ("Menu Tidak Tersedia!")
            continue
        ulang = input ('Kembali (ya/tidak) : ')
        if ulang == "ya":
            os.system ('cls')
            continue
