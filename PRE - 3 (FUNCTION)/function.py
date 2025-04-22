# membuat function sederhana
def sapa():
    print("Halo, selamat datang!")

sapa()  # Memanggil fungsi ke-1 
sapa()  # Memanggil fungsi ke-2 
sapa()  # Memanggil fungsi ke-3

# function dengan parameter
# function dengan 1 parameter
def sapa_nama(nama):
    print(f"Halo, {nama}!")

# Pemanggilan Function
sapa_nama("aby")
sapa_nama("zhira")

# function dengan lebih dari 1 parameter
def luas_segitiga(alas, tinggi):
    luas = (alas * tinggi) / 2
    print("Luas segitiga: %f" % luas)

# Pemanggilan Function
luas_segitiga(4, 6)

# function dengan return (nilai kembali)
def tambah(a, b):
    return a + b

# pemanggilan fungsi
hasil = tambah(3, 5)
print("Hasil:", hasil)

# function fungsi digunakan didalam fungsi lagi
# rumus sisi x sisi
def luas_persegi(sisi):
    luas = sisi * sisi
    return luas


# rumus: sisi x sisi x sisi
def volume_persegi(sisi):
    volume = luas_persegi(sisi) * sisi
    return volume

# pemanggilan fungsi
vol_persegi = volume_persegi(6)
print(f"Volume Persegi = {vol_persegi}")

def student(firstname, lastname ='Mark', standard ='Fifth'):
    print(firstname, lastname, 'studies in', standard, 'Standard')

# pemanggilan function, dengan 1 argumen
student("Wallberg")
# pemanggilan function, dengan 3 argumen
student('John', 'Gates', 'Seventh')  

# function pada hints
def kali(a: int, b: int) -> int:
    return a * b

# Pemanggilan function
print("Hasil = " ,kali(3, 4))
print("Tipe Data : ", type(kali(3,4)))

# function dengan *args
# *args untuk argumen bervariasi
def myFun(*argv):
    for arg in argv:
        print(arg)

myFun('Hello', 'Selamat Datang', 'Di', 'PTI UNDIKMA')

# function dengan **
def info_mahasiswa(**data):
    for key, value in data.items():
        print(f"{key}: {value}")

# Pemanggilan function
info_mahasiswa(nama="Rina", jurusan="TI", angkatan=2022)

# Function variasi global dan lokal python
nama = "Budi"  # variabel global

def sapa():
    print("Halo,", nama)

# memanggil function
sapa()