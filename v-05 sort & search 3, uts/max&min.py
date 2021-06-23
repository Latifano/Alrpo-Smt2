#bonus = [30,24,61,12,13,20,27,22,20,21,30,40,41,42,40,42]

def findMax(a):
    nilai_terbesar = max(a)
    print(nilai_terbesar)
    print(a.count(nilai_terbesar))


print(findMax([30, 24, 61, 12, 13, 20, 27,
               22, 20, 21, 30, 40, 41, 42, 40, 42]))


def findMin(b):
    nilai_terbesar = min(b)
    print(nilai_terbesar)
    print(b.count(nilai_terbesar))


print(findMin([30, 24, 61, 12, 13, 20, 27,
               22, 20, 21, 30, 40, 41, 42, 40, 42]))
