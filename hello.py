#!/usr/bin/env python3

"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente o programa exibe a mensagem 
correspondente.

Como user:

Tenha a variável LANG devidamente configurada ex:

	export LANG=pt_BR

Execução:

	python hello.py
	ou
	./hello.py
"""
__version__ = '0.1.2'
__author__ = 'Henrique de Andrade'
__license__ = 'Unlicense'

import os

current_language = os.getenv('LANG', 'en_US')[:5]

msg = {
    'en_US': 'Hello, World!',
    'pt_BR': 'Olá, Mundo!',
    'it_IT': 'Ciao, Mondo!',
    'es_SP': 'Hola, Mundo!',
    'fr_FR': 'Bonjour, Monde!',
}

print(msg[current_language])
