def LinearSearchSentinel(k, n, A):

    # Kamus Lokal
    found = False
    templast = A[n - 1]
    A[n - 1] = k
    i = 0

    # Algoritma
    while A[i] != k:
        i = i + 1
    A[n-1] = templast
    if i < n - 1 or k == A[n-1]:
        found = True
    return found


a = [20, 45, 60, 75, 35, 10, 25, 15]
print("\nAngka Ditemukan\n\t", LinearSearchSentinel(35, len(a), a), '\n')
