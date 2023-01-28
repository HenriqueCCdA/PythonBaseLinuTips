# Procotolos / Data Model
# Printable

class Cor:
    english_name = "color"
    icon = "⬜"

    def __str__(self):
        return f"{self.icon} - {self.english_name}"

class Amarelo(Cor):
    english_name = "yellow"
    icon = "🟨"

class Azul(Cor):
    english_name = "blue"
    icon = "🟦"

class Vermelho(Cor):
    english_name = "red"
    icon = "🟥"


print("Cores primárias")

obj = Amarelo()

print(obj)
print(Azul())
print(Vermelho())
