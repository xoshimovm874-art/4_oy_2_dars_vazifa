class Transport:
    def harakatlanish(self):
        print("Transport harakatlanmoqda")


class Mashina(Transport):
    def harakatlanish(self):
        print("Mashina yo'lda yurmoqda")


class Velosiped(Transport):
    def harakatlanish(self):
        print("Velosiped pedal bilan yurmoqda")


class Poyezd(Transport):
    def harakatlanish(self):
        print("Poyezd relsda yurmoqda")


transportlar = [Mashina(), Velosiped(), Poyezd()]

for transport in transportlar:
    transport.harakatlanish()