def list1():
    data3 = [1, 3, 5, 7, 9, 11, 13, 15]
    data4 = ['jeruk', 'pisang', 'semangka']
    data5 = [1, 2, 3]
    data6 = [4, 5, 6]

    concatenation = data5 + data6

    subdata1 = data3[-2]
    # Mengambil indeks list kedua dari paling kanan = [13]

    subdata2 = data3[2:5]
    # Mengambil dari indeks ke 2 sampai ke 4 = [5,7,9]
    # indeks ke 5 tidak diambil karena itu batasnya

    subdata3 = data3[:3]
    # Mengambil indeks dari paling kiri sampai ke3 = [1,3,5,7]

    subdata4 = data3[-2:]
    # Mengambil indeks dari paling kanan = [13,15]

    subdata5 = data4.remove('jeruk')
    # Membuang list jeruk

    return concatenation, subdata1, subdata2, subdata3, subdata4, subdata5, data4


print(list1())
