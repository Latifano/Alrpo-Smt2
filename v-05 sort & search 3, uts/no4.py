# IKROMI LATIFANO
def Bubble(pl, L):
    '''
    pl = Panjang List
    L = List

    '''
    swap = False  # Artinya yaitu untuk menyimpan list sementara dan menampung list yang akan ditukar
    while not swap:
        swap = True  # Karena True maka lanjut looping

        for y in range(1, pl):
            # looping sebanyak 1 - 9

            if L[y-1] > L[y]:
                # membandingkan 0 > 1 , karena loopingan pertama
                swap = False
                temp = L[y]
                L[y] = L[y-1]
                L[y-1] = temp
    return L


print("\nHasil Bubble Sort : ", Bubble(
    9, [33, 11, 22, 99, 100, 102, 200, 50, 20]), '\n')
