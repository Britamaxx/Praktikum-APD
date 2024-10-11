import os
os.system ('cls')


# daftarBuku = {
#     "Buku1": "Harry Potter",
#     "Buku2": "Percy Jackson",
#     "Buku3": "Twilight"
# }

# print (daftarBuku["Buku1"])
# print (daftarBuku["Buku2"])
# print (daftarBuku["Buku3"])

# print (daftarBuku)

# games = dict(Sekiro = "Action", Pokemon = "Adventure", CounterStrike = "FPS")

# print (games)

# Biodata = {
#     "Nama": "Muhammad Britama Putra Jaya",
#     "NIM": "2409106047",
#     "KRS": ["Kalkulus","Fisika Dasar", "Agama"],
#     "Mahasiswa Aktif": True,
#     "Sosial Media": {
#         "Instagram" : "@britama.putra.jaya",
#         "Discord" : "siriusinaja",
#     }
# }

# print (f"Nama saya adalah {Biodata['Nama']}")
# print (f"NIM saya adalah {Biodata['NIM']}")
# print (f"Instagram : {Biodata['Sosial Media']['Instagram']}")

# nilai = {
#     "Matematika" : 100,
#     "Fisika" : 90,
#     "Biologi" : 80
# }

# for i in nilai:
#     print (i)

# for i, j in nilai.items():
#     print (f"Nilai {i} anda adalah {j}")

# Film = {
#     'Avenger Endgame' : "Action",
#     'Spider-Man: Far From Home' : "Adventure",
#     'Lookism' : "Drama"
# }

# print (Film)

# Film["Oh My Queen"] = "Comedy"
# Film.update({"Khazanah" : "TV Series"})
# print (Film)

# Film['Lookism'] = "Action"
# Film.update({"Avenger Endgame" : "Comedy"})
# print (Film)

# data = {
#     "Nama" : "Britama",
#     "Kelas" : "B 24",
#     "Jurusan" : "Informatika"
# }

# print (data)

# del data["Nama"]
# print (data)
# print (data.get("Nama"))

# cache = data.pop("Nama")
# print (data)
# print (data.get("Nama"))
# print (cache)

# data.clear()
# print (data)

# print ("Jumlah Data = ", len(data))

# Buah = {
#     "Apel" : "Merah",
#     "Jeruk" : "Oren",
#     "Anggur" : "Ungu"
# }

# pinjam = Buah.copy()
# print ("Dictionary telah disalin : ", pinjam)

# key = "Apel", "Jeruk", "Anggur"
# value = 1

# buah = dict.fromkeys(key, value)
# print (buah)

# nilai = {
#     "Matematika" : 100,
#     "Fisika" : 90,
#     "Biologi" : 80
# }

# for i in nilai.keys():
#     print (i)

# print ("")

# for i in nilai.values():
#     print (i)

# print (nilai)
# print ("")

# print ("Nilai : ", nilai.setdefault("Kimia", 70))
# print ("")
# print (nilai)

# Musik = {
#     "Alan Walker" : ["Lily", "On My Way"],
#     "Adele" : ["Love In The Dark", "Easy On Me"],
#     "Eminem" : ["Mockingbird"]
# }

# for i, j in Musik.items():
#     print (f"Musik Milik {i} adalah : ")
#     for song in j:
#         print (song)
#     print ("")