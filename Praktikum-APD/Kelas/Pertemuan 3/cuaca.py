cuaca = "mendung"
if cuaca == "cerah":
    print ("Kamu keluar rumah")
else:
    print ("Kamu ngendok")



Nilai = (float(input("Masukkan Angka : ")))

if Nilai < 0:
    print ("Negatif")
else:
    print ("Positif")



Umur = (int(input("Masukkan Umur Anda : ")))
if Umur <= 10:
    print ("Kamu Anak-Anak")
elif Umur <= 18:
    print ("Kamu Remaja")
elif Umur <= 35:
    print ("Kamu Dewasa")
elif Umur <= 65:
    print ("Kamu Paruh Baya")
elif Umur <= 100:
    print ("Kamu Terlalu Tua")
else:
    print ("Kamu Fossil")



print ("Menu : ")
print ("1. Nonton Film")
print ("2. Ngoding")
print ("3. Keluar")
Menu = (str(input("1. Nonton Film , 2. Ngoding , 3. Keluar")))
if Menu == "1":
    print ("Kamu Nonton Marvel")
elif Menu == "2":
    print ("Kamu lagi buat game")
elif Menu == "3":
    print ("Kamu lagi diluar")
else:
    print ("Menu tidak tersedia")



value = (int(input("Masukkan Angka : ")))
if value %2 == 0:
    print ("Genap")
if value > 0:
    print ("Positif")

valuee = (int(input("Msukka Angka : ")))
if valuee %2 == 0:
    print ("Genap")
elif valuee > 0:
    print ("Positif")