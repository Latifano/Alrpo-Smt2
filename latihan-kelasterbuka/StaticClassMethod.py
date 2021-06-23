class Hero:

    __jumlah = 0

    def __init__(self, name):
        self.__name = name
        Hero.__jumlah += 1

    def getJumlah(self):  # Berlaku Untuk Objek
        return Hero.__jumlah  # Terdapat Argumen

    def getJumlah1():  # Berlaku Untuk Class
        return Hero.__jumlah  # Tanpa Argumen

    @staticmethod  # decorator
    def getJumlah2():  # Bisa ke Objek maupun ke Class
        return Hero.__jumlah  # Tanpa Argumen

    @classmethod  # decorator
    def getJumlah3(cls):  # self bisa diubah apapun penamaannya
        return cls.__jumlah  # flexible ketika ada perubahan penamaan Clas


levi = Hero('levi')
print(levi.getJumlah())
print(Hero.getJumlah1())
print(levi.getJumlah2())
reiner = Hero('reiner')
print(Hero.getJumlah2())
