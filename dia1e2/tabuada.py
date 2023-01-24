#!/usr/bin/env python
"""Impreme a tabuada do 1 ao 10.

---Tabuada do 1---

    1 x 1 = 1
    2 x 1 = 2
    3 x 1 = 3
...
################################
---Tabuada do 2---

    2 x 1 = 2 
    2 x 2 = 4 
    3 x 2 = 6
...
"""

__version__ = '0.1.1'
__author__ = 'Bruno'


# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Iterable (percorriveis)
numeros = list(range(1, 11))


# para
for n1 in numeros:
    print('{:-^19}'.format(f'Tabuada do {n1:2d}'))
    print()
    for n2 in numeros:
        resultado = n1 * n2
        print('{:^19}'.format(f'{n1:2d} x {n2:2d} = {resultado:3d}'))
    print('#' * 19)