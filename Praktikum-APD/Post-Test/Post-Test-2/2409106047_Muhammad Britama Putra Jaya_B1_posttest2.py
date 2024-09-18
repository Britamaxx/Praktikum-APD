#input
Nama = str(input('Masukkan Nama : '))
gender = input('Masukkan Jenis Kelamin (Pria/Wanita) : ')
gender = gender.lower()=='pria'
Umur = int(input('Masukkan Umur : '))
Tinggi = float(input('Masukkan Tinggi Badan : '))
Berat_Badan = float(input('Masukkan Berat Badan : '))

#deklarasi
Pria = gender

#proses
Total = Umur + Tinggi + Berat_Badan

#output
print ('='*30)
print ('Biodata Anda')
print ('Nama                :',Nama)

if Pria :
    print ('Jenis Kelamin       : Pria')
else :
    print ('Jenis Kelamin       : Wanita')

print ('Umur                :',Umur)
print ('Tinggi Badan        :',Tinggi,'cm')
print ('Berat Badan         :',Berat_Badan,'kg')
print ('=' *30)
print ('Hasil penjumlahan variabel int dan float = ', Total)