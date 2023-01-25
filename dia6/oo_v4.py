# Frutaria

class Fruit:
    """Represent a fruit"""

    def __init__(self, name, color):
        self.name = name
        self.color = color


apple = Fruit("Apple", "red")

print(apple.name, apple.color)

banana = Fruit("Banana", "yellow")

print(banana.name, banana.color)
