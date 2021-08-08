import pygame

Dimensões = (480, 640)
Escolha = False
Inicio = True
Atacou = False
Correu = False
Entrada = False
Caverna = False
Cidade = False
Conjunto = {'0': Escolha, '1': Inicio, '2': Atacou, '3': Correu, '4': Entrada, '5': Caverna, '6': Cidade}



def Arquivos():
    global Fases, Alternativas, Resultados, Marcador, Ícone
    Ícone = pygame.image.load("Ícone.jpg")
    Fase1 = pygame.image.load('Fase 1.jpg')
    Fase2 = pygame.image.load('Fase 2.jpg')
    Fase3 = pygame.image.load('Fase 3.jpg')
    Fase4 = pygame.image.load('Fase 4.jpg')
    Fase5 = pygame.image.load('Fase 5.jpg')
    Fase6 = pygame.image.load('Fase 6.jpg')
    Resultado1 = pygame.image.load('Falha 1.jpg')
    Resultado2 = pygame.image.load('Falha 2.jpg')
    Resultado3 = pygame.image.load('Falha 3.jpg')
    Resultado4 = pygame.image.load('Falha 4.jpg')
    Resultado5 = pygame.image.load('Falha 5.jpg')
    Resultado6 = pygame.image.load('Falha 6.jpg')
    Resultado7 = pygame.image.load('Falha 7.jpg')
    Resultado8 = pygame.image.load('Acerto 1.jpg')
    Resultado9 = pygame.image.load('Acerto 2.jpg')
    Alternativa1 = {'ObjRect': pygame.Rect(75, 390, 23, 30),'Imagem': pygame.image.load('Espaço.jpg')}
    Alternativa2 = {'ObjRect': pygame.Rect(75, 450, 23, 30),'Imagem': pygame.image.load('Espaço.jpg')}
    Alternativa3 = {'ObjRect': pygame.Rect(75, 510, 23, 30),'Imagem': pygame.image.load('Espaço.jpg')}
    Alternativas = [Alternativa1, Alternativa2, Alternativa3]
    Marcador = {'Obj': pygame.Rect(50, 50, 46, 60), 'Imagem': pygame.image.load('Pena.jpg')}
    Fases = [Fase1, Fase2, Fase3, Fase4, Fase5, Fase6]
    Resultados = [Resultado1, Resultado2, Resultado3, Resultado4, Resultado5, Resultado6, Resultado7, Resultado8, Resultado9]


def Músicas():
    pygame.mixer.music.load('Plano de Fundo.mp3')
    pygame.mixer.music.play(-1, 0.0)


def Início(Janela, Alternativas):
    Janela.blit(Fases[0], (0, 0))
    Janela.blit((Alternativas[0])['Imagem'], (Alternativas[0])['ObjRect'])
    Janela.blit((Alternativas[1])['Imagem'], (Alternativas[1])['ObjRect'])
    Janela.blit((Alternativas[2])['Imagem'], (Alternativas[2])['ObjRect'])
    if Conjunto['0'] == 'A':
        Conjunto['2'] = True
        Conjunto['0'] = False
    elif Conjunto['0'] == 'B':
        Janela.blit(Resultados[0], (0, 0))
    elif Conjunto['0'] == 'C':
        Conjunto['3'] = True
        Conjunto['0'] = False


def Ataque(Janela, Alternativas):
    Conjunto['1'] = False
    Janela.blit(Fases[1], (0, 0))
    Janela.blit((Alternativas[0])['Imagem'], (Alternativas[0])['ObjRect'])
    Janela.blit((Alternativas[1])['Imagem'], (Alternativas[1])['ObjRect'])
    Janela.blit((Alternativas[2])['Imagem'], (Alternativas[2])['ObjRect'])
    if Conjunto['0'] == 'A':
        Conjunto['3'] = True
        Conjunto['0'] = False
    elif Conjunto['0'] == 'B': Janela.blit(Resultados[1], (0, 0))
    elif Conjunto['0'] == 'C':
        Conjunto['4'] = True
        Conjunto['0'] = False


def Corrida(Janela, Alternativas):
    Conjunto['2'] = False
    Conjunto['5'] = False
    Conjunto['1'] = False
    Janela.blit(Fases[4], (0, 0))
    Janela.blit((Alternativas[0])['Imagem'], (Alternativas[0])['ObjRect'])
    Janela.blit((Alternativas[1])['Imagem'], (Alternativas[1])['ObjRect'])
    Janela.blit((Alternativas[2])['Imagem'], (Alternativas[2])['ObjRect'])
    if Conjunto['0'] == 'A': Janela.blit(Resultados[2], (0, 0))
    elif Conjunto['0'] == 'B': Janela.blit(Resultados[3], (0, 0))
    elif Conjunto['0'] == 'C': Conjunto['6'] = True


def Entrada(Janela, Alternativas):
    Conjunto['2'] = False
    Conjunto['3'] = False
    Janela.blit(Fases[2], (0, 0))
    Janela.blit((Alternativas[0])['Imagem'], (Alternativas[0])['ObjRect'])
    Janela.blit((Alternativas[1])['Imagem'], (Alternativas[1])['ObjRect'])
    if Conjunto['0'] == 'A':
        Conjunto['5'] = True
        Conjunto['0'] = False
    elif Conjunto['0'] == 'B': Janela.blit(Resultados[5], (0, 0))


def Caverna(Janela, Alternativas):
    Conjunto['4'] = False
    Janela.blit(Fases[3], (0,0))
    Janela.blit((Alternativas[0])['Imagem'],(Alternativas[0])['ObjRect'])
    Janela.blit((Alternativas[1])['Imagem'],(Alternativas[1])['ObjRect'])
    Janela.blit((Alternativas[2])['Imagem'],(Alternativas[2])['ObjRect'])
    if Conjunto['0'] == 'A':
        Janela.blit(Resultados[2], (0, 0))
    elif Conjunto['0'] == 'B':
        Janela.blit(Resultados[8], (0, 0))
    elif Conjunto['0'] == 'C':
        Conjunto['3'] = True
        Conjunto['0'] = False



def Cidade(Janela, Alternativas):
    Conjunto['3'] = False
    Conjunto['5'] = False
    Janela.blit(Fases[5], (0, 0))
    Janela.blit((Alternativas[0])['Imagem'], (Alternativas[0])['ObjRect'])
    Janela.blit((Alternativas[1])['Imagem'], (Alternativas[1])['ObjRect'])
    if Conjunto['0'] == 'A':
        Janela.blit(Resultados[7], (0, 0))
    elif Conjunto['0'] == 'B':
        Janela.blit(Resultados[6], (0, 0))



def Execultando():
    global Conjunto
    pygame.init()
    Arquivos()
    Músicas()
    Relógio = pygame.time.Clock()
    Janela = pygame.display.set_mode(Dimensões)
    pygame.display.set_caption("Sonho do Guerreiro")
    pygame.display.set_icon(Ícone)
    Musica = True
    Aberta = True
    while Aberta == True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                Aberta = False
            Esquerdo, Giratório ,Direito = pygame.mouse.get_pressed()
            if Esquerdo == True:
                if (Marcador['Obj'][0])>=(75) and (Marcador['Obj'][0])<=(108) and (Marcador['Obj'][1])>=(390) and (Marcador['Obj'][1])<=(420):
                    Conjunto['0'] = 'A'
                if (Marcador['Obj'][0])>=(75) and (Marcador['Obj'][0])<=(108) and (Marcador['Obj'][1])>=(450) and (Marcador['Obj'][1])<=(470):
                    Conjunto['0'] = 'B'
                if (Marcador['Obj'][0])>=(75) and (Marcador['Obj'][0])<=(108) and (Marcador['Obj'][1])>=(510) and (Marcador['Obj'][1])<=(540):
                    Conjunto['0'] = 'C'
            if Direito == True:
                if Musica:
                    pygame.mixer.music.stop()
                    Musica = False
                else:
                    pygame.mixer.music.play()
                    Musica = True
        if Conjunto['1'] == True:
            Início(Janela, Alternativas)
        if Conjunto['2'] == True:
            Ataque(Janela, Alternativas)
        if Conjunto['3'] == True:
            Corrida(Janela, Alternativas)
        if Conjunto['4'] == True:
            Entrada(Janela, Alternativas)
        if Conjunto['5'] == True:
            Caverna(Janela, Alternativas)
        if Conjunto['6'] == True:
            Cidade(Janela, Alternativas)
        Marcador['Obj'].left, Marcador['Obj'].top = pygame.mouse.get_pos()
        Janela.blit(Marcador['Imagem'], Marcador['Obj'])
        pygame.display.update()
        Relógio.tick(40)

    pygame.quit()

Execultando()


