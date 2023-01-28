# Procotolos / Data Model

# Iterable - __iter__


class Cor:
    english_name = "color"
    icon = "⬜"

    def __str__(self):
        return self.icon

    def __add__(self, other):
        mixtable = [
            ((Amarelo, Vermelho), Laranja),
            ((Azul, Amarelo), Verde),
            ((Vermelho, Azul), Violeta),
        ]
        for mix, result in mixtable:
            if isinstance(self, mix) and isinstance(other, mix):
                return result()


class Amarelo(Cor):
    icon = "🟨"

    def __len__(self):
        return 1

class Azul(Cor):
    icon = "🟦"

    def __len__(self):
        return 2


class Vermelho(Cor):
    icon = "🟥"

    def __len__(self):
        return 3


class Laranja(Cor):
    icon = "🟧"

    def __len__(self):
        return 4


class Violeta(Cor):
    icon = "🟪"

    def __len__(self):
        return 5


class Verde(Cor):
    icon = "🟩"

    def __len__(self):
        return 6


print("Cores primárias")
amarelo = Amarelo()
azul = Azul()
vermelho = Vermelho()
print(amarelo, azul, vermelho)

print("Cores secundarias")
print("Amaralo + Vermelho", amarelo + vermelho)
print("Azul + Amarelo", azul + amarelo)
print("Vermelho + Azul", vermelho + azul)


class Paleta:
    def __init__(self, *cores):
        self._cores = cores

    def __len__(self):
        return len(self._cores)

    def __iter__(self):
        return iter([cor for cor in self._cores])

    def __contains__(self, item):
        return item in [cor.icon for cor in self._cores]

    def __getitem__(self, item):
        if isinstance(item, (int, slice)):
            return self._cores[item]
        if isinstance(item, str):
            for cor in self._cores:
                if cor.__class__.__name__.lower() == item.lower():
                    return cor


rgb = Paleta(Vermelho(), Verde(), Azul())

for cor in rgb:
    print(cor)


# Container - __contains__

print("🟥" in rgb)


# Size - __len__

for cor in rgb:
    print(cor, len(cor))

print(len(rgb))


# Collection - Sizedr + Container + Iterable

# Subscritebla - __getitem__

print(rgb[1])
print(rgb["azul"])
