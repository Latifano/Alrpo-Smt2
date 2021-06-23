''' Nama = Ikromi Latifano , Nim = A11.2020.12667 '''
print('\nList Awal :', [20, 17, 18, 19, 21, 23, 22, 24])


def Insertion(pl, L):
    '''
    pl = Panjang List
    L = List
    '''
    temp = 0
    for x in range(1, pl):
        temp = L[x]
        y = x - 1
        while y >= 0 and temp < L[y]:
            L[y+1] = L[y]
            y -= 1
        L[y+1] = temp
    return L


print("\nHasil Insertion Sort : ", Insertion(
    8, [20, 17, 18, 19, 21, 23, 22, 24]), '\n')


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


print(Binary(8, Insertion(8, [17, 18, 19, 20, 21, 22, 23, 24]), f=int(
    input("Cari angka : "))), '\n')
