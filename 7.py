class Telefon:
    def __init__(self, brend, model, narx):
        self.brend = brend
        self.model = model
        self.narx = narx

    def __str__(self):
        return f"{self.brend} {self.model} — {self.narx:,} so'm"

    def __eq__(self, boshqa):
        return self.narx == boshqa.narx


telefon1 = Telefon("Samsung", "A54", 4500000)
telefon2 = Telefon("Redmi", "Note 12", 4500000)
telefon3 = Telefon("iPhone", "13", 8000000)

print(telefon1)
print(telefon2)
print(telefon3)

print(telefon1 == telefon2)
print(telefon1 == telefon3)