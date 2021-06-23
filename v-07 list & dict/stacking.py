def stack():
    global data1  # Membuat list data1 bisa di akses di fungsi lain
    data1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # list awal dari 1-10
    data1.append(11)  # Tambah 11 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    data1.append(12)  # Tambah 12 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    return data1  # return data1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


print(stack())


def popRight():
    out = data1.pop()  # Buat Variabel , Lalu ambil data1 paling akhir dikeluarkan
    return out  # return out = 12


print("Data yang keluar : ", popRight())

'''
Penjelasan :

Stack yaitu algoritma yang biasa digunakan pada Struktur Data, 
Stacking bisa diibaratkan seperti tumpukan baju yang diambil dari paling bawah

Built-in function python :
- append() = Menambahkan Data pada Indeks terakhir
- pop() = Untuk mengeluarkan indeks terakhir
'''
