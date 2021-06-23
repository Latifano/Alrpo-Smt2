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
                print(L)
    return L


print("memori dari list setelah di bubble sort yaitu :", hex(id(print("\nHasil Bubble Sort : ", Bubble(
    8, [4, 5, 1, 3, 6, 8, 2, 7]), '\n'))))


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
        print(A)
    return A


print("memori dari list setelah di selection sort yaitu :", hex(id(print("\nHasil Selection Sort : ", Selection(
    8, [4, 5, 1, 3, 6, 8, 2, 7]), '\n'))))


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
        print(L)
    return L


print("memori dari list setelah di selection sort yaitu :", hex(id(print("\nHasil Insertion Sort : ", Insertion(
    8, [4, 5, 1, 3, 6, 8, 2, 7]), '\n'))))
