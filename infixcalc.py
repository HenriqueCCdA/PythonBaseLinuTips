#!/usr/bin/env python3
"""Calculadora infix.

Funcionamento:

[operação] [n1] [n2]

Operação:
sum -> +
sub -> -
mul -> *
div -> /

Use:
$ infixcalc.py sum 5 2
7

$ infixcalc.py mul 10 5
50

$ infixcalc.py
operação: sum
n1: 5
n2: 4
9

Os resultados serão salvos em 'ínfixcalc.log'
"""

__version__ = '0.1.0'

import os
import sys
from datetime import datetime

arguments = sys.argv[1:]

valid_operations = {	
	"sum": lambda a, b: a + b,
	"sub": lambda a, b: a - b,
	"mul": lambda a, b: a * b,
	"div": lambda a, b: a / b,
}


if not  arguments:
	operation = input('Operação:')
	n1 = input('n1:')
	n2 = input('n2:')
	arguments = [operation, n1, n2]
elif len(arguments) != 3:
	print('Número de argumentos inválidos')
	print()
	print('ex: "sum 5 5"')
	sys.exit(1)

operation, *nums = arguments

if operation not in valid_operations:
	print('Operação inválida')
	print(valid_operations)
	sys.exit(1)

validated_nums = []

for num in nums:
	if not num.replace('.', '').isdigit():
		print(f'Número inválido {num}')
		sys.exit(1)
	if '.' in num:
		num = float(num)
	else:
		num = int(num)
	validated_nums.append(num)

try:
    n1, n2 = validated_nums
except ValueError as e:
    print(str(e))
    sys.exit(1)

result = valid_operations[operation](n1, n2)

path = os.curdir
filepath = os.path.join(path, 'infixcalc.log')
timestamp = datetime.now().isoformat()
user = os.getenv('USER', 'anonymous')

print(f'O resultado é {result}')
	
try:
    with open(filepath, 'a') as file_:
	    file_.write(f'{timestamp} - {user} - {operation},{n1},{n2} = {result}\n')
except PermissionError as e:
	# TODO: logging
    print(str(e))
    sys.exit(1)