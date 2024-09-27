# batas = 20
# for i in range(1, batas, 2):
#     print (f"Perulangan ke-{i}")

# buah_banyak = ['Apel', 'Mangga', 'Anggur']
# for buah in buah_banyak:
#     print (buah)

# for i in range (1, 4):
#     for j in range (1, 4):
#         print (f'{i} x {j} = {i * j}')
#     print ()

# for baris in range (1, 4):
#     print ('Baris ke', baris)
#     for kolom in range (1, 4):
#         print (kolom, "kolom", end=" ")
#     print ()
#     print ()

# lagi = 'ya'
# hitung = 0
# while(lagi == 'ya'):
#     print ('Mabar')
#     hitung += 1
#     lagi = input ('Ulang lagi tidak?')
# print (f'Total Perulangan:{hitung}')

# hitung = 0
# while True:
#     hitung += 1
#     ulang = input('Masih ingin mengulang?')
#     if ulang == 'tidak' or ulang == 'Tidak':
#         break
# print (f"Total perulangan: {hit}")

# for i in range (1, 10):
#     if i == 4:
#         continue
#     print (f'Perulangan ke - {i}')

# for i in range (6):
#     for j in range (1):
#         print ("*"*i)

kesempatan = 3
while kesempatan > 0:
    username = input("Masukkan Username: ")
    password = input("Masukkan Password: ")
    if username == " admin" and password == "admin1234":
        print ("Login Berhasil")
        break
    else:
       print ("Username atau password salah")
       kesempatan -= 1
       print (f"Kesempatan login tersisa {kesempatan} kali")

print ("Program Utama")