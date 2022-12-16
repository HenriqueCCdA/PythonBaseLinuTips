#!/usr/bin/env python
"""Impreme a tabuada do 1 ao 10.

Tabuada do 1
1
2
3
...
-----------------------
Tabuada do 2
2
4
8
...
"""

__version__ = '0.1.0'
__author__ = 'Bruno'

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 
numeros = list(range(1, 11))

# Iterable (percorriveis)

# para
for n in numeros:
    print("Tabuada do:", n)
    for o in numeros:
        print(n * o)
    print("-----------")