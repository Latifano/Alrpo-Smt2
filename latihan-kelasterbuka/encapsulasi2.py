class Hero:
    __jumlah = 0

    def __init__(self, name, health, attPower, armor):
        self.__name = name
        self.__healthStandar = health
        self.__attPowerStandar = attPower
        self.__armorStandar = armor
        self.__level = 1
        self.__exp = 0

        self.__healthMax = self.__healthStandar * self.__exp
        self.__attPowerMax = self.__attPowerStandar * self.__exp
        self.__armorMax = self.__armorStandar * self.__exp
        self.__health = self.__healthMax

        Hero.__jumlah += 1

    @property
    def info(self):
        return (f"{self.__name} {self.__level} :\t\n health = {self.__healthMax}\t\n attack = {self.__attPowerMax}\t\n armor = {self.__armorMax}")

    @property
    def gainExp(self):
        pass

    @gainExp.setter
    def gainExp(self, addExp):
        self.__exp += addExp  # exp awal 0 + addExp adalah kiriman dari gainExp method attack
        if self.__exp >= 100:  # Jika Exp sudah lebih dari 100 maka :
            print('\n', self.__name, 'level Up !')
            self.__level += 1  # Level naik 1
            self.__exp -= 100  # di reset ke exp = 0
            self.__healthMax = self.__healthStandar * \
                self.__level  # 100 * level(1)
            self.__attPowerMax = self.__attPowerStandar * \
                self.__level  # 10 * level(1)
            self.__armorMax = self.__armorStandar * \
                self.__level  # 15 * level(1)

    def attack(self, musuh):
        self.gainExp = 50  # Tiap 1x Attack, mendapatkan Exp 50, dirujuk ke setter di atas


levi = Hero('Levi', 100, 10, 15)
zeke = Hero('Zeke', 150, 10, 10)

print(levi.info)
levi.attack(zeke)
print(levi.info)
levi.attack(zeke)
print(levi.info)
levi.attack(zeke)
print(levi.info)
