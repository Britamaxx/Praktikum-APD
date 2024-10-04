# data = [1, 2 , 3, 4, 5]
# data_2 = ((1, 2, 3, 4, 5))

# print (type(data))
# print (type(data_2))
# print (data[1])

# buah = ['apel', 'anggur', 'yanto']

# print (buah)
# print()
# buah.append('semangka')
# print()
# buah.append(True)
# print(buah)

# buah.insert(1, 'matakucing')
# print(buah)

# buah[1] = 'Mata Kucing'
# print(buah)

# del buah[2]
# print(buah)

# data_mahasiswa = [
#     ['047', 'britama'], 
#     ['049', 'nopal']
#     ]
# print (data_mahasiswa[0][1])

# data_mahasiswa.append(['051', 'yusuf'])
# print (data_mahasiswa)

# buah = ["Apel", "Semangka", "Jeruk"]
# indeks = 1
# for data in buah:
#     print(f"data ke {indeks}")
#     print(data)
#     print("="*10)
#     indeks += 1

# for indeks in range(len(indeks)):
#     print(f"data ke {indeks + 1}")
#     print(buah[indeks])
#     print("="*10)   

# mahasiswa = (47, 'Informatika', '2409106047', "Muhammad Britama")

# absen, prodi, nim, nama = mahasiswa

# print(absen)
# print(prodi)
# print(nim)
# print(nama)

# import os
# os.system ('cls')

# data_mahasiswa = []

# while True:
#     print ("="*50)
#     print ("   Menu")
#     print ("="*50)
#     print ("1. Lihat Data")
#     print ("2. Tambah data")
#     print ("3. Edit data")
#     print ("4. Hapus data")
#     print ("5. Keluar")

#     menu = input("Masukkan pilihan (1-5): ")

#     if menu == "1":
#         os.system('cls')
#         print ("Berikut data mahasiswa")
#         print (data_mahasiswa)

#     elif menu == "2":
#         os.system('cls')
#         absen = input("Masukkan absen: ")
#         prodi = input("Masukkan prodi: ")
#         nim = input("Masukkan NIM: ")
#         nama = input("Masukkan nama: ")
#         data_mahasiswa.append([absen, prodi, nim, nama])
#         print ("Data berhasil ditambahkan")
    
#     elif menu == "3":
#         os.system('cls')
#         print (data_mahasiswa)
#         index = int(input("Masukkan index data yang ingin diedit: ")) - 1
#         if index < len(data_mahasiswa):
#             absen = input("Masukkan absen baru: ")
#             prodi = input("Masukkan prodi baru: ")
#             nim = input("Masukkan NIM baru: ")
#             nama = input("Masukkan nama baru: ")
#             data_mahasiswa[index] = [absen, prodi, nim, nama]
#             print ("Data berhasil diubah")
#         else:
#             print ("Index data invalid")
    
#     elif menu == "4":
#         os.system('cls')
#         print (data_mahasiswa)
#         index = int(input("Masukkan index data yang ingin dihapus: ")) - 1
#         if index < len(data_mahasiswa):
#             del data_mahasiswa[index]
#             print ("Data berhasil dihapus")
#         else:
#             print ("Index data invalid")
    
#     elif menu == "5":
#         os.system('cls')
#         print ("Terima kasih, sampai jumpa lagi")
#         break

#     else:
#         os.system('cls')
#         print ("Pilihan menu invalid")

#     ulang = input("Kembali ke menu?")
#     if ulang == "ya":
#         continue
#     else:
#         break

# mhs = ['a', 'b', 'c', 'd',]
# mhs[2] = "e"

# for i in mhs:
#     print(i, end="")