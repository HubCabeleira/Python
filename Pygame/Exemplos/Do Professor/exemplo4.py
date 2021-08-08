import pygame

# Variáveis globais que serão úteis durante a construção do programa
DIMENSAO_TELA = (600, 450)

# Variáveis das cores. Só lembrando que as cores são no formato RGB (Red-Green-Blue)
# Onde o R, o G e o B são representados númericamente com valores de 0 a 255.
AZUL = (154, 209, 252)
VERDE = (111, 242, 155)
VERMELHO = (255, 0, 0)
MARROM = (150, 75, 0)
BRANCO = (255, 255, 255)

def principal():
    # inicia o pygma
    pygame.init()

    # Cria a nossa tela onde iremos colar superficies através do objeto Surface e desenhar objetos através
    # do objeto Rect.
    tela = pygame.display.set_mode(DIMENSAO_TELA)

    # Define o título que aparecerá na nossa janela.
    pygame.display.set_caption('Exemplo Pygame 921A')

    # Cria o objeto que será responsável por definir os frames que irão animar nossos objetos por segundo.
    """"
    Só lembrando:
    
        Por trás de toda a ação e do movimento que você vê em qualquer tipo de vídeo, 
        incluindo nos games, existe um truque que transforma imagens paradas em imagens animadas. 
        A ilusão que nosso cérebro interpreta como movimento é feita exibindo-se vários quadros 
        consecutivos em um curto período de tempo. Estes quadros são chamados de frames. 
    """
    relogio = pygame.time.Clock()

    sup = pygame.Surface((200, 200))
    sup.fill(VERDE)

    quad = pygame.Rect(0, 0, 40, 40)

    ret = pygame.Rect(200, 100, 150, 50)

    fonte_padrao = pygame.font.get_default_font()
    fonte_colidiu = pygame.font.SysFont(fonte_padrao, 45)

    executando = True

    while executando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                executando = False

            if evento.type == pygame.MOUSEBUTTONDOWN:
              # quad = quad.move(10, 10)
                pygame.mouse.set_pos(10, 10)
            #
            # if evento.type == pygame.MOUSEMOTION:
            #   quad = quad.move(-2, -2)

            # if evento.type == pygame.KEYDOWN:
            #   if evento.key == pygame.K_RIGHT:
            #     quad.move_ip(10, 0)
            #
            #   if evento.key == pygame.K_LEFT:
            #     quad.move_ip(-10, 0)
            #
            #   if evento.key == pygame.K_DOWN:
            #     quad.move_ip(0, 10)
            #
            #   if evento.key == pygame.K_UP:
            #     quad.move_ip(0, -10)
            #
            #   if evento.key == pygame.K_SPACE:
            #     quad.move_ip(10, 10)
            #
            #   if evento.key == pygame.K_BACKSPACE:
            #     quad.move_ip(-10, -10)

        # Aqui dizemos pro nosso objeto relógio quantos frames o programa usará por segundo para animar os objetos.
        # Nesse caso eu defini 30.
        relogio.tick(30)
        tela.fill(AZUL)
        tela.blit(sup, (250, 200))

        qx_anterior, qy_anterior = quad.left, quad.top

        quad.left, quad.top = pygame.mouse.get_pos()

        quad.left -= quad.width / 2
        quad.top -= quad.height / 2

        if quad.colliderect(ret):
          texto_colidiu = fonte_colidiu.render('COLIDIU!', 1, BRANCO)
          tela.blit(texto_colidiu, (200, 250))
          quad.left, quad.top = qx_anterior, qy_anterior


        if quad.top > 420:
          texto_colidiu = fonte_colidiu.render('COLIDIU!', 1, BRANCO)
          tela.blit(texto_colidiu, (200, 250))
          quad.left, quad.top = qx_anterior, qy_anterior

        pygame.draw.rect(tela, VERMELHO, quad)
        pygame.draw.rect(tela, MARROM, ret)

        pygame.display.update()

    pygame.quit()


principal()