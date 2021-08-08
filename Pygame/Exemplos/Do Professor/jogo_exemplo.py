import pygame

# Variáveis globais de configuração
BRANCO = (255,255,255)
AMARELO = (255,255,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
VERMELHO = (255,0,0)
MARROM = (150,75,0)

dimensão_janela = (600, 450)

def cria_retangulos():
    ret1 = {'obj': pygame.Rect(10, 30, 560, 30), 'cor': VERMELHO}
    # ret2 = {'obj': pygame.Rect(30, 90, 560, 30), 'cor': VERMELHO}
    # ret3 = {'obj': pygame.Rect(10, 150, 560, 30), 'cor': VERMELHO}
    # ret4 = {'obj': pygame.Rect(30, 210, 560, 30), 'cor': VERMELHO}
    # ret5 = {'obj': pygame.Rect(10, 270, 560, 30), 'cor': VERMELHO}
    # ret6 = {'obj': pygame.Rect(30, 330, 560, 30), 'cor': VERMELHO}
    # ret7 = {'obj': pygame.Rect(10, 390, 560, 30), 'cor': VERMELHO}

    #return ret1, ret2, ret3, ret4, ret5, ret6, ret7
    return ret1,


def principal():
    pygame.init()
    
    tela = pygame.display.set_mode(dimensão_janela)
    pygame.display.set_caption('Jogo Exemplo')
    relogio = pygame.time.Clock()

    retangulos = cria_retangulos()

    # objeto de interação do jogo
    quad = pygame.Rect(10, 5, 20, 20)

    pygame.font.init()
    
    fonte_padrão = pygame.font.get_default_font()
    fonte_perdeu = pygame.font.SysFont(fonte_padrão, 45)
    fonte_ganhou = pygame.font.SysFont(fonte_padrão, 30)

    executando = True

    while executando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                executando = False

            if evento.type == pygame.MOUSEBUTTONDOWN:
                pygame.mouse.set_pos(15, 12)
                principal()

        tela.fill(AZUL)
        relogio.tick(30)

        # pega a posição do quadrado permitindo movimento com o mouse
        (x_anterior, y_anterior) = (quad.left, quad.top)
        quad.left, quad.top = pygame.mouse.get_pos()
        quad.left -= quad.width / 2
        quad.top -= quad.height / 2

        for retangulo in retangulos:
            # se colidiu com algum retângulo ou alguma borda, reposiciona o objeto 'quad' para o início e exibe mensagem
            if quad.colliderect(retangulo['obj']) or quad.right > 600 or quad.left < 0:
                pygame.mouse.set_pos(15, 12)
                texto_perdeu = fonte_perdeu.render('VOCÊ MORREU!', 1, BRANCO)
                tela.blit(texto_perdeu, (200, 225))
                (quad.left, quad.top) = (x_anterior, y_anterior)

            # verifica se chegou ao final e exibe mensagem de vitória com opcão de clique para recomeçar
            if quad.top > 400:
                texto_ganhou = fonte_ganhou.render('VOCÊ CONSEGUIU!', 1, BRANCO)
                tela.blit(texto_ganhou, (200, 225))
                texto_click = fonte_ganhou.render('Clique para recomeçar', 1, VERMELHO)
                tela.blit(texto_click, (185, 250))
                retangulo['obj'].left = 602

            pygame.draw.rect(tela, retangulo['cor'], retangulo['obj'])

        pygame.draw.rect(tela, AMARELO, quad)
        
        pygame.display.update()

    pygame.quit()


principal()
