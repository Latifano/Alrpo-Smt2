class Hero:
    def __init__(self, name, health, attackpower):
        self.__name = name
        self.__health = health
        self.__attpower = attackpower

    def getName(self):  # Getter
        return self.__name

    def getHealth(self):  # Getter
        return self.__health

    def diserang(self, serang):  # Setter
        self.__health -= serang


Senku = Hero("Senku", 50, 5)

print(Senku.getName())  # Mengambil Nama
print(Senku.getHealth())  # Mengambil Health
Senku.diserang(20)  # Health - 20 . 50-20 = 30
print(Senku.getHealth())  # Mengambil Health
