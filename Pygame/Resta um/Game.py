import pygame

def Imagens():

    global Peças, Ícone, Fundos, Ícone, Verificáveis, Movida

    Ícone = pygame.image.load("Ícone.jpg")

    Fundo1 = pygame.image.load("Fundo1.jpg")
    Fundo2 = pygame.image.load("Fundo2.jpg")
    Fundo3 = pygame.image.load("Fundo3.jpg")

    Peça1 = {"Obj": pygame.Rect(185, 35, 75, 75), "Imagem": pygame.image.load('Peça1.jpg')}
    Peça2 = {"Obj": pygame.Rect(260, 35, 75, 75), "Imagem": pygame.image.load('Peça1.jpg')}
    Peça3 = {"Obj": pygame.Rect(335, 35, 75, 75), "Imagem": pygame.image.load('Peça1.jpg')}

    Peça4 = {"Obj": pygame.Rect(185, 110, 75, 75), "Imagem": pygame.image.load('Peça1.jpg')}
    Peça5 = {"Obj": pygame.Rect(260, 110, 75, 75), "Imagem": pygame.image.load('Peça1.jpg')}
    Peça6 = {"Obj": pygame.Rect(335, 110, 75, 75), "Imagem": pygame.image.load('Peça1.jpg')}

    Peça7 = {"Obj": pygame.Rect(35, 185, 75, 75), "Imagem": pygame.image.load('Peça1.jpg')}
    Peça8 = {"Obj": pygame.Rect(110, 185, 75, 75), "Imagem": pygame.image.load('Peça1.jpg')}
    Peça9 = {"Obj": pygame.Rect(185, 185, 75, 75), "Imagem": pygame.image.load('Peça1.jpg')}
    Peça10 = {"Obj": pygame.Rect(260, 185, 75, 75), "Imagem": pygame.image.load('Peça1.jpg')}
    Peça11 = {"Obj": pygame.Rect(335, 185, 75, 75), "Imagem": pygame.image.load('Peça1.jpg')}
    Peça12 = {"Obj": pygame.Rect(410, 185, 75, 75), "Imagem": pygame.image.load('Peça1.jpg')}
    Peça13 = {"Obj": pygame.Rect(485, 185, 75, 75), "Imagem": pygame.image.load('Peça1.jpg')}

    Peça14 = {"Obj": pygame.Rect(35, 260, 75, 75), "Imagem": pygame.image.load('Peça1.jpg')}
    Peça15 = {"Obj": pygame.Rect(110, 260, 75, 75), "Imagem": pygame.image.load('Peça1.jpg')}
    Peça16 = {"Obj": pygame.Rect(185, 260, 75, 75), "Imagem": pygame.image.load('Peça1.jpg')}
    Peça17 = {"Obj": pygame.Rect(335, 260, 75, 75), "Imagem": pygame.image.load('Peça1.jpg')}
    Peça18 = {"Obj": pygame.Rect(410, 260, 75, 75), "Imagem": pygame.image.load('Peça1.jpg')}
    Peça19 = {"Obj": pygame.Rect(485, 260, 75, 75), "Imagem": pygame.image.load('Peça1.jpg')}

    Peça20 = {"Obj": pygame.Rect(35, 335, 75, 75), "Imagem": pygame.image.load('Peça1.jpg')}
    Peça21 = {"Obj": pygame.Rect(110, 335, 75, 75), "Imagem": pygame.image.load('Peça1.jpg')}
    Peça22 = {"Obj": pygame.Rect(185, 335, 75, 75), "Imagem": pygame.image.load('Peça1.jpg')}
    Peça23 = {"Obj": pygame.Rect(260, 335, 75, 75), "Imagem": pygame.image.load('Peça1.jpg')}
    Peça24 = {"Obj": pygame.Rect(335, 335, 75, 75), "Imagem": pygame.image.load('Peça1.jpg')}
    Peça25 = {"Obj": pygame.Rect(410, 335, 75, 75), "Imagem": pygame.image.load('Peça1.jpg')}
    Peça26 = {"Obj": pygame.Rect(485, 335, 75, 75), "Imagem": pygame.image.load('Peça1.jpg')}

    Peça27 = {"Obj": pygame.Rect(185, 410, 75, 75), "Imagem": pygame.image.load('Peça1.jpg')}
    Peça28 = {"Obj": pygame.Rect(260, 410, 75, 75), "Imagem": pygame.image.load('Peça1.jpg')}
    Peça29 = {"Obj": pygame.Rect(335, 410, 75, 75), "Imagem": pygame.image.load('Peça1.jpg')}

    Peça30 = {"Obj": pygame.Rect(185, 485, 75, 75), "Imagem": pygame.image.load('Peça1.jpg')}
    Peça31 = {"Obj": pygame.Rect(260, 485, 75, 75), "Imagem": pygame.image.load('Peça1.jpg')}
    Peça32 = {"Obj": pygame.Rect(335, 485, 75, 75), "Imagem": pygame.image.load('Peça1.jpg')}


    Peças = [Peça1, Peça2, Peça3, Peça4, Peça5, Peça6, Peça7, Peça8, Peça9, Peça10, Peça11, Peça12, Peça13, Peça14, Peça15, Peça16, Peça17, Peça18, Peça19, Peça20, Peça21, Peça22, Peça23, Peça24, Peça25, Peça26, Peça27, Peça28, Peça29, Peça30, Peça31, Peça32]
    Fundos = [Fundo1, Fundo2, Fundo3]
    Verificáveis = Peças.copy()
    Movida = []


