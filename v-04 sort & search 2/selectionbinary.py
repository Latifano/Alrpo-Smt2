''' Nama = Ikromi Latifano , Nim = A11.2020.12667 '''
print('\nList Awal :', [2, 3, 1, 4, 5, 6, 8, 7])


def Selection(n, A):
    '''
    n = Panjang List
    A = List
    '''
    x = 0
    while x != n:
        for y in range(x, n):
            if A[x] >= A[y]:
                temp = A[y]
                A[y] = A[x]
                A[x] = temp
        x += 1
    return A


print("\nHasil Selection Sort : ", Selection(
    8, [2, 3, 1, 4, 5, 6, 8, 7]), '\n')


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


print(Binary(8, Selection(8, [2, 3, 1, 4, 5, 6, 8, 7]), f=int(
    input("Cari angka : "))), '\n')
