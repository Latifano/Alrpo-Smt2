def sum(x):
    ''' sum(x) -> sum(3)
    '''
    res = 0
    ''' res digunakan untuk menyimpan angka yang dijumlahkan
        T = 1, Karena terdapat Assignment 
    '''
    for i in range(x+1):
        '''
         range(x+1)
         range(3+1)
         range(4)
         Terdepat looping 4kali yaitu dari 0 sampai 3
         Maka terdapat juga increment i+=1 sejumalah 4 kali, 
         maka T = 8 , Karena terdapat 4 Assignment dan 4 Operasi Penjumlahan
        '''
        res += i
        '''
        -> Looping ke-1
           res = res + i
           res = 0 + 0 = 0
           T = 2 karena terdapat 1 Assignment dan 1 Operasi Penjumlahan

         return res
         res = 0
         T = 1, Karena terdapat 1 Assignment

        -> Looping ke-2
           res = res + i
           res = 0 + 1 = 1
           T = 2 karena terdapat 1 Assignment dan 1 Operasi Penjumlahan

         return res
         res = 1
         T = 1, Karena terdapat 1 Assignment

        -> Looping ke-3
           res = res + i
           res = 1 + 2 = 3
           T = 2 karena terdapat 1 Assignment dan 1 Operasi Penjumlahan

         return res
         res = 3
         T = 1, Karena terdapat 1 Assignment

        -> Looping ke-4
          res = res + i
          res = 3 + 3 = 6
          T = 2 karena terdapat 1 Assignment dan 1 Operasi Penjumlahan

         Looping Selesai
        '''

    return res
    # return = 6


print(sum(3))  # Input dengan 3

'''
Jadi total banyaknya operasi pada fungsi sum(x) adalah 4 + 16x ,
 dimana 16x didapat dari Looping : 4 Assignment, 4 operasi Penjumlahan dan 8 Increment .
 Lalu 4 didapat dari Res terulang secara Rekursif sebanyak 4 kali
'''
