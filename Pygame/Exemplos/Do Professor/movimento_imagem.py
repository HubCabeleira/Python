""""

Este programa visa carregar uma imagem e associá-la a um objeto que será desenhado na tela. A idéia aqui é fazer com
que este objeto se movimente na tela aleatoriamente.

"""

import pygame

VERMELHO = 255, 0, 0
BRANCO = 255, 255, 255
DIMENSAO_TELA = 600, 450

# Função para mover a figura (objeto com a imagem da bola)
def mover(figura):
    borda_esquerda = 0
    borda_superior = 0
    borda_direita = DIMENSAO_TELA[0]
    borda_inferior = DIMENSAO_TELA[1]

    # Verifica se o objeto atingiu a borda esquerda ou direta
    if figura['obj'].top < borda_superior or figura['obj'].bottom > borda_inferior:
        # Quando atingir a borda direita, significa que o X do objeto é positivo, então iremos negativá-lo para retornar a esquerda.
        # Quando atingir a borda esquerda, significa que o X do objeto é negativo, então iremos negativá-lo (e torná-lo positivo) para retornar a direita.
        figura['vel'][1] = -figura['vel'][1]

    # Verifica se o objeto atingiu a borda inferior ou superior
    if figura['obj'].left < borda_esquerda or figura['obj'].right > borda_direita:
        # Quando atingir a borda inferior, significa que o Y do objeto é positivo, então iremos negativá-lo para retornar para cima.
        # Quando atingir a borda superior, significa que o Y do objeto é negativo, então iremos negativá-lo (e torná-lo positivo) para retornar para baixo.
        figura['vel'][0] = -figura['vel'][0]

    # Aqui as coordenadas do objeto serão atualizadas de acordo com os valores definidos acima
    figura['obj'].x += figura['vel'][0]
    figura['obj'].y += figura['vel'][1]



def principal():
    pygame.init()

    # Definie a tela do programa
    tela = pygame.display.set_mode(DIMENSAO_TELA)

    # Cria o objeto relógio para manipular os frames
    relogio = pygame.time.Clock()

    # Carrega uma uma imagem como superfície
    bola = pygame.image.load('ball.png')
    # Transforma a imagem em um objeto retangulo que poderá ser manipulado
    bola_sup = bola.get_rect()

    # Dicionário da figura (Bola) com o objeto que será desenhado na tela suas coordenadas que serão utilizados como
    # valocidade para animar o objeto pelos frames
    figura1 = {'obj': bola_sup, 'vel': [30, 30]}

    # Cria uma lista de figuras para poder manipula-las e reutilizar código
    figuras = [figura1]

    executando = True

    while executando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                executando = False

        # Define os frames(quadros) por segundo que irá animar os objetos na tela
        relogio.tick(30)
        tela.fill(BRANCO)

        # Percorre a lista de figuras
        for fig in figuras:
            # Chama a função de mover e passamos o dicionário da figura
            mover(fig)

            # Como uma imagem no pygame é uma superfíce e nao um objeto Rect, precisamos colar essa imagem (bola) no
            # objeto rect que será desenhado na tela
            tela.blit(bola, fig['obj'])

        pygame.display.update()

    pygame.quit()


principal()