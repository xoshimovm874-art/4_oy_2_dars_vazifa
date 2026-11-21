class Shakl:
    def yuza(self):
        pass


class Kvadrat(Shakl):
    def __init__(self, tomon):
        self.tomon = tomon

    def yuza(self):
        return self.tomon ** 2


class TogriTortburchak(Shakl):
    def __init__(self, uzunlik, eni):
        self.uzunlik = uzunlik
        self.eni = eni

    def yuza(self):
        return self.uzunlik * self.eni


shakllar = [Kvadrat(5), TogriTortburchak(4, 6)]

for shakl in shakllar:
    print(shakl.yuza())