import pygame
from random import randint
from pygame.locals import *

#iniciando o pygame
pygame.init()

#defidindo as propriedades da tela

tela = pygame.display
tamanho_tela = tela.set_mode((500,500))
tela.set_caption("Jogo da cobrinha")

#definir as posicoes da cobrinha

cobrinha = [(150, 150), (150, 160), (150, 170)]

#definir as posicoes iniciais da comida

comida = pygame.Surface((10, 10))
comida.fill((0, 168, 107))

#definindo as possiveis direcoes da cobrinha

direita = 1
esquerda = 3
cima = 0
baixo = 2

#definir a direção inicial da cobrinha

direcao = direita

#defindindo as propriedades da cobrinha

preenchimento_cobrinha = pygame.Surface((10, 10))
preenchimento_cobrinha.fill((25, 140, 255))

#definindo as posicoes da comida

def posicaoDaComida():
    return (randint(0, 490)//10*10, randint(0, 490)//10*10)
posicaoComida = posicaoDaComida()

#funlção para verificar se a cobra comeu a comida

def comeu(posicao1, posicao2):
    return (posicao1[1] == posicao2[1] and posicao1[0] == posicao2[0])

#definindo o tempo de atualização

tempo = pygame.time.Clock()

#trabalhando com as atualizações da tela

while 1==1:
    tempo.tick(20)
    for evento in pygame.event.get():
        if evento.type == QUIT:

            #fechando o jogo
            
            pygame.quit()

    #definindo as condições para apertos das teclas

        if evento.type == KEYDOWN:
                if evento.key == K_LEFT:    
                    direcao = esquerda
                if evento.key == K_RIGHT:
                    direcao = direita
                if evento.key == K_UP:
                    direcao = cima
                if evento.key == K_DOWN:
                    direcao = baixo

    #verificando se a cobra comeu a comida

    if comeu(posicaoComida, cobrinha[0]):
        cobrinha.append((0, 0))
        posicaoComida = posicaoDaComida()

    #definindo as condições para diferentes direções

    for i in range(len(cobrinha) - 1, 0, -1):
        cobrinha[i] = (cobrinha[i-1][0], cobrinha[i-1][1])

    if direcao == direita:
        cobrinha[0] = (cobrinha[0][0] + 10, cobrinha[0][1])
    if direcao == esquerda:
        cobrinha[0] = (cobrinha[0][0] - 10, cobrinha[0][1])
    if direcao == cima:
        cobrinha[0] = (cobrinha[0][0], cobrinha[0][1] - 10)
    if direcao == baixo:
        cobrinha[0] = (cobrinha[0][0], cobrinha[0][1] + 10)
        
    #limpando a tela para desenhar a cobrinha na

    tamanho_tela.fill((0, 0, 0))

    #desenhando a comida da cobrinha
    
    tamanho_tela.blit(comida, posicaoComida)

    #desenhando a cobrinha na posicao inicial
    
    for quadradinho in cobrinha:
        tamanho_tela.blit(preenchimento_cobrinha, quadradinho)

    #atualizando a tela

    tela.update()
