'''
def LinearSearch(k, n, A):
    found = False
    templast = A[n-1]
    A[n-1] = k
    i = 0

    while A[i] != k:
        i += 1
    A[n-1] = templast
    if i < n - 1 or k == A[n-1]:
        found = True
        print("angka ditemukan")
    return found


a = (LinearSearch(5, 8, [2, 4, 7, 8, 5, 6, 3, 1]))
print(a)
'''


def LinearSearchListurut(k, n, A):
    found = False

    for i in range(n):
        if A[i] == k:
            found = True
        if A[i] > k:
            found = False
    return found


print(LinearSearchListurut(2, 8, [1, 2, 3, 4, 5, 6, 7, 8]))
