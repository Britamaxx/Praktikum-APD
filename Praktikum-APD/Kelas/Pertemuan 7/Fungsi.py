import os
os.system ('cls')

# def salam():
#     print ("Selamat Pagi FT Muda")
# def kali ():
#     x = 6*4
#     print (x)

# salam()
# kali()

# def luaspersegipanjang (panjang, lebar):
#     luas = panjang * lebar
#     print ("Luas Persegi Panjang : ", luas)
# luaspersegipanjang(5, 6)

# def luaspersegi (sisi):
#     luas = sisi * sisi
#     return luas 
# print ("Luas Persegi : ", luaspersegi(9))

# def luaspersegi(sisi):
#     luas = sisi * sisi
#     return luas
# def volumepersegi(sisi):
#     volume = luaspersegi(sisi)*sisi
#     print ("Volume Persegi : ", volume)
# luaspersegi(4)
# volumepersegi(6)

# nama = "Informatika"
# mataKuliah = "Algoritma Pemrograman Dasar"

# def info ():
#     nama = "Teknik Elektro"
#     mataKuliah = "Pengantar Teknik Elektro"
#     print ("Prodi : ", nama)
#     print ("Mata Kuliah : ", mataKuliah)
# print ("Prodi : ",nama)
# print ("Mata Kuliah : ", mataKuliah)
# info ()

# width = 30

# buku = []
# def showData():
#     os.system("cls")
#     if len(buku) <= 0:
#         print ("Data Buku Kosong!")
#     else:
#         print ("ID", "Nama Buku")
#         for indeks in range(len(buku)):
#             print (indeks, buku[indeks])

# def bukuBaru():
#     os.system("cls")
#     bukuBaru = input ("Judul Buku : ")
#     buku.append(bukuBaru)
#     return bukuBaru

# def editBuku():
#     os.system("cls")
#     showData()
#     indeks = int(input("Input ID Buku : "))
#     if (indeks >=len(buku) or indeks < 0):
#         print ("ID Buku Tidak Ditemukan!")
#     else:
#         judulBaru = input("Judul Baru : ")
#         buku[indeks] = judulBaru
#         print ("Data Buku Berhasil Diubah!")

# def hapusBuku():
#     os.system("cls")
#     showData()
#     indeks = int(input("Input ID Buku : "))
#     if (indeks >=len(buku) or indeks < 0):
#         print ("ID Buku Tidak Ditemukan!")
#     else:
#         del buku[indeks]
#         print ("Data Buku Berhasil Dihapus!")

# def showMenu ():
#     print ("="*width)
#     print ("Menu".center(width))
#     print ("="*width)
#     print ("1. Tampilkan Data Buku")
#     print ("2. Tambah Buku Baru")
#     print ("3. Edit Buku")
#     print ("4. Hapus Buku")
#     print ("0. Keluar")
#     menu = input ("Pilih Menu : ")
#     print ("\n")

#     if menu == "1":
#         showData()
#     elif menu == "2":
#         bukuBaru()
#     elif menu == "3":
#         editBuku()
#     elif menu == "4":
#         hapusBuku()
#     elif menu == "0":
#         exit()
#     else:
#         print ("Menu Tidak Tersedia")

# if __name__ == "__main__":
#     while True:
#         showMenu()

# def faktorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * faktorial(n-1)
    
# print(faktorial(6))

# import os
# data_mahasiswa =["Ifnu","Adi","ucup","michael"]

# def clear_screen():
#     os.system('cls || clear')

# clear_screen()

# def tampilkan_mahasiswa():
#     for i in range(len(data_mahasiswa)):
#         print(f"data ke {i+1}")
#         print(f"Nama : {data_mahasiswa[i]}")
#         print("="*10)

# def tambah_data():
#     print("MENU TAMBAH DATA")
#     print("=" * 10)
#     inputUser = input("Data yang mau ditambahkan : ")
#     data_mahasiswa.append(inputUser)
#     print(f"{inputUser} telah ditambahkan")
#     return data_mahasiswa

# def ubah_data():
#     index= int(input("masukkan index yang mau diedit : "))
#     data_baru =input("masukkan nama anda :")
#     data_mahasiswa[index-1]=data_baru
#     print("data berhasil diubah")

# def hapus_data():
#     index_user = int(input("masukkan index yang ingin dihapus: "))
#     del_user = data_mahasiswa.pop(index_user-1)
#     print(f"{del_user} telah dihapus")

# def menu():
#     print("""
#     Menu
# Lihat Data  >> 1
# Tambah Data >> 2
# Edit Data   >> 3
# Hapus Data  >> 4
# Keluar      >> 5
# """)

# while True:
#     menu()
#     pilih = input("Masukan Pilihan menu >> ")
#     clear_screen()
#     match(pilih):
#         case "1":
#             print("===Lihat Data===")
#             tampilkan_mahasiswa()
#             input("Enter.....")
#             clear_screen()
#         case "2":
#             tambah_data()
#             input("Enter....")
#             clear_screen()
#         case "3":
#             print("Menu ubah data")
#             tampilkan_mahasiswa()
#             ubah_data()
#             input("Enter.....")
#             clear_screen()
#         case "4":
#             print("Menu Hapus Data")
#             tampilkan_mahasiswa()
#             hapus_data()
#             input("Enter......")
#             clear_screen()
#         case "5":
#             print("Anda memilih menu 5")
#             exit()
#         case _:
#             print(f"Menu {pilih} tidak tersedia")
#             input("Enter.....")
#             clear_screen()

# def say_hello():
#     nama = "Yanto"
#     print ("Hello")
#     print ("World")
#     return nama

# say_hello()

# def say_hello():
#     pilihan = input ("1 Untuk berhenti 2 Untuk lanjut")
#     if pilihan == "1":
#         return
#     os.system ("cls")

# say_hello()