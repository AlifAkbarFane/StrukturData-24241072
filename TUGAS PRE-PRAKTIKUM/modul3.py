class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

print("=====PROGRAM SEDERHANA UNTUK IMPLEMENTASI STACK DENGAN LINKED-LIST=====")
capacity = int(input("Tentukan berapa kapasitas stack: "))
top = None
size_count = 0

while True:
    print("\nPilih menu berikut ini:")
    print("1. Menambah isi stack")
    print("2. Menghapus isi stack")
    print("3. Cek Ukuran Stack saat ini")
    print("4. Cek Puncak Stack")
    print("5. Cek Stack Full")
    print("6. Keluar")
    
    choice = int(input("Masukkan pilihan anda: "))
    
    if choice == 1:
        if size_count >= capacity:
            print("Stack sudah penuh!")
            continue
            
        data = int(input("Masukkan isi stack: "))
        new_node = Node(data)
        new_node.next = top
        top = new_node
        size_count += 1
        
        # Menampilkan stack
        current = top
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        print(f"Stack: {elements}")
        
        if size_count < capacity:
            continue_choice = input("Menambah isi Stack Pilih [Ya/Tidak]: ").strip().lower()
            while continue_choice == 'ya' and size_count < capacity:
                data = int(input("Masukkan isi stack: "))
                new_node = Node(data)
                new_node.next = top
                top = new_node
                size_count += 1
                
                current = top
                elements = []
                while current:
                    elements.append(current.data)
                    current = current.next
                print(f"Stack: {elements}")
                
                if size_count < capacity:
                    continue_choice = input("Menambah isi Stack Pilih [Ya/Tidak]: ").strip().lower()
    
    elif choice == 2:
        if top is None:
            print("Stack kosong, tidak bisa menghapus elemen!")
        else:
            popped_data = top.data
            top = top.next
            size_count -= 1
            print(f"Elemen yang dihapus: {popped_data}")
            
            # Menampilkan stack setelah pop
            current = top
            elements = []
            while current:
                elements.append(current.data)
                current = current.next
            print(f"Stack: {elements}")
    
    elif choice == 3:
        print(f"Ukuran Stack saat ini: {size_count}")
    
    elif choice == 4:
        if top is None:
            print("Stack kosong, tidak ada elemen puncak!")
        else:
            print(f"Elemen puncak Stack: {top.data}")
    
    elif choice == 5:
        print("Apakah Stack Full?", size_count >= capacity)
    
    elif choice == 6:
        print("Keluar dari program.")
        break
    
    else:
        print("Pilihan tidak valid, silakan coba lagi.")
