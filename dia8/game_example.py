from multiprocessing.connection import wait
from operator import truediv
import os
import random
import pygame as pg
import pygame.locals as keys


DIR = os.path.abspath(os.path.dirname(__file__))
TAMANHO_JANELA = (800, 800)
#        R, G, B
VERDE = ( 0, 100, 0)
CINZA = ( 100, 100, 100)
AMARELO = (255, 240, 60)
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)


largura, altura = TAMANHO_JANELA
largura_estrada =  int(largura / 1.6)
largura_separador = int(largura / 200)
lado_direito = largura / 2 + largura_estrada / 4
lado_esquerdo = largura / 2 - largura_estrada / 4

pg.init()
pg.display.set_caption("Catch a Beer")
tela = pg.display.set_mode(TAMANHO_JANELA)
tela.fill(VERDE)
pg.display.update()

# Fonte
letra = pg.font.SysFont("Comic Sans MS", 30)
letra_grande = pg.font.SysFont("Comic Sans MS", 90)

# Jogador
jogador = pg.image.load(os.path.join(DIR, "player", "player.png"))
jogador = pg.transform.scale(jogador, (150, 150))
posicao_do_jogador = jogador.get_rect()
posicao_do_jogador.center = lado_direito, altura * 0.8


def carrega_cerveja_aleatoria():
    i = random.randint(1, 5)
    cerveja = pg.image.load(os.path.join(DIR, "beers", f"{i}.png"))
    cerveja = pg.transform.scale(cerveja, (100, 100))
    posicao_do_cerveja = cerveja.get_rect()
    if random.randint(0, 1):
        posicao_do_cerveja.center = lado_direito, altura * 0.2
    else:
        posicao_do_cerveja.center = lado_esquerdo, altura * 0.2

    return cerveja, posicao_do_cerveja


cerveja, posicao_da_cerveja = carrega_cerveja_aleatoria()


executanto = True
velocidade = 1
bebeu = 0
perdeu = 0

while executanto:
    # determina o estado do jogo no loop

    # colission detection
    if (
        10 < (posicao_do_jogador[1] - posicao_da_cerveja[1]) < 50
        and posicao_do_jogador[0] == posicao_da_cerveja[0] - 25
    ):
        bebeu += 1
        sound = pg.mixer.music.load(os.path.join(DIR, "sound", "sensacional.mp3"))
        cerveja, posicao_da_cerveja = carrega_cerveja_aleatoria()
        pg.mixer.music.play(0)

    posicao_da_cerveja[1] += velocidade

    # captura eventos
    for event in pg.event.get():
        if event.type == keys.QUIT:
            executanto = False

        elif event.type == keys.KEYDOWN:
            if event.key in (keys.K_a, keys.K_LEFT):
                posicao_do_jogador = posicao_do_jogador.move(
                    (-int(largura_estrada / 2), 0)
                )
            if event.key in (keys.K_d, keys.K_RIGHT):
                posicao_do_jogador = posicao_do_jogador.move(
                    (int(largura_estrada / 2), 0)
                )
    # Desenha
    # Estrada
    pg.draw.rect(
        tela,
        CINZA,
        (
            largura / 2 - largura_estrada / 2,
            0,
            largura_estrada,
            altura
        ),
    )

    # Separador
    pg.draw.rect(
        tela,
        AMARELO,
        (
            largura / 2 - largura_separador / 2,
            0,
            largura_separador,
            altura
        ),
    )

    # Bordas
    pg.draw.rect(
        tela,
        BRANCO,
        (
            largura / 2 - largura_estrada / 2 + largura_separador * 2,
            0,
            largura_separador,
            altura
        ),
    )

    pg.draw.rect(
        tela,
        BRANCO,
        (
            largura / 2 + largura_estrada / 2 - largura_separador * 2,
            0,
            largura_separador,
            altura
        ),
    )

    titulo = letra.render(
        f"Carch a beer! bebeu: {bebeu} vacilou: {perdeu}", True, BRANCO, PRETO
    )
    tela.blit(titulo, (largura / 5, 0))
    tela.blit(jogador, posicao_do_jogador)
    tela.blit(cerveja, posicao_da_cerveja)

    pg.display.update()

    # calcula o resultado final do loop
    if posicao_da_cerveja[1] > altura:
        perdeu += 1
        cerveja, posicao_da_cerveja = carrega_cerveja_aleatoria()

    if perdeu > 3:

        sound = pg.mixer.music.load(os.path.join(DIR, "sound", "zika.mp3"))
        cerveja, posicao_da_cerveja = carrega_cerveja_aleatoria()
        pg.mixer.music.play(0)

        msg = letra_grande.render("GAME_OVER", True, AMARELO, PRETO)
        tela.blit(msg, (largura / 4, 100))
        pg.display.update()
        wait_key = True
        while wait_key:
            for event in pg.event.get():
                if event.type == keys.KEYDOWN:
                    wait_key = False
        break

pg.quit()
