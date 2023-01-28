# Procotolos / Data Model

# Addible - __add__ / __radd__


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

class Azul(Cor):
    icon = "🟦"

class Vermelho(Cor):
    icon = "🟥"

class Laranja(Cor):
    icon = "🟧"

class Violeta(Cor):
    icon = "🟪"

class Verde(Cor):
    icon = "🟩"

print("Cores primárias")
amarelo = Amarelo()
azul = Azul()
vermelho = Vermelho()
print(amarelo, azul, vermelho)

print("Cores secundarias")
print("Amaralo + Vermelho", amarelo + vermelho)
print("Azul + Amarelo", azul + amarelo)
print("Vermelho + Azul", vermelho + azul)
