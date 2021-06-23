from aritmatika import *


def main():
    angka1 = 8
    angka2 = 7
    angka3 = 80
    angka4 = 99
    angka5 = 2
    angka6 = 120

    hasil1 = Perkalian1(angka1, angka2)
    hasil2 = Pengurangan(angka3, angka4)
    hasil3 = Pembagian(hasil2, angka5)
    hasil4 = Penjumlahan(hasil1, hasil3)
    hasil5 = Perkalian2(hasil4, angka6)

    print('\n')

    print(hasil5)

    print('\n')


main()

print(((8 * 7) + (80 - 99) / 2) * 120)
