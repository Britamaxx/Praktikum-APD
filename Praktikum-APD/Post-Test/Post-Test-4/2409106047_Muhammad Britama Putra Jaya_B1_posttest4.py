import os
os.system ('cls')

username = "Tama"
password = "047"
kesempatan = 3

while kesempatan >= 1:
    print ("="*30)
    print ("            Login")
    print ("="*30)
    user = str(input("Masukkan Username : "))
    pw = str(input("Masukkan Password : "))
    if user == username and pw == password:
        os.system ('cls')
        print ("Login Berhasil")
        print ("Selamat Datang, ",username,"!")
        break
    else:
        os.system ('cls')
        print ("Username atau password anda salah!")
        kesempatan -= 1
        if kesempatan == 0:
            exit ("Keluar program")

if kesempatan > 0:
    while True:
            print ("="*50)
            print ("    Menu Menghitung Keliling/Luas Bangun Datar")
            print ("="*50)
            print ("1. Keliling Persegi")
            print ("2. Luas Persegi")
            print ("3. Keliling Persegi Panjang")
            print ("4. Luas Persegi Panjang")
            print ("5. Keliling Lingkaran")
            print ("6. Luas Lingkaran")
            print ("0. Keluar Program")
            print ("="*50)

            Menu = str(input("Pilih Salah Satu Dari Menu : "))
            if Menu == "1":
                os.system ('cls')
                panjangsisi = (float(input("Masukkan Panjang Sisi : ")))
                keliling = panjangsisi*4
                print ("Keliling Persegi adalah ",keliling," cm")
            elif Menu == "2":
                os.system ('cls')
                panjangsisi = (float(input("Masukkan Panjang Sisi : ")))
                luas = panjangsisi*panjangsisi
                print ("Luas Persegi adalah ",luas," cm²")
            elif Menu == "3":
                os.system ('cls')
                panjangsisi = (float(input("Masukkan Panjang : ")))
                lebarsisi = (float(input("Masukkan Lebar : ")))
                keliling = panjangsisi*2 + lebarsisi*2
                print ("Keliling Persegi Panjang adalah ",keliling," cm")
            elif Menu == "4":
                os.system ('cls')
                panjangsisi = (float(input("Masukkan Panjang : ")))
                lebarsisi = (float(input("Masukkan Lebar : ")))
                luas = panjangsisi*lebarsisi
                print ("Luas Persegi Panjang adalah ",luas," cm²")
            elif Menu == "5":
                os.system ('cls')
                jarijari = (float(input("Masukkan Jari-Jari : ")))
                keliling = 2*22/7*jarijari
                print ("Keliling Lingkaran adalah ",keliling," cm")
            elif Menu == "6":
                os.system ('cls')
                jarijari = (float(input("Masukkan Jari-Jari : ")))
                luas = 22/7*jarijari*jarijari
                print ("Luas Lingkaran adalah ",luas," cm²")
            elif Menu == "0":
                os.system('cls')
                print ("Terima Kasih, sampai jumpa kembali!")
                break
            else:
                print ("Menu Tidak Tersedia :)")
                continue

            ulang = input ("Kembali ke menu utama? ya/tidak")
            if ulang == "ya":
                continue
            else:
                break