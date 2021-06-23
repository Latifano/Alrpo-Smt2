from collections import deque
# Mengambil Library Collection dan mengimport deque


def queque():
    global data2
    # (Variabel Global)
    # # Membuat list data2 bisa di akses di fungsi lain
    data2 = deque([11, 12, 13, 14, 15])
    return data2


print(queque())


def pop():
    out = data2.popleft()
    # Buat variabel, lalu ambil data2 paling kiri
    return out


print("Data yang keluar : ", pop())

'''
Queque bisa diibaratkan seperti antrian, jadi yang keluar paling kiri / paling awal
'''
