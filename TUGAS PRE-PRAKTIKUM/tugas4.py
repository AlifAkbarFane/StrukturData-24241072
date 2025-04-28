# variasi global untuk menyimpan data mahasiswa
mahasiswa = []

# fungsi untuk menampilkan semua data mahasiswa
def show_data():
    if len(mahasiswa) <=0 :
        print("DATA MAHASISWA BELUM ADA")
    else:
        for indeks in range(len(mahasiswa)):
            print("[%d] %s" % (indeks, mahasiswa[indeks]))

def insert_data():
    mahasiswa_baru = input("nama mahasiswa : ")
    mahasiswa.append(mahasiswa_baru)

def edit_data():
    show_data()
    indeks = int(input("Inputkan nama mahasiswa : "))
    if(indeks > len(mahasiswa)):
        print("nama mahasiswa Tidak Ditemukan")
    else:
        mahasiswa_baru = input("nama mahasiswa : ")
        mahasiswa[indeks] = mahasiswa_baru

def delete_data():
    show_data()
    indeks = int(input("Inputkan nama mahasiswa : "))
    if(indeks > len(mahasiswa)):
        print("ID Buku Tidak Ditemukan")
    else:
        mahasiswa.remove(mahasiswa[indeks])
        print(f"mahasiswa dengan nama {indeks} Terhapus")

def show_menu():
    print("\n")
    print(5*"-","MENU", 5*"-")
    print("[1] tambah mahasiswa")
    print("[2] tampilkan mahasiswa")
    print("[3] ubah mahasiswa")
    print("[4] hapus mahasiswa")
    print("[5] keluar")
    
    menu = int(input("PILIH mahasiswa : "))
    print("\n")
    if menu == 1:
        show_data()
    elif menu == 2:
        insert_data()
    elif menu == 3:
        edit_data()
    elif menu == 4:
        delete_data()
    elif menu == 5:
        exit()
    else:
        print("Pilihan Anda Salah!")

if __name__ == "__main__":
    while(True):
        show_menu()

