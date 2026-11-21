class Inson:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh


class Talaba(Inson):
    def __init__(self, ism, yosh, universitet, baho):
        super().__init__(ism, yosh)
        self.universitet = universitet
        self.baho = baho

    def natija(self):
        if 86 <= self.baho <= 100:
            print("A'lo")
        elif 71 <= self.baho <= 85:
            print("Yaxshi")
        elif 56 <= self.baho <= 70:
            print("Qoniqarli")
        elif 0 <= self.baho < 56:
            print("Qoniqarsiz")
        else:
            print("Noto'g'ri baho")


talaba1 = Talaba("Ali", 18, "TATU", 95)
talaba2 = Talaba("Vali", 19, "TATU", 73)

talaba1.natija()
talaba2.natija()