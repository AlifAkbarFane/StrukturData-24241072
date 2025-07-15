nama_customer = input("Masukkan nama customer: ")
tanggal_belanja = input("Masukkan tanggal belanja (yyyy-mm-dd): ")
info_customer = (nama_customer, tanggal_belanja)
jumlah_barang = int(input("Masukkan jumlah barang yang akan dibeli: "))

# dictionary
daftar_barang = []

for i in range(jumlah_barang):
        print(f"\nData barang ke-{i + 1}:")
        nama_barang = input("Nama barang: ")
        harga_satuan = float(input("Harga satuan barang: "))
        qty = int(input("Jumlah QTY: "))
        
        barang = {
            "nama_barang": nama_barang,
            "harga_satuan": harga_satuan,
            "qty": qty,
            "total_harga": harga_satuan * qty
        }
        
        daftar_barang.append(barang)
    
print("\n DATA CUSTOMER ")
print(f"Nama Customer: {info_customer[0]}")
print(f"Tanggal Belanja: {info_customer[1]}")
    
print("\n DAFTAR BELANJA ")
total_bayar = 0
for barang in daftar_barang:
        print(f"Nama Barang: {barang['nama_barang']}")
        print(f"Harga Satuan: Rp {barang['harga_satuan']:,.2f}")
        print(f"Jumlah QTY: {barang['qty']}")
        print(f"Total Harga: Rp {barang['total_harga']:,.2f}")
        total_bayar += barang['total_harga']
    
print(f"Total Bayar: Rp {total_bayar:,.2f}")
