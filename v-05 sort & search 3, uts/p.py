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


print(Binary(8, [20, 18, 19, 20, 21, 22, 23, 20],
             f=int(input("Cari angka : "))), '\n')
