import os

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
    panjangsisi = (float(input("Masukkan Panjang Sisi : ")))
    keliling = panjangsisi*4
    print ("Keliling Persegi adalah ",keliling," cm")
elif Menu == "2":
    panjangsisi = (float(input("Masukkan Panjang Sisi : ")))
    luas = panjangsisi*panjangsisi
    print ("Luas Persegi adalah ",luas," cm²")
elif Menu == "3":
    panjangsisi = (float(input("Masukkan Panjang : ")))
    lebarsisi = (float(input("Masukkan Lebar : ")))
    keliling = panjangsisi*2 + lebarsisi*2
    print ("Keliling Persegi Panjang adalah ",keliling," cm")
elif Menu == "4":
    panjangsisi = (float(input("Masukkan Panjang : ")))
    lebarsisi = (float(input("Masukkan Lebar : ")))
    luas = panjangsisi*lebarsisi
    print ("Luas Persegi Panjang adalah ",luas," cm²")
elif Menu == "5":
    jarijari = (float(input("Masukkan Jari-Jari : ")))
    keliling = 2*22/7*jarijari
    print ("Keliling Lingkaran adalah ",keliling," cm")
elif Menu == "6":
    jarijari = (float(input("Masukkan Jari-Jari : ")))
    luas = 22/7*jarijari*jarijari
    print ("Luas Lingkaran adalah ",luas," cm²")
elif Menu == "0":
    os.system('cls')
else:
    print ("Menu Tidak Tersedia :)")