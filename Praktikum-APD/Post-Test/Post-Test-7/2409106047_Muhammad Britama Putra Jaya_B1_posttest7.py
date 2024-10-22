import os
width = 30

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

akun = {
    "adminganteng" : {"password" : "admin123", "role" : "admin"}
}

data_pasien = {}

def buat_akun():
    clear_screen()
    username = input("Masukkan username : ")
    if username in akun:
        print("Username sudah ada!")
        return
    password = input("Masukkan password : ")
    role = "user"
    akun[username] = {"password" : password, "role" : role}
    print("Akun berhasil dibuat!")

def login():
    clear_screen()
    kesempatan = 0
    while kesempatan < 3:
        username = input("Masukkan username : ")
        if username not in akun:
            print("Username tidak ditemukan!")
            kesempatan += 1
        else:
            password = input("Masukkan password : ")
            if akun[username]["password"] == password:
                print("Login Berhasil!")
                return akun[username]["role"]
            else:
                print("Password salah!")
                kesempatan += 1
        if kesempatan == 3:
            print("Kesempatan login habis!")
            exit()

def lihat_data_pasien():
    clear_screen()
    if not data_pasien:
        print("Data pasien kosong!")
    else:
        print("="*width)
        print("Data Pasien".center(width))
        print("="*width)
        for nomor_pasien, data in data_pasien.items():
            print(f"Nomor Pasien : {nomor_pasien}")
            print(f"Nama : {data['nama']}")
            print(f"Penyakit : {data['penyakit']}")
            print(f"Ruangan : {data['ruangan']}")
            print("="*width)

def tambah_data_pasien():
    clear_screen()
    print ("="*width)
    print("Tambah Data Pasien".center(width))
    print("="*width)
    nomor_pasien = input("Masukkan Nomor Pasien : ")
    if nomor_pasien in data_pasien:
        print ("Nomor pasien sudah terdaftar!")
        return
    nama = input("Masukkan Nama Pasien : ")
    penyakit = input("Masukkan Penyakit : ")
    ruangan = input("Masukkan Ruangan : ")
    data_pasien[nomor_pasien] = {"nama" : nama, "penyakit" : penyakit, "ruangan" : ruangan}
    print("Data pasien berhasil ditambahkan!")

def ubah_data_pasien():
    clear_screen()
    print ("="*width)
    print("Ubah Data Pasien".center(width))
    print("="*width)
    nomor_pasien = input("Masukkan Nomor Pasien yang ingin diubah : ")
    if nomor_pasien in data_pasien:
        nama = input("Masukkan Nama Pasien baru : ")
        penyakit = input("Masukkan Penyakit baru : ")
        ruangan = input("Masukkan Ruangan baru : ")
        data_pasien[nomor_pasien] = {"nama" : nama, "penyakit" : penyakit, "ruangan" : ruangan}
        print("Data pasien berhasil diubah!")
    else:
        print("Nomor pasien tidak ditemukan!")

def hapus_data_pasien():
    clear_screen()
    print ("="*width)
    print("Hapus Data Pasien".center(width))
    print("="*width)
    nomor_pasien = input("Masukkan Nomor Pasien yang ingin dihapus : ")
    if nomor_pasien in data_pasien:
        del data_pasien[nomor_pasien]
        print("Data pasien berhasil dihapus!")
    else:
        print("Nomor pasien tidak ditemukan!")

def menu_admin():
    while True:
        clear_screen()
        print("="*width)
        print("Menu Admin".center(width))
        print("="*width)
        print("1. Lihat Data")
        print("2. Tambah Data")
        print("3. Ubah Data")
        print("4. Hapus Data")
        print("5. Keluar")
        print("="*width)

        menu_admin = input("Pilih menu : ")
        
        if menu_admin == '1':
            lihat_data_pasien()
            input("Tekan ENTER untuk kembali ke menu...")
        elif menu_admin == '2':
            tambah_data_pasien()
            input("Tekan ENTER untuk kembali ke menu...")
        elif menu_admin == '3':
            ubah_data_pasien()
            input("Tekan ENTER untuk kembali ke menu...")
        elif menu_admin == '4':
            hapus_data_pasien()
            input("Tekan ENTER untuk kembali ke menu...")
        elif menu_admin == '5':
            print("Logout Berhasil!")
            break
        else:
            print("Menu tidak tersedia!")

def menu_user():
    while True:
        clear_screen()
        print("="*width)
        print("Menu User".center(width))
        print("="*width)
        print("1. Lihat Data")
        print("2. Keluar")
        print("="*width)
        
        menu_user = input("Pilih menu : ")
        
        if menu_user == '1':
            lihat_data_pasien()
            input("Tekan ENTER untuk kembali ke menu...")
        elif menu_user == '2':
            print("Logout Berhasil!")
            break
        else:
            print("Menu tidak tersedia!")

while True:
    clear_screen()
    print("="*width)
    print("Menu Login".center(width))
    print("="*width)
    print("1. Login")
    print("2. Buat Akun")
    print("3. Keluar")
    print("="*width)
    
    menu = input("Pilih menu : ")
    
    if menu == '1':
        role = login()
        if role == "admin":
            menu_admin()
        elif role == "user":
            menu_user()
        else:
            print("Login gagal!")
    elif menu == '2':
        buat_akun()
    elif menu == '3':
        print("Terima kasih!")
        break
    else:
        print("Menu tidak tersedia!")