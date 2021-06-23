class Hero:
    def __init__(self, name, health, armor):
        self.name = name
        self.health = health
        self.armor = armor

    @property  # method sudah seperti variabel yang bisa diubah - ubah
    def info(self):
        return (f"nama : {self.name}\nhealth : {self.health}\narmor : {self.armor} ")

    @property  # method sudah seperti variabel yang bisa diubah - ubah
    def armor(self):
        pass  # dibuat kosong

    # rujukan dari method armor
    @armor.getter  # hanya mengambil
    def armor(self):
        return self.__armor

    # rujukan dari method armor
    @armor.setter  # bisa diubah
    def armor(self, inputn):
        self.__armor = inputn

    @armor.deleter  # mendelet sebuah argumen
    def armor(self):
        print('armor di delete')
        self.__armor = None


thor = Hero('thor', 100, 10)

# tidak perlu diberi info() karena sudah property
print(thor.info)  # masih bernama thor
thor.name = 'loki'  # cara merubahnya
print(thor.info)  # berubah menjadi loki

print(thor.armor)  # masih 10
thor.armor = 20  # diubah ke 20
print(thor.armor)  # berubah menjadi 20

del thor.armor
print(thor.armor)  # hasil runnya : None
print(thor.info)
