print('\n')
'''Data Perpustakaan Udinus'''

buku_1 = {
    'ID': 101,
    'Nama_buku': 'Algoritma & Pemrograman',
    'Jumlah_hal': 250,
    'Tahun_terbit': 2017
}

buku_2 = {
    'ID': 102,
    'Nama_buku': 'Bahasa Pemrograman Python',
    'Jumlah_hal': 436,
    'Tahun_terbit': 2020
}

buku_3 = {
    'ID': 103,
    'Nama_buku': 'Internet Of Things',
    'Jumlah_hal': 155,
    'Tahun_terbit': 2018
}

buku_4 = {
    'ID': 104,
    'Nama_buku': 'Kalkulus Informatika',
    'Jumlah_hal': 350,
    'Tahun_terbit': 2019
}
buku_5 = {
    'ID': 105,
    'Nama_buku': 'Fisika',
    'Jumlah_hal': 245,
    'Tahun_terbit': 2018
}
buku_6 = {
    'ID': 106,
    'Nama_buku': 'Fundamental of Python',
    'Jumlah_hal': 110,
    'Tahun_terbit': 2020
}

'''Nested Dictionary'''
lemari_1 = {
    'rak_1': buku_1,
    'rak_2': buku_2,
    'rak_3': buku_3
}
lemari_2 = {
    'rak_1': buku_4,
    'rak_2': buku_5,
    'rak_3': buku_6
}

print('Data Lemari 1 = ', lemari_1)
print('\n')
print('Data Lemari_1,rak_1 = ', lemari_1['rak_1'])
print('\n')
print('Data Lemari_2,rak_3 = ', lemari_2['rak_3'])
print('\n')
