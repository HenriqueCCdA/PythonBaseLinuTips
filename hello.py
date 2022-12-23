#!/usr/bin/env python3

"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente o programa exibe a mensagem 
correspondente.

Como user:

Tenha a variável LANG devidamente configurada ex:

	export LANG=pt_BR

Ou informe atraves do CLI argument `--lang`


Execução:

	python hello.py
	ou
	./hello.py
"""
__version__ = '0.1.3'
__author__ = 'Henrique de Andrade'
__license__ = 'Unlicense'

import os
import sys

arguments = {'lang': None, 'count': 1}

for arg in sys.argv[1:]:
	try:
		key, value = arg.split('=')
	except ValueError as e:
		# TODO: Logging
		print(f'[ERROR] {str(e)}')
		print('You need to use `=`')
		print(f'You passed {arg}')
		print('try with --key=value')
		sys.exit(1)
		
	key = key.lstrip('-').strip()
	value = value.strip()

	#Validacao
	if key not in arguments:
		print(f'Invalid Option `{key}`')
		sys.exit(1)
	
	arguments[key] = value

current_language = arguments['lang']
if current_language is None:
	# TODO: User repetição
	if "LANG" in os.environ:
		current_language = os.getenv('LANG') 
	else:
		current_language = input('Chosse a language:')
	
current_language = current_language[:5]

msg = {
    'en_US': 'Hello, World!',
    'pt_BR': 'Olá, Mundo!',
    'it_IT': 'Ciao, Mondo!',
    'es_ES': 'Hola, Mundo!',
    'fr_FR': 'Bonjour, Monde!',
}

try:
	message = msg[current_language]
except KeyError as e:
	print(f'[ERROR] {str(e)}')
	print(f'Language is invalid, choose from: {list(msg.keys())}')
	sys.exit(1)

# message = msg.get(current_language, msg['en_US'])

print(message * int(arguments['count']))
