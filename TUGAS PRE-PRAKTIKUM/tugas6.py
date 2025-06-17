class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def delete_first(self):
        if not self.head:
            return
        if self.head.next:
            self.head = self.head.next
            self.head.prev = None
        else:
            self.head = None

    def delete_last(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        last = self.head
        while last.next:
            last = last.next
        last.prev.next = None

    def delete_by_value(self, value):
        if not self.head:
            return
        current = self.head
        while current:
            if current.data == value:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:  # Jika node yang dihapus adalah head
                    self.head = current.next
                return
            current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

# Contoh penggunaan
dll = DoublyLinkedList()
dll.append(2)
dll.append(4)
dll.append(6)
dll.append(8)

print("List sebelum penghapusan:")
dll.display()

dll.delete_first()
print("List setelah menghapus node pertama:")
dll.display()

dll.delete_last()
print("List setelah menghapus node terakhir:")
dll.display()

dll.delete_by_value(2)
print("List setelah menghapus node dengan nilai 2:")
dll.display()