def Sons():
    global Jogada
    Jogada = pygame.mixer.Sound('Jogada.wav')
    pygame.mixer.music.load('Plano de Fundo.mp3')
    pygame.mixer.music.play(-1, 0.0)


def Seleção():
    global Selecionada
    for Peça in Peças.copy():
        if pygame.mouse.get_pos()[0] >= (Peça["Obj"][0]) and pygame.mouse.get_pos()[0] <= ((Peça["Obj"][0])+75):
            if pygame.mouse.get_pos()[1] >= (Peça["Obj"][1]) and pygame.mouse.get_pos()[1] <= ((Peça["Obj"][1])+70):
                Selecionada = Peça.copy()
                Movida.append(Peça)



def Movimento(Direção,Selecionada,Música, Movida):

    if Direção == "Cima" or Direção == "Baixo" or Direção == "Direita" or Direção == "Esquerda":
        if Música:
            Jogada.play()

    for Peça in Peças.copy():

        if Direção == "Cima":
            Selecionada['Obj'].y -= Selecionada['Obj'].height
            if Peça['Obj'].contains(Selecionada['Obj']):
                Selecionada['Obj'].y -= Selecionada['Obj'].height
                if Peça['Obj'].contains(Selecionada['Obj']):
                    Selecionada['Obj'].y += (Selecionada['Obj'].height) * 2
                else:
                    Limite(Peça, Verificáveis, Direção, Movida)
                    if Válida == True:
                        Peças.remove(Peça)
                        Direção = False
                    else:
                        Selecionada['Obj'].y += (Selecionada['Obj'].height) * 2
            else:
                Selecionada['Obj'].y += Selecionada['Obj'].height

        if Direção == "Baixo":
            Selecionada['Obj'].y += Selecionada['Obj'].height
            if Peça['Obj'].contains(Selecionada['Obj']):
                Selecionada['Obj'].y += Selecionada['Obj'].height
                if Peça['Obj'].contains(Selecionada['Obj']):
                    Selecionada['Obj'].y -= (Selecionada['Obj'].height)*2
                else:
                    Limite(Peça, Verificáveis, Direção, Movida)
                    if Válida == True:
                        Peças.remove(Peça)
                        Direção = False
                    else:
                        Selecionada['Obj'].y -= (Selecionada['Obj'].height) * 2
            else:
                Selecionada['Obj'].y -= Selecionada['Obj'].height

        if Direção == "Direita":
            Selecionada['Obj'].x -= Selecionada['Obj'].height
            if Peça['Obj'].contains(Selecionada['Obj']):
                Selecionada['Obj'].x -= Selecionada['Obj'].height
                if Peça['Obj'].contains(Selecionada['Obj']):
                    Selecionada['Obj'].x += (Selecionada['Obj'].height)*2
                else:
                    Limite(Peça, Verificáveis, Direção, Movida)
                    if Válida == True:
                        Peças.remove(Peça)
                        Direção = False
                    else:
                        Selecionada['Obj'].x += (Selecionada['Obj'].height) * 2
            else:
                Selecionada['Obj'].x += Selecionada['Obj'].height

        if Direção == "Esquerda":
            Selecionada['Obj'].x += Selecionada['Obj'].height
            if Peça['Obj'].contains(Selecionada['Obj']):
                Selecionada['Obj'].x += Selecionada['Obj'].height
                if Peça['Obj'].contains(Selecionada['Obj']):
                   Selecionada['Obj'].x -= (Selecionada['Obj'].height)*2
                else:
                   Limite(Peça, Verificáveis, Direção, Movida)
                   if Válida == True:
                       Peças.remove(Peça)
                       Direção = False
                   else:
                       Selecionada['Obj'].x -= (Selecionada['Obj'].height) * 2
            else:
                Selecionada['Obj'].x -= Selecionada['Obj'].height


