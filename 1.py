class Hayvon:
    def __init__(self, nomi, yoshi):
        self.nomi = nomi
        self.yoshi = yoshi

    def ovoz(self):
        print("Hayvon ovoz chiqaryapti")


class It(Hayvon):
    def qoriqlash(self):
        print("It uyni qo'riqlayapti")

class Mushuk(Hayvon):
    def sichqon_tutish(self):
        print("Mushuk sichqon tutyapti")


it = It("Bobik", 3)
mushuk = Mushuk("Momiq", 2)

it.ovoz()
it.qoriqlash()

mushuk.ovoz()
mushuk.sichqon_tutish()