from random import triangular


class Triangle:
    side_qtd = 3

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        perimetor = self.a + self.b + self.c
        s = perimetor / 2
        area = (s * (s - self.a) * (s - self.b) *  (s - self.c)) ** 0.5
        return area

triangle = Triangle(3, 4, 5)

print(triangle.area())
