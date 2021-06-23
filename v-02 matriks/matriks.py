print('\n')
mA = [[3, 4, 5], [5, 6, 7], [6, 7, 8]]
mB = [[1, 2, 3], [4, 4, 4], [9, 10, 11]]
print('Matriks A = ', mA)
print('Matriks B = ', mB)
print('\n')


def Add2matrices(mA, mB):
    baris1 = len(mA)
    kolom1 = len(mB[0])
    baris2 = len(mA)
    kolom2 = len(mB[0])
    if baris1 != baris2 or kolom1 != kolom2:
        return -1
    else:
        # siapkan list matriks
        mAB = [0]*baris1
        for x in range(baris1):
            mAB[x] = [0]*kolom1
        # Perkalian per Elemen A * B
        for x in range(baris1):
            for y in range(kolom2):
                mAB[x][y] = mA[x][y] * mB[x][y]
        return mAB


mA = [[3, 4, 5], [5, 6, 7], [6, 7, 8]]
mB = [[1, 2, 3], [4, 4, 4], [9, 10, 11]]
print("Hasil A * B = ", Add2matrices(mA, mB))

'''
def Division2matrices(mA, mB):
    baris1 = len(mA)
    kolom1 = len(mB[0])
    baris2 = len(mA)
    kolom2 = len(mB[0])
    if baris1 != baris2 or kolom1 != kolom2:
        return -1
    else:
        # Siapkan list matriks
        mAB = [0]*baris1
        for x in range(baris1):
            mAB[x] = [0]*kolom1
        # Pembagian per Elemen A // B
        for x in range(baris1):
            for y in range(kolom2):
                mAB[x][y] = mA[x][y] // mB[x][y]
        return mAB


mA = [[20, 30, 40, 50], [10, 10, 10, 10], [5, 5, 5, 5]]
mB = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]]
print("Hasil A // B = ", Division2matrices(mA, mB))


def Add2matrices(mA, mB):
    baris1 = len(mA)
    kolom1 = len(mB[0])
    baris2 = len(mA)
    kolom2 = len(mB[0])
    if baris1 != baris2 or kolom1 != kolom2:
        return -1
    else:
        # Siapkan list matriks
        mAB = [0]*baris1
        for x in range(baris1):
            mAB[x] = [0]*kolom1
        # Pertambahan per Elemen A + B
        for x in range(baris1):
            for y in range(kolom2):
                mAB[x][y] = mA[x][y] + mB[x][y]
        return mAB


mA = [[20, 30, 40, 50], [10, 10, 10, 10], [5, 5, 5, 5]]
mB = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]]
print("Hasil A + B = ", Add2matrices(mA, mB))


def Minus2matrices(mA, mB):
    baris1 = len(mA)
    kolom1 = len(mB[0])
    baris2 = len(mA)
    kolom2 = len(mB[0])
    if baris1 != baris2 or kolom1 != kolom2:
        return -1
    else:
        # Siapkan list matriks
        mAB = [0]*baris1
        for x in range(baris1):
            mAB[x] = [0]*kolom1
        # Pengurangan per Elemen A - B
        for x in range(baris1):
            for y in range(kolom2):
                mAB[x][y] = mA[x][y] - mB[x][y]
        return mAB


mA = [[20, 30, 40, 50], [10, 10, 10, 10], [5, 5, 5, 5]]
mB = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]]
print("Hasil A - B = ", Minus2matrices(mA, mB))

print('\n')
'''
