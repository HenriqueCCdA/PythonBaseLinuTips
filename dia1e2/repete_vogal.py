"""
Repete vogais

Faça um programa que pede ao usário que digite uma ou mais palavras e imprime
cada uma das palavras com suas vogais duplicadas.

ex:
python repete_vogal.py

'Digite um palavra:' Python
'Digite um palavra:' Bruno
'Digite um palavra:' <enter>
Pythoon
Bruunoo
"""

words = []
while True:
    word = input("Digite uma palavra (ou enter para sair):").strip()

    if not word:
        break

    final_word = ""
    for letter in word:
        # TODO: Remover acentuação usando função
        if letter.lower() in 'aeiou':
            final_word += letter * 2
        else:
            final_word += letter

    words.append(final_word)

print(*words, sep='\n')
