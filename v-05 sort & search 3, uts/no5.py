''' Nama = Ikromi Latifano , Nim = A11.2020.12667 '''
print('\nList Awal :', [145, 77, 20, 1, 120, 3, 4])


def Insertion(pl, L):
    '''
    pl = Panjang List
    L = List
    '''
    temp = 0  # menyimpan temporary data
    for x in range(1, pl):  # looping dari 1 - 7
        temp = L[x]  # temp = index ke 1 = 77
        y = x - 1  # maka y = 0
        while y >= 0 and temp < L[y]:
            # temp = A[1]
            # temp = 77
            # y = i - 1
            # y = 1 -1
            # y = 0
            # y >= 0 and temp < A[y]
            # y >= 0 and temp < A[0]
            # 0 >= 0 and 77 < 145 True, maka tukar
            L[y+1] = L[y]
            y -= 1
        L[y+1] = temp
        # Kondisi Array = [77, 145, 20, 1, 120, 3, 4]
    return L


print("\nHasil Insertion Sort : ", Insertion(
    7, [145, 77, 20, 1, 120, 3, 4]), '\n')


def Binary(pl, L, f):
    '''
    pl = Panjang List
    L = List
    f = angka yang dicari
    '''
    found = False
    bb = 0
    ba = pl - 1
    while bb <= ba and not found:  # 0 <= 6 And not False --> True
        mid = (ba+bb)//2  # mid = (0+6) / 2 = 3
        if L[mid] == f:  # jika index ke 3 (20) == angka yang dcari maka True,
            # Jika False lanjut mencari sebelah kiri dan kanan
            print("\tAngka Ditemukan")
            found = True
        else:  # mencari sebelah kiri dan kanan
            if L[mid] > f:  # jika index ke 3(20) > angka yang dicari maka
                # batas atas menjadi --> 3 - 1
                ba = mid - 1
            else:
                bb = mid + 1  # jika index ke 3(20) < angka yang dicari maka
                # batas atas menjadi --> 3 + 1
    return found  # lalu return Found


print(Binary(7, Insertion(7, [1, 3, 4, 20, 77, 120, 145]), f=int(
    input("Cari angka : "))), '\n')
