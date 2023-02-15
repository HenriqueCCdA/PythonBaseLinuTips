import os
import random
from rich.prompt import Prompt
from rich.console import Console

EMOJIS = {
    "posicao_correta": "🟩",
    "letra_correta": "🟧",
    "letra_errada": "⬜"
}



DIR = os.path.abspath(os.path.dirname(__file__))

def posicao_correta(letra):
    return f"[black on green]{letra}[/]"

def letra_correta(letra):
    return f"[black on yellow]{letra}[/]"

def letra_errada(letra):
    return f"[black on white]{letra}[/]"

MESSAGEM = (
    posicao_correta("Boas vindas ") +
    letra_correta("ao ") +
    letra_errada("Pylavras!")
)

INSTRUCAO = "Adivinhe a palavra de 5 letras.\n"



palavra_correta = random.choice(open(os.path.join(DIR,  "palavras.txt")).readlines()).strip().upper()

tenativas = 6
rodadas = 0

console = Console()
console.print(MESSAGEM)
console.print(INSTRUCAO)


def computa_tentativa(tentativa):
    acertos = []
    emojis = []
    for i, letra in enumerate(tentativa):
        if tentativa[i] == palavra_correta[i]:
            acertos += posicao_correta(letra)
            emojis.append(EMOJIS['posicao_correta'])
        elif letra in palavra_correta:
            acertos += letra_correta(letra)
            emojis.append(EMOJIS['letra_correta'])
        else:
            acertos += letra_errada(letra)
            emojis.append(EMOJIS['letra_errada'])

    return "".join(acertos), "".join(emojis)

print(palavra_correta)
acertados = []
todo_os_emojis = []
while rodadas < tenativas:
    tenativa = Prompt.ask("Digite [green]5[/] letras.").strip().upper()
    if len(tenativa) != 5:
        console.print("Erro: Digite exatamente [red]5[/] letras.")
        continue
    rodadas += 1

    # calcula
    acertos, emojis = computa_tentativa(tenativa)
    todo_os_emojis.append(emojis)
    acertados.append(acertos)
    console.clear()

    for acerto in acertados:
        console.print(acerto)

    if tenativa == palavra_correta:
        break

console.print(f"Pylavras: {rodadas}/{tenativas}\n")
for item in todo_os_emojis:
    console.print(item)
