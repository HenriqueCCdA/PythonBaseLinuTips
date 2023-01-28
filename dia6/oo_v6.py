# Abstração

# class Person:
#     kingdom = "animalia"

# class Fruit:
#     kingdom = "vegetalia"

# class Animal:
#     kingdim = "animalia"
from abc import ABC


class Fruit(ABC):
    kingdom = "vegatila"

    def __init__(self, colors):
        self.colors = colors


class Apple(Fruit):
    imagem = "Orange"


fruta = Apple(colors=["black"])

print(id(fruta))
