''' Nama = Ikromi Latifano , Nim = A11.2020.12667 '''
print('\nList Awal :', [9, 10, 12, 11, 13, 15, 14, 16])


def Bubble(pl, L):
    '''
    pl = Panjang List
    L = List
    '''
    swap = False
    while not swap:
        swap = True
        for y in range(1, pl):
            if L[y-1] > L[y]:
                swap = False
                temp = L[y]
                L[y] = L[y-1]
                L[y-1] = temp
    return L


print("\nHasil Bubble Sort : ", Bubble(
    8, [9, 10, 12, 11, 13, 15, 14, 16]), '\n')


def Binary(pl, L, f):
    '''
    pl = Panjang List
    L = List
    f = angka yang dicari
    '''
    found = False
    bb = 0
    ba = pl - 1
    while bb <= ba and not found:
        mid = (ba+bb)//2
        if L[mid] == f:
            print("\tAngka Ditemukan")
            found = True
        else:
            if L[mid] > f:
                ba = mid - 1
            else:
                bb = mid + 1
    return found


print(Binary(8, Bubble(8, [9, 10, 12, 11, 13, 15, 14, 16]), f=int(
    input("Cari Angka : "))), '\n')
