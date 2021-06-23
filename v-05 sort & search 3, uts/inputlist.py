l = [12, 15, 20, 50, 100]
a = l[0]

if a % 2 == 0:
    for i in l:
        print(i * 2)
elif a % 2 != 0:
    for i in l:
        print(i * 3)


def Bubble(pl, L):
    '''
    pl = Panjang List
    L = List
    '''
    a = L[0]

    if a % 2 == 0:
        for i in L:
            print(i * 2)
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

    elif a % 2 != 0:
        for i in L:
            print(i * 3)
            swap = False
            while not swap:
                swap = True
                for y in range(1, pl):
                    if L[y-1] < L[y]:
                    swap = False
                    temp = L[y]
                    L[y] = L[y-1]
                    L[y-1] = temp
            return L


print("\nSort : ", Bubble(
    5, [12, 15, 20, 50, 100]), '\n')
