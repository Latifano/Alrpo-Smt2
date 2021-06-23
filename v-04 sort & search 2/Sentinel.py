''' IKROMI LATIFANO (A11.2020.12667) 4209 '''


def LinearSearchSentinel(k, n, A):
    '''
    k = Item yang dicari
    n = Panjang dari List
    A = List

    k = 35 (item yang dicari)
    n = 8 , didapat dari len(a)
    A = a = [20, 45, 60, 75, 35, 10, 25, 15]

    '''
    found = False
    templast = A[n - 1]
    '''templast = A[n-1]
         = A[7]
         = 15 '''

    A[n - 1] = k
    '''
    A[n-1] = k
    A[7] = 35 (Replace Index 7 Menjadi 35)
    List Awal : [20, 45, 60, 75, 35, 10, 25, 15]
    Jadi, List Terbaru [20, 45, 60, 75, 35, 10, 25, 35]'''
    i = 0

    while A[i] != k:
        i = i + 1
    '''
    ==================== Masuk Ke Looping ====================
    ---Looping 1---
    i = 0
    while A[i] != k :
    while A[0] != 35 :
    while 20 != 35 : True , Maka Looping Masih Lanjut
    Jadi , i += 1
           i = 0 + 1

    ---Looping 2---
    i = 1
    while A[i] != k :
    while A[1] != 35 :
    while 45 != 35 : True , Waduh Masih Lanjut Bro
    Jadi , i += 1
           i = 1 + 1

    ---Looping 3---
    i = 2
    while A[i] != k :
    while A[2] != 35 :
    while 60 != 35 : True , Yaelah Masih Lanjut Dong
    Jadi , i += 1
           i = 2 + 1

    ---Looping 4---
    i = 3
    while A[i] != k :
    while A[3] != 35 :
    while 75 != 35 : True , Sabar - sabar bentar lagi False
    Jadi , i += 1
           i = 3 + 1

    ---Looping 5---
    i = 4
    while A[i] != k :
    while A[4] != 35 :
    while 35 != 35 : False , Hore Akhirnya ... , Maka Looping Berhenti
    '''

    A[n-1] = templast
    '''
    ---Out Dari Looping---
    A[n-1] = templast
    A[7] = 15 (Replace Lagi index 7 Menjadi 15)
    List Sebelumnya [20, 45, 60, 75, 35, 10, 25, 35]
    Jadi, List Terbaru [20, 45, 60, 75, 35, 10, 25, 15]
    '''

    if i < n - 1 or k == A[n-1]:
        found = True
    '''
    if i < n - 1 or k == A[n-1]:
    if 4 < 7 or 35 == A[7]:
    if 4 < 7 or 35 == 15:
    Maka, True Or False == True 
        found = True

    Lalu return found
    '''
    return found


a = [20, 45, 60, 75, 35, 10, 25, 15]
print("\nAngka Ditemukan\n\t", LinearSearchSentinel(35, len(a), a), '\n')
