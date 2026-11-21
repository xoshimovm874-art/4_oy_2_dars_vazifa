class Karta:
    def __init__(self, egasi, raqam_oxiri, balans):
        self.egasi = egasi
        self.raqam_oxiri = raqam_oxiri
        self.balans = balans

    def __str__(self):
        return f"{self.egasi} — {self.balans:,} so'm"

    def __gt__(self, boshqa):
        return self.balans > boshqa.balans

    def __lt__(self, boshqa):
        return self.balans < boshqa.balans


karta1 = Karta("Ali", "1234", 1500000)
karta2 = Karta("Vali", "5678", 2000000)

print(karta1)
print(karta2)

if karta1 > karta2:
    print("Alini kartasida ko'proq pul")
elif karta1 < karta2:
    print("Valini kartasida ko'proq pul")
else:
    print("Balanslar teng")