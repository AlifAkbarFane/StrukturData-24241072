def main():
    # Meminta pengguna memasukkan jumlah mahasiswa
    jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))
    
    # Struktur data untuk menyimpan data mahasiswa
    data_mahasiswa = {}
    
    for _ in range(jumlah_mahasiswa):
        # Input NIM
        nim = input("Masukkan NIM: ")
        
        # Input Nama
        nama = input("Masukkan Nama: ")
        
        # Input mata kuliah dan nilai
        mata_kuliah_nilai = []
        while True:
            mata_kuliah = input("Masukkan nama mata kuliah (atau ketik 'selesai' untuk selesai): ")
            if mata_kuliah.lower() == 'selesai':
                break
            nilai = float(input(f"Masukkan nilai untuk {mata_kuliah}: "))
            mata_kuliah_nilai.append((mata_kuliah, nilai))
        
        # Menyimpan data mahasiswa dalam dictionary
        data_mahasiswa[nim] = {
            'nama': nama,
            'mata_kuliah_nilai': mata_kuliah_nilai
        }
    
    # Menampilkan nilai rata-rata dan penjumlahan nilai dibagi rata-rata untuk setiap mahasiswa
    print("\nRekapitulasi Data Mahasiswa:")
    for nim, info in data_mahasiswa.items():
        nama = info['nama']
        nilai_list = [nilai for _, nilai in info['mata_kuliah_nilai']]
        jumlah_nilai = sum(nilai_list)
        rata_rata = jumlah_nilai / len(nilai_list) if nilai_list else 0
        if rata_rata != 0:
            hasil_bagi = jumlah_nilai / rata_rata
        else:
            hasil_bagi = 0
        print(f"NIM: {nim}, Nama: {nama}, Jumlah Nilai: {jumlah_nilai:.2f}, Rata-rata Nilai: {rata_rata:.2f}, Jumlah nilai dibagi rata-rata: {hasil_bagi:.2f}")
    
    # Menampilkan daftar seluruh data mahasiswa
    print("\nDaftar Seluruh Data Mahasiswa:")
    for nim, info in data_mahasiswa.items():
        print(f"NIM: {nim}, Nama: {info['nama']}, Mata Kuliah dan Nilai: {info['mata_kuliah_nilai']}")

if __name__ == "__main__":
    main()
