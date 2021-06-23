print('\nData Populasi Ternak di Kab. Pemalang tahun 2015-2017\n')

kuda = {
    'Jenis_Hewan': 'Kuda',
    'Tahun_2015': 304,
    'Tahun_2016': 299,
    'Tahun_2017': 296
}

kerbau = {
    'Jenis_Hewan': 'Kerbau',
    'Tahun_2015': 1043,
    'Tahun_2016': 960,
    'Tahun_2017': 985
}

kambing = {
    'Jenis_Hewan': 'Kambing',
    'Tahun_2015': 156474,
    'Tahun_2016': 160178,
    'Tahun_2017': 169234
}

sapi = {
    'Jenis_Hewan': 'Sapi Perah',
    'Tahun_2015': 990,
    'Tahun_2016': 934,
    'Tahun_2017': 1197
}

'''Looping Dictionary'''
for i, j in kuda.items():
    print(i, '=', j)
print('\n')
for i, j in kerbau.items():
    print(i, '=', j)
print('\n')
for i, j in kambing.items():
    print(i, '=', j)
print('\n')
for i, j in sapi.items():
    print(i, '=', j)
print('\n')

'''Mengakses Data Ternak'''
print('Data Kuda Tahun 2016 =', kuda['Tahun_2016'])
print('Data Kerbau Tahun 2015 =', kerbau['Tahun_2015'])
print('Data Sapi Tahun 2017 =', sapi['Tahun_2017'], '\n')

'''Merubah Data Ternak'''
print('\nData Awal Kambing Tahun 2017 =', kambing['Tahun_2017'])
kambing['Tahun_2017'] = 169525  # Key'Tahun_2017' diganti menjadi 169525
print('Data Akhir Kambing Tahun 2017 =', kambing['Tahun_2017'])
print('\n')
