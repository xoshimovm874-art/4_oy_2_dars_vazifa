class FilmKutubxonasi:
    def __init__(self, nom, filmlar=None):
        self.nom = nom
        if filmlar is None:
            self.filmlar = []
        else:
            self.filmlar = filmlar

    def __len__(self):
        return len(self.filmlar)

    def __getitem__(self, index):
        return self.filmlar[index]

    def __contains__(self, film):
        return film in self.filmlar


kutubxona = FilmKutubxonasi(
    "Kinolar",
    ["Avatar", "Titanic", "Interstellar"]
)

print(len(kutubxona))
print(kutubxona[0])
print(kutubxona[1])
print("Avatar" in kutubxona)
print("Joker" in kutubxona)