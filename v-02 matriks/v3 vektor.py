def Vector(v1, v2):
    vjumlah = []
    vkurang = []
    vkali = []
    vbagi = []
    if len(v1) != len(v2):
        return -1
    else:
        for x in range(len(v1)):
            vjumlah.append(v1[x] + v2[x])
            vkurang.append(v1[x] - v2[x])
            vkali.append(v1[x] * v2[x])
            vbagi.append(v1[x] // v2[x])
    return vjumlah, vkurang, vkali, vbagi


print('\n', 'Hasil = ')
v1 = [10, 20, 30]
v2 = [5, 6, 7]
r = Vector(v1, v2)
for y in r:
    print(y)

print('\n')
