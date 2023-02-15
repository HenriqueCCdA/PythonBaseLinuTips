"""Filtra palavras que contem  5 letras
e remove os acentos
"""

import unicodedata

def tira_acento(s):
    return unicodedata.normalize("NFD", s).encode("ascii", "ignore").decode("utf-8")


original = open("br-utf8.txt").readlines()

with open("palavras.txt", "w") as palavras:
    palavras.write("\n".join(tira_acento(p.strip().upper()) for p in original if len(p.strip()) == 5))
