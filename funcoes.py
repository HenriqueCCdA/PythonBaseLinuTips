"""Exemplos de funções"""

"""
f(x) = 5 * (x / 2)
"""

# SOLID 
# S - Single Respomsibility


def f(x):
    result = 5 * (x / 2)
    return result

def double(x):
    return x * 2


valor = double(f(10))

print(valor == 50)

####

def print_in_upper(text):
    """Procedurre with no explicit rerturn"""
    print(text.upper())
    # implicit return none

print_in_upper("bruno")


def heron(a, b, c):
    """Calcula a area de um triangulo"""
    perimeter = a + b + c
    s = perimeter / 2

    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

    return area


def heron2(params):
    """Calcula a area de um triangulo"""
    return heron(*params)



triangulos = [
    (3, 4, 5),
    (5, 12, 13),
    (8, 15, 17),
    (12, 35, 37),
    (3, 4, 5),
    (5, 12, 13),
    (8, 15, 17),
    (12, 35, 37),
]

print(list(map(heron2, triangulos)))


for t in triangulos:
    area = heron2(t)
    print(f"A area do trianguli é : {area}")
    