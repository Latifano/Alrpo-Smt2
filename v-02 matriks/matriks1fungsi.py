class matriks():
    def __init__(self):
        # nilai matriks A & B
        self.mA = [[4, 4, 4, 4], [6, 6, 6, 6], [8, 8, 8, 8]]
        self.mB = [[2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2]]
        # Panjang baris & kolom untuk pengecekan
        self.barisA = len(self.mA)
        self.kolomA = len(self.mA[0])
        self.barisB = len(self.mB)
        self.kolomB = len(self.mB[0])

        # Siapkan list matriks
        self.m_Hasil(self.barisA, self.kolomB)

    def m_Hasil(self, baris, kolom):
        self.m_total = []
        for i in range(baris):
            data = []
            for j in range(kolom):
                data.append(0)
            self.m_total.append(data)

    def AddMatrices(self):
        for i in range(self.barisA):
            for j in range(self.barisB):
                self.m_total = self.mA[i][j] + self.mB[i][j]
                return self.m_total
        print('mA + mB = ', self.m_total)