def Limite(Peça, Verificáveis, Direção, Movida):
    global Válida
    Válida = True
    if Direção == "Cima":
        if Peça == Verificáveis[0] or Peça == Verificáveis[1] or Peça == Verificáveis[2]:
            Válida = False
        if Peça == Verificáveis[3] or Peça == Verificáveis[5]:
            Válida = False
        if Peça == Verificáveis[6] or Peça == Verificáveis[7] or Peça == Verificáveis[11] or Peça == Verificáveis[12]:
            Válida = False
    elif Direção == "Direita":
        if Peça == Verificáveis[0] or Peça == Verificáveis[3]:
            Válida = False
        if Peça == Verificáveis[6] or Peça == Verificáveis[13] or Peça == Verificáveis[19]:
            Válida = False
        if Peça == Verificáveis[26] or Peça == Verificáveis[29]:
            Válida = False
    elif Direção == "Esquerda":
        if Peça == Verificáveis[2] or Peça == Verificáveis[5]:
            Válida = False
        if Peça == Verificáveis[12] or Peça == Verificáveis[18] or Peça == Verificáveis[25]:
            Válida = False
        if Peça == Verificáveis[28] or Peça == Verificáveis[31]:
            Válida = False
    elif Direção == "Baixo":
        if Peça == Verificáveis[19] or Peça == Verificáveis[20]:
            Válida = False
        if Peça == Verificáveis[29] or Peça == Verificáveis[30] or Peça == Verificáveis[31]:
            Válida = False
        if Peça == Verificáveis[24] or Peça == Verificáveis[25]:
            Válida = False
    if Peça in Movida:
        Válida = True

def Execultando():
    pygame.init()
    Relógio = pygame.time.Clock()
    Janela = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Resta um")
    Imagens()
    pygame.display.set_icon(Ícone)
    Sons()
    Aberto = True
    Música = True
    Jogadas = 0
    Carregando = False
    while Aberto:
        for Evento in pygame.event.get():
            if Evento.type == pygame.QUIT:
                Aberto = False
            Pressionado= pygame.mouse.get_pressed()
            if Pressionado[0] == True:
                Seleção()
            if Evento.type == pygame.KEYDOWN:
                if Evento.key == pygame.K_SPACE:
                    if Música:
                        pygame.mixer.music.stop()
                        Música = False
                    else:
                        pygame.mixer.music.play()
                        Música = True
                Direção = False
                if Evento.key == pygame.K_w:
                    Direção = "Cima"
                    Jogadas += 1
                if Evento.key == pygame.K_s:
                    Direção = "Baixo"
                    Jogadas += 1
                if Evento.key == pygame.K_a:
                    Direção = "Direita"
                    Jogadas += 1
                if Evento.key == pygame.K_d:
                    Direção = "Esquerda"
                    Jogadas += 1
                Movimento(Direção, Selecionada, Música, Movida)
            if Carregando == False:
                pygame.time.set_timer(pygame.USEREVENT + 1, 3000)
                if Evento.type == pygame.USEREVENT + 1:
                    pygame.time.set_timer(pygame.USEREVENT + 1, 0)
                    Carregando = True
        Janela.blit(Fundos[1], (0, 0))
        for Peça in Peças.copy():
            Janela.blit(Peça['Imagem'], Peça['Obj'])
        if len(Peças) == 1:
            Janela.blit(Fundos[2], (0, 0))
            Estilo = pygame.font.get_default_font()
            FonteA = pygame.font.SysFont(Estilo, 75)
            FonteB = pygame.font.SysFont(Estilo, 40)
            ConteúdoA = ("Você Venceu!")
            ConteúdoB = (f"Quantidade de jogadas: { Jogadas } !")
            TextoA = FonteA.render((ConteúdoA), 1, (255, 148, 7))
            TextoB = FonteB.render((ConteúdoB), 1, (255, 148, 7))
            Janela.blit(TextoA, (120, 320))
            Janela.blit(TextoB, (110, 380))
        if Carregando == 0:
            Janela.blit(Fundos[0], (0, 0))
            Carregando = False
        pygame.display.update()
        Relógio.tick(40)
    pygame.quit()


Execultando()




