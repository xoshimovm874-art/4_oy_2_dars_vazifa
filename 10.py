class Mahsulot:
    def __init__(self, nom, narx):
        self.nom = nom
        self.narx = narx


class Savat:
    def __init__(self):
        self.mahsulotlar = []

    def __len__(self):
        return len(self.mahsulotlar)

    def __bool__(self):
        return len(self.mahsulotlar) > 0

    def umumiy_narx(self):
        jami = 0
        for mahsulot in self.mahsulotlar:
            jami += mahsulot.narx
        return jami

    def __str__(self):
        return f"Savatda {len(self.mahsulotlar)} ta mahsulot bor"


savat = Savat()

savat.mahsulotlar.append(Mahsulot("Telefon", 3000000))
savat.mahsulotlar.append(Mahsulot("Noutbuk", 7000000))
savat.mahsulotlar.append(Mahsulot("Sichqoncha", 200000))

print(savat)
print("Mahsulotlar soni:", len(savat))

if savat:
    print("Savat bo'sh emas")
    print("Umumiy narx:", savat.umumiy_narx())
else:
    print("Savat bo'sh")