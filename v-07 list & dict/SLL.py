class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data  # Data dari node
        self.next_node = next_node  # Pointer dari node

    # Menentukan node berikutnya
    def set_next(self, new_next):
        self.next_node = new_next

    # Mengambil data dari node
    def get_data(self):
        return self.data

    # Mengambil node berikutnya
    def get_next(self):
        return self.next_node


class LinkedList(object):
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def tambahbelakang(self, data):
        # Inisialisasi node baru / buat objek baru dari class node
        new_node = Node(data)
        # jika head masih kosong
        if (self.head is None):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def showData(self):
        # os.system('clear')
        print("\nTampilkan list data:\n")
        current_node = self.head
        if (self.head is None):
            print("Data masih Kosong")
        else:
            while current_node is not None:
                print(current_node.data, end='')
                print(" => ", end='')
                current_node = current_node.next_node

    def main(self):
        self.tambahbelakang('Akbar')
        self.tambahbelakang('Bintang')
        self.tambahbelakang('Daffa')
        self.tambahbelakang('Romi')
        self.tambahbelakang('Rizqi')
        self.showData()
        print()


if __name__ == "__main__":
    # execute only if run as a script
    l = LinkedList()
    l.main()
