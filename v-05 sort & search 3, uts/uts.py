# Mwnghitung Air dalam 1 Bulan
# IKROMI LATIFANO

def MenghitungDebitAir(p, l, t):
    jumlah_mandi = 30 * 2
    volume_air = (p * l * t) * 3/4
    total_literAir = jumlah_mandi * volume_air
    return total_literAir


a = ("Jumlah Air dalam 1 Bulan = ", MenghitungDebitAir(p=int(input("Masukan p :")), l=int(
    input("Masukan l :")), t=int(input("Masukan t :"))))
print(a)
