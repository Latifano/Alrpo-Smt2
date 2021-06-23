''' | Nama : IKROMI LATIFANO | NIM : A11.2020.12667 |
n adalah panjang array dan A adalah array yang dimasukkan
List : [12,9,2003,111,90,91,92,10000] '''


def insertionSort(n, A):
    temp = 0  # menyimpan temporary data
    for i in range(1, n):  # looping dari 1 sampai ke n=5
        temp = A[i]
        # temp = A[1]
        # temp = 9

        j = i - 1
        # j = 1 -1
        # j = 0
        while j >= 0 and temp < A[j]:
            '''
            # [12,9,2003,111,90,91,92,10000]
            i = 1
             temp = A[1]
                 temp = 9
            # j = i - 1
                 j = 1 - 1
                     j = 0
            # j >= 0 and temp < A[j]
                 j >= 0 and temp < A[0]
                     0 >= 0 and 9 < 12 , True = Tukar

            # A[j+1] = A[j]
                 A[0+1] = A[0]
                     A[1] = 12
            # j = j - 1
                 j = 0 - 1
                     j = -1  
            # i = i - 1
                 i = 1 - 1
                     i = 0
            # A[j + 1] = temp
                 A[-1 + 1] = 9 
                     A[0] = 9
            # Kondisi Array a2 = [9,12,2003,111,90,91,92,10000]

            # i++, i = 0 + 1 = 1

            # temp = A[i]
                temp = A[1]
                    temp = A[12]
            # j = i - 1
                j = 1 - 1
                    j = 0
            # j >= 0 and temp < A[j]
                0 >= 0 and 12 < A[0]
                    0 >= 0 and 12 < 9 , False = Tidak Tukar
            # Kondisi Array a2 = [9,12,2003,111,90,91,92,10000]

            # i++, i = 1 + 1 = 2

            # temp = A[i]
                temp = A[2]
                    temp = A[2003]
            # j = i - 1
                j = 2 - 1
                    j = 1
            # j >= 0 and temp < A[j]
                1 >= 0 and 2003 < A[1]
                    1 >= 0 and 2003 < 12 , False = Tidak Tukar
            # Kondisi Array a2 = [9,12,2003,111,90,91,92,10000]

            # i++, i = 2 + 1 = 3

            # temp = A[i]
                temp = A[3]
                    temp = 111
            # j = i - 1
                j = 3 - 1
                    j = 2
            # j >= 0 and temp < A[j]
                2 >= 0 and 111 < A[2]
                    2 >= 0 and 111 < 2003 , True = Tukar
            # A[j+1] = A[j]
                A[2+1] = A[2]
                    A[3] = 2003
            # j = j - 1
                j = 2 - 1
                 j = 1
            # i = i - 2
                i = 3 - 2
                    i = 1
            # A[j+1] = temp
                A[1+1] = temp
                    A[2] = 111
            # Kondisi Array a2 = [9,12,111,2003,90,91,92,10000]

            # i++, i = 1 + 1 = 2

            # temp = A[i]
                temp = A[2]
                    temp = 111
            # j = i - 1
                j = 2 - 1
                    j = 1
            # j >= 0 and temp < A[j]
                1 >= 0 and 111 < A[1]
                    1 >= 0 and 111 < 12 , False = Tidak Tukar
            # Kondisi Array a2 = [9,12,111,2003,90,91,92,10000]

            # i++, i = 2 + 1 = 3

            # temp = A[i]
                temp = A[3]
                    temp = 2003
            # j = i - 1
                j = 3 - 1
                    j = 2
            # j >= 0 and temp < A[j]
                2 >= 0 and 2003 < A[2]
                    2 >= 0 and 2003 < 111 , False = Tidak Tukar
            # Kondisi Array a2 = [9,12,111,2003,90,91,92,10000]

            # i++, i = 3 + 1 = 4

            # temp = A[i]
                temp = A[4]
                    temp = 90
            # j = i - 1
                j = 4 - 1
                    j = 3
            # j >= 0 and temp < A[j]
                3 >= 0 and 90 < A[3]
                    3 >= 0 and 90 < 2003 , True = Tukar
            # A[j+1] = A[j]
                A[3+1] = A[3]
                    A[4] = 2003
            # j = j - 1
                j = 3 - 1
                    j = 2
            # i = i - 2
                i = 4 - 2
                    i = 2
            # A[j+1] = temp
                A[2+1] = temp
                    A[3] = 90
            # Kondisi Array a2 = [9,12,111,90,2003,91,92,10000]

            # i++, i = 2 + 1 = 3

            # temp = A[i]
                temp = A[3]
                    temp = 90
            # j = i - 1
                j = 3 - 1
                    j = 2
            # j >= 0 and temp < A[j]
                2 >= 0 and 90 < A[2]
                    2 >= 0 and 90 < 111 , True = Tukar
            # A[j+1] = A[j]
                A[2+1] = A[2]
                    A[3] = 111
            # j = j - 1
                j = 2 - 1
                    j = 1
            # i = i - 2
                i = 3 - 2
                    i = 1
            # A[j+1] = temp
                A[1+1] = 90
                    A[2] = 90
            # Kondisi Array a2 = [9,12,90,111,2003,91,92,10000]

            # i++, i = 1 + 1 = 2

            # temp = A[i]
                temp = A[2]
                 temp = 90
            # j = i - 1
                j = 2 - 1
                    j = 1
            # j >= 0 and temp < A[j]
                1 >= 0 and 90 < A[1]
                    1 >= 0 and 90 < 12 , False = Tidak Tukar
            # Kondisi Array a2 = [9,12,90,111,2003,91,92,10000]

            # i++, i = 2 + 1 = 3

            # temp = A[i]
                temp = A[3]
                    temp = 111
            # j = i - 1
                j = 3 - 1
                    j = 2
            # j >= 0 and temp < A[j]
                2 >= 0 and 111 < A[2]
                    2 >= 0 and 111 < 90 , False = Tidak Tukar
            # Kondisi Array a2 = [9,12,90,111,2003,91,92,10000]

            # i++, i = 3 + 1 = 4

            # temp = A[i]
                temp = A[4]
                    temp = 2003
            # j = i - 1
                j = 4 - 1
                    j = 3
            # j >= 0 and temp < A[j]
                3 >= 0 and 2003 < A[3]
                    3 >= 0 and 2003 < 111, False = Tidak Tukar
            # Kondisi Array a2 = [9,12,90,111,2003,91,92,10000]

            # i++, i = 4 + 1 = 5

            # temp = A[i]
                temp = A[5]
                    temp = 91
            # j = i - 1
                j = 5 - 1
                    j = 4
            # j >= 0 and temp < A[j]
                j >= 0 and 91 < A[4]
                    j >= 0 and 91 < 2003 , True = Tukar
            # A[j+1] = A[j]
                A[4+1] = A[4]
                    A[5] = 2003
            # j = j - 1
                j = 4 - 1
                    j = 3
            # i = i - 2
                i = 5 - 2
                    i = 3
            A[j+1] = temp
                A[3+1] = 91
                    A[4] = 91
            # Kondisi Array a2 = [9,12,90,111,91,2003,92,10000]

            # i++, i = 3 + 1 = 4

            # temp = A[i]
                temp = A[4]
                    temp = 91
            # j = i - 1
                j = 4 - 1
                    j = 3
            # j >= 0 and temp < A[j]
                3 >= 0 and 91 < A[3]
                    3 >= 0 and 91 < 111 , True = Tukar

            # A[j+1] = A[j]
                A[3+1] = A[3]
                    A[4] = 111
            # j = j - 1
                j = 3 - 1
                    j = 2
            # i = i - 2
                i = 4 - 2
                    i = 2
            # A[j+1] = temp
                A[2+1] = 91
                    A[3] = 91
            # Kondisi Array a2 = [9,12,90,91,111,2003,92,10000]

            # i++, i = 2 + 1 = 3

            # temp = A[i]
                temp = A[3]
                    temp = 91
            # j = i - 1
                j = 3 - 1
                    j = 2
            # j >= 0 and temp < A[j]
                2 >= 0 and 91 < A[2]
                    2 >= 0 and 91 < 90 , False = Tidak Tukar
            # Kondisi Array a2 = [9,12,90,91,111,2003,92,10000]

            # i++, i = 3 + 1 = 4

            # temp = A[i]
                temp = A[4]
                    temp = 111
            # j = i - 1
                j = 4 - 1
                    j = 3
            # j >= 0 and temp < A[j]
                3 >= 0 and 111 < A[3]
                    3 >= 0 and 111 < 91 , False = Tidak Tukar
            # Kondisi Array a2 = [9,12,90,91,111,2003,92,10000]

            # i++, i = 4 + 1 = 5

            # temp = A[i]
                temp = A[5]
                    temp = 2003
            # j = i - 1
                j = 5 - 1
                    j = 4
            # j >= 0 and temp < A[j]
                4 >= 0 and temp < A[4]
                    4 >= 0 and 2003 < 111 , False = Tidak Tukar
            # Kondisi Array a2 = [9,12,90,91,111,2003,92,10000]

            # i++, i = 5 + 1 = 6

            # temp = A[i]
                temp = A[6]
                    temp = 92
            # j = i - 1
                j = 6 - 1
                    j = 5
            # j >= 0 and temp < A[j]
                5 >= 0 and 92 < A[5]
                    5 >= 0 and 92 < 2003 , True = Tukar
            # A[j+1] = A[j]
                A[5+1] = A[5]
                    A[6] = 2003
            # j = j - 1
                j = 5 - 1
                    j = 4
            # i = i - 2
                i = 6 - 2
                    i = 4
            # A[j+1] = temp
                A[4+1] = 92
                    A[5] = 92
            # Kondisi Array a2 = [9,12,90,91,111,92,2003,10000]

            # i++, i = 4 + 1 = 5

            # temp = A[i]
                temp = A[5]
                    temp = 92
            # j = i - 1
                j = 5 - 1
                    j = 4
            # j >= 0 and temp < A[j]
                4 >= 0 and 92 < A[4]
                    4 >= 0 and 92 < 111 , True = Tukar
            # A[j+1] = A[j]
                A[4+1] = A[4]
                    A[5] = 111
            # j = j - 1
                j = 4 - 1
                    j = 3
            # i = i - 2
                i = 5 - 2
                    i = 3
            # A[j+1] = temp
                A[3+1] = 92
                    A[4] = 92
            # Kondisi Array a2 = [9,12,90,91,92,111,2003,10000]

            # i++, i = 3 + 1 = 4

            # temp = A[i]
                temp = A[4]
                    temp = 92
            # j = i - 1
                j = 4 - 1
                    j = 3
            # j >= 0 and temp < A[j]
                3 >= 0 and 92 < A[3]
                    3 >= 0 and 92 < 91 , False = Tidak tukar
            # Kondisi Array a2 = [9,12,90,91,92,111,2003,10000]

            # i++, i = 4 + 1 = 5

            # temp = A[i]
                temp = A[5]
                    temp = 111
            # j = i - 1
                j = 5 - 1
                    j = 4
            # j >= 0 and temp < A[j]
                4 >= 0 and 111 < A[4]
                    4 >= 0 and 111 < 92 , False = Tidak tukar
            # Kondisi Array a2 = [9,12,90,91,92,111,2003,10000]

            # i++, i = 5 + 1 = 6

            # temp = A[i]
                temp = A[6]
                    temp = 2003
            # j = i - 1
                j = 6 - 1
                    j = 5
            # j >= 0 and temp < A[j]
                5 >= 0 and 2003 < A[5]
                    5 >= 0 and 2003 < 111  , False = Tidak tukar
            # Kondisi Array a2 = [9,12,90,91,92,111,2003,10000]

            # i++, i = 6 + 1 = 7

            # temp = A[i]
                temp = A[7]
                    temp = 10000
            # j = i - 1
                j = 7 - 1
                    j = 6
            # j >= 0 and temp < A[j]
                6 >= 0 and 10000 < A[6]
                    6 >= 0 and 10000 < 2003  , False = Tidak tukar
            # Kondisi Array a2 = [9,12,90,91,92,111,2003,10000]

            # i++, i = 7 + 1 = 8

            # temp = A[i]
                temp = A[8]
                    temp = ERROR, Maka Out Looping
            '''
            A[j+1] = A[j]
            j = j-1
            i = i-2
        A[j+1] = temp
    return A


list_ = [12, 9, 2003, 111, 90, 91, 92, 10000]  # 8
print('\nHasil List = \n', insertionSort(8, list_))

nama = 'Ikromi Latifano'
nim = 'A11.2020.12667'
a = f"\nNama = {nama} \nNIM  = {nim}\n"
print(a)
