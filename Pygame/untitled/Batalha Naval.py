import pygame, random;

def Imagem():

    global ConjuntoL, ConjuntoE, Posicionados, Ícone, Fundos

    #Mar

    Peça0 = {"ObjRect": pygame.Rect(75, 110, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça1 = {"ObjRect": pygame.Rect(108, 110, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça2 = {"ObjRect": pygame.Rect(141, 110, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça3 = {"ObjRect": pygame.Rect(173, 110, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça4 = {"ObjRect": pygame.Rect(206, 110, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça5 = {"ObjRect": pygame.Rect(239, 110, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça6 = {"ObjRect": pygame.Rect(272, 110, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça7 = {"ObjRect": pygame.Rect(305, 110, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça8 = {"ObjRect": pygame.Rect(338, 110, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça9 = {"ObjRect": pygame.Rect(371, 110, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}

    Peça10 = {"ObjRect": pygame.Rect(75, 143, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça11 = {"ObjRect": pygame.Rect(108, 143, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça12 = {"ObjRect": pygame.Rect(141, 143, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça13 = {"ObjRect": pygame.Rect(173, 143, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça14 = {"ObjRect": pygame.Rect(206, 143, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça15 = {"ObjRect": pygame.Rect(239, 143, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça16 = {"ObjRect": pygame.Rect(272, 143, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça17 = {"ObjRect": pygame.Rect(305, 143, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça18 = {"ObjRect": pygame.Rect(338, 143, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça19 = {"ObjRect": pygame.Rect(371, 143, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}

    Peça20 = {"ObjRect": pygame.Rect(75, 176, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça21 = {"ObjRect": pygame.Rect(108, 176, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça22 = {"ObjRect": pygame.Rect(141, 176, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça23 = {"ObjRect": pygame.Rect(173, 176, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça24 = {"ObjRect": pygame.Rect(206, 176, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça25 = {"ObjRect": pygame.Rect(239, 176, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça26 = {"ObjRect": pygame.Rect(272, 176, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça27 = {"ObjRect": pygame.Rect(305, 176, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça28 = {"ObjRect": pygame.Rect(338, 176, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça29 = {"ObjRect": pygame.Rect(371, 176, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}

    Peça30 = {"ObjRect": pygame.Rect(75, 209, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça31 = {"ObjRect": pygame.Rect(108, 209, 33, 33 ), "Imagem": pygame.image.load("Onda.jpg")}
    Peça32 = {"ObjRect": pygame.Rect(141, 209, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça33 = {"ObjRect": pygame.Rect(173, 209, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça34 = {"ObjRect": pygame.Rect(206, 209, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça35 = {"ObjRect": pygame.Rect(239, 209, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça36 = {"ObjRect": pygame.Rect(272, 209, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça37 = {"ObjRect": pygame.Rect(305, 209, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça38 = {"ObjRect": pygame.Rect(338, 209, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça39 = {"ObjRect": pygame.Rect(371, 209, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}

    Peça40 = {"ObjRect": pygame.Rect(75, 243, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça41 = {"ObjRect": pygame.Rect(108, 243, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça42 = {"ObjRect": pygame.Rect(141, 243, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça43 = {"ObjRect": pygame.Rect(173, 243, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça44 = {"ObjRect": pygame.Rect(206, 243, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça45 = {"ObjRect": pygame.Rect(239, 243, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça46 = {"ObjRect": pygame.Rect(272, 243, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça47 = {"ObjRect": pygame.Rect(305, 243, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça48 = {"ObjRect": pygame.Rect(338, 243, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça49 = {"ObjRect": pygame.Rect(371, 243, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}

    Peça50 = {"ObjRect": pygame.Rect(75, 276, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça51 = {"ObjRect": pygame.Rect(108, 276, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça52 = {"ObjRect": pygame.Rect(141, 276, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça53 = {"ObjRect": pygame.Rect(173, 276, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça54 = {"ObjRect": pygame.Rect(206, 276, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça55 = {"ObjRect": pygame.Rect(239, 276, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça56 = {"ObjRect": pygame.Rect(272, 276, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça57 = {"ObjRect": pygame.Rect(305, 276, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça58 = {"ObjRect": pygame.Rect(338, 276, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça59 = {"ObjRect": pygame.Rect(371, 276, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}

    Peça60 = {"ObjRect": pygame.Rect(75, 309, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça61 = {"ObjRect": pygame.Rect(108, 309, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça62 = {"ObjRect": pygame.Rect(141, 309, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça63 = {"ObjRect": pygame.Rect(173, 309, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça64 = {"ObjRect": pygame.Rect(206, 309, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça65 = {"ObjRect": pygame.Rect(239, 309, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça66 = {"ObjRect": pygame.Rect(272, 309, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça67 = {"ObjRect": pygame.Rect(305, 309, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça68 = {"ObjRect": pygame.Rect(338, 309, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça69 = {"ObjRect": pygame.Rect(371, 309, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}

    Peça70 = {"ObjRect": pygame.Rect(75, 342, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça71 = {"ObjRect": pygame.Rect(108, 342, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça72 = {"ObjRect": pygame.Rect(141, 342, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça73 = {"ObjRect": pygame.Rect(173, 342, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça74 = {"ObjRect": pygame.Rect(206, 342, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça75 = {"ObjRect": pygame.Rect(239, 342, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça76 = {"ObjRect": pygame.Rect(272, 342, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça77 = {"ObjRect": pygame.Rect(305, 342, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça78 = {"ObjRect": pygame.Rect(338, 342, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}
    Peça79 = {"ObjRect": pygame.Rect(371, 342, 33, 33), "Imagem": pygame.image.load("Onda.jpg")}


    LinhaA = [Peça0, Peça1, Peça2, Peça3, Peça4, Peça5, Peça6, Peça7,Peça8, Peça9]
    LinhaB = [Peça10, Peça11, Peça12, Peça13, Peça14, Peça15, Peça16, Peça17, Peça18, Peça19]
    LinhaC = [Peça20, Peça21, Peça22, Peça23, Peça24, Peça25, Peça26, Peça27, Peça28, Peça29]
    LinhaD = [Peça30, Peça31, Peça32, Peça33, Peça34, Peça35, Peça36, Peça37, Peça38, Peça39]
    LinhaE = [Peça40, Peça41, Peça42, Peça43, Peça44, Peça45, Peça46, Peça47, Peça48, Peça49]
    LinhaF = [Peça50, Peça51, Peça52, Peça53, Peça54, Peça55, Peça56, Peça57, Peça58, Peça59]
    LinhaG = [Peça60, Peça61, Peça62, Peça63, Peça64, Peça65, Peça66, Peça67, Peça68, Peça69]
    LinhaH = [Peça70, Peça71, Peça72, Peça73, Peça74, Peça75, Peça76, Peça77, Peça78, Peça79]

    ConjuntoL = [LinhaA, LinhaB, LinhaC, LinhaD, LinhaE, LinhaF, LinhaG, LinhaH]

    #Navios

    EmbarcaçãoS1 = {"ObjRect": pygame.Rect(0, 0, 33, 33), "Imagem": pygame.image.load("Submarino.jpg")}
    EmbarcaçãoS2 = {"ObjRect": pygame.Rect(0, 0, 33, 33), "Imagem": pygame.image.load("Submarino.jpg")}
    EmbarcaçãoS3 = {"ObjRect": pygame.Rect(0, 0, 33, 33), "Imagem": pygame.image.load("Submarino.jpg")}

    EmbarcaçãoR1 = {"ObjRect": pygame.Rect(0, 0, 33, 33), "Imagem": pygame.image.load("Rebocador(1).jpg")}
    EmbarcaçãoR11 = {"ObjRect": pygame.Rect(0, 0, 33, 33), "Imagem": pygame.image.load("Rebocador(2).jpg")}

    EmbarcaçãoR2 = {"ObjRect": pygame.Rect(0, 0, 33, 33), "Imagem": pygame.image.load("Rebocador(1).jpg")}
    EmbarcaçãoR22 = {"ObjRect": pygame.Rect(0, 0, 33, 33), "Imagem": pygame.image.load("Rebocador(2).jpg")}

    EmbarcaçãoR3 = {"ObjRect": pygame.Rect(0, 0, 33, 33), "Imagem": pygame.image.load("Rebocador(1).jpg")}
    EmbarcaçãoR33 = {"ObjRect": pygame.Rect(0, 0, 33, 33), "Imagem": pygame.image.load("Rebocador(2).jpg")}

    EmbarcaçãoC1 = {"ObjRect": pygame.Rect(0, 0, 33, 33), "Imagem": pygame.image.load("Cruzador (1).jpg")}
    EmbarcaçãoC11 = {"ObjRect": pygame.Rect(0, 0, 33, 33), "Imagem": pygame.image.load("Submarino.jpg")}
    EmbarcaçãoC111 = {"ObjRect": pygame.Rect(0, 0, 33, 33), "Imagem": pygame.image.load("Cruzador (1).jpg")}

    EmbarcaçãoC2 = {"ObjRect": pygame.Rect(0, 0, 33, 33), "Imagem": pygame.image.load("Cruzador (1).jpg")}
    EmbarcaçãoC22 = {"ObjRect": pygame.Rect(0, 0, 33, 33), "Imagem": pygame.image.load("Submarino.jpg")}
    EmbarcaçãoC222 = {"ObjRect": pygame.Rect(0, 0, 33, 33), "Imagem": pygame.image.load("Cruzador (1).jpg")}

    #EmbarcaçãoC11 = {"ObjRect": pygame.Rect(x, y), "Imagem": pygame.load.imaga("A1.jpg")}
    #EmbarcaçãoC111 = {"ObjRect": pygame.Rect(x, y), "Imagem": pygame.load.image("A1.jpg")}

    #EmbarcaçãoC2 = {"ObjRect": pygame.Rect(x, y), "Imagem": pygame.load.image("A1.jpg")}
    #EmbarcaçãoC22 = {"ObjRect": pygame.Rect(x, y), "Imagem": pygame.load.image("A1.jpg")}
    #EmbarcaçãoC333 = {"ObjRect": pygame.Rect(x, y), "Imagem": pygame.load.image("A1.jpg")}

    #EmbarcaçãoP1 = {"ObjRect": pygame.Rect(x, y), "Imagem": pygame.load.image("A1.jpg")}
    #EmbarcaçãoP11 = {"ObjRect": pygame.Rect(x, y), "Imagem": pygame.load.image("A1.jpg")}
    #EmbarcaçãoP111 = {"ObjRect": pygame.Rect(x, y), "Imagem": pygame.load.image("A1.jpg")}
    #EmbarcaçãoP111 = {"ObjRect": pygame.Rect(x, y), "Imagem": pygame.load.image("A1.jpg")}

    ConjuntoE = [EmbarcaçãoS1, EmbarcaçãoS2, EmbarcaçãoS3, EmbarcaçãoR1, EmbarcaçãoR11, EmbarcaçãoR2, EmbarcaçãoR22, EmbarcaçãoR3, EmbarcaçãoR33, EmbarcaçãoC1, EmbarcaçãoC11, EmbarcaçãoC111, EmbarcaçãoC2, EmbarcaçãoC22, EmbarcaçãoC222]

    Carregando = pygame.image.load('Meio.jpg')

    Fundo = pygame.image.load('Meio.jpg')

    Final = pygame.image.load('Meio.jpg')

    Fundos = [Carregando, Fundo, Final]

    Ícone = pygame.image.load("Ícone.jpg")

    Posicionados = []

def Sons():
    global Jogada
    Jogada = pygame.mixer.Sound('Jogada.wav')
    pygame.mixer.music.load('Plano de Fundo.mp3')
    pygame.mixer.music.play(0, 0.0)


def Embarcações(Posicionados ,ConjuntoE,Tela):

    Submarino(Posicionados, ConjuntoE, Tela)
    Rebocadores(Posicionados, ConjuntoE, Tela)
    #Cruzadores(Posicionados, ConjuntoE, Tela)
    #PortaAviões(Posicionar, ConjuntoE, Ocupados)



def Submarino(Posicionados, ConjuntoE, Tela):
    #Submarino1
    if len(Posicionados) == 0:
        Linha = random.randint(0, 7)
        Coluna = random.randint(0, 7)
        Posicionados.append((Linha, Coluna))
        ConjuntoE[0]["ObjRect"] = ConjuntoL[Linha][Coluna]["ObjRect"]
    Tela.blit(ConjuntoE[0]["Imagem"], ConjuntoE[0]["ObjRect"])

    #Submariono2
    if len(Posicionados) == 1:
        while ((Linha,Coluna) == Posicionados[0]):
            Linha = random.randint(0, 7)
            Coluna = random.randint(0, 7)
        Posicionados.append((Linha, Coluna))
        ConjuntoE[1]["ObjRect"] = ConjuntoL[Linha][Coluna]["ObjRect"]
    Tela.blit(ConjuntoE[1]["Imagem"], ConjuntoE[1]["ObjRect"])

    #Submariono3
    if len(Posicionados) == 2:
        while ((Linha, Coluna) == Posicionados[1]) or (Linha, Coluna) == Posicionados[1]:
            Linha = random.randint(0, 7)
            Coluna = random.randint(0, 7)
        Posicionados.append((Linha, Coluna))
        ConjuntoE[2]["ObjRect"] = ConjuntoL[Linha][Coluna]["ObjRect"]
    Tela.blit(ConjuntoE[2]["Imagem"], ConjuntoE[2]["ObjRect"])


def Rebocadores(Posicionados, ConjuntoE, Tela):
    #Rebocador1
    if len(Posicionados) == 3:
        Sorteando = True
        while Sorteando:
            Linha = random.randint(0, 7)
            Coluna = random.randint(0, 7)
            for Bloquados in Posicionados:
                Permitido = True
                if Bloquados == (Linha, Coluna):
                    Permitido = False
                    break
            Posicionados.append((Linha, Coluna))
            while (Permitido == True):
                Linha1 = Linha
                Coluna1 = Coluna
                Direção = random.randint(0, 1)
                if Direção == 0:
                    Direção = random.randint(0, 1)
                    if Direção == 0:
                        Coluna1 -= 1
                    else:
                        Coluna1 += 1
                    if Coluna1 > 7 or Coluna1 < 0:
                        del Posicionados[3]
                        break
                else:
                    Direção = random.randint(0, 1)
                    if Direção == 0:
                        Direção = random.randint(0, 1)
                        if Direção == 0:
                            Linha1 -= 1
                        else:
                            Linha1 += 1
                        if Linha1 > 7 or Linha1 < 0:
                            del Posicionados[3]
                            break
                    for Bloqueados in Posicionados.copy():
                        if Bloqueados == (Linha1, Coluna1):
                            Permitido = False
                            del Posicionados[3]
                            break
                    if Permitido == True:
                        Posicionados.append((Linha1, Coluna1))
                        ConjuntoE[3]["ObjRect"] = ConjuntoL[Linha][Coluna]["ObjRect"]
                        ConjuntoE[4]["ObjRect"] = ConjuntoL[Linha1][Coluna1]["ObjRect"]
                        Permitido = False
                        Sorteando = False
    Tela.blit(ConjuntoE[3]["Imagem"], ConjuntoE[3]["ObjRect"])
    Tela.blit(ConjuntoE[4]["Imagem"], ConjuntoE[4]["ObjRect"])

    #Rebocador2
    if len(Posicionados) == 5:
        Sorteando = True
        while Sorteando:
            Linha = random.randint(0, 7)
            Coluna = random.randint(0, 7)
            for Bloquados in Posicionados:
                Permitido = True
                if Bloquados == (Linha, Coluna):
                    Permitido = False
                    break
            Posicionados.append((Linha, Coluna))
            while (Permitido == True):
                Linha1 = Linha
                Coluna1 = Coluna
                Direção = random.randint(0, 1)
                if Direção == 0:
                    Direção = random.randint(0, 1)
                    if Direção == 0:
                        Coluna1 -= 1
                    else:
                        Coluna1 += 1
                    if Coluna1 > 7 or Coluna1 < 0:
                        del Posicionados[5]
                        break
                else:
                    Direção = random.randint(0, 1)
                    if Direção == 0:
                        Direção = random.randint(0, 1)
                        if Direção == 0:
                            Linha1 -= 1
                        else:
                            Linha1 += 1
                        if Linha1 > 7 or Linha1 < 0:
                            del Posicionados[5]
                            break
                    for Bloqueados in Posicionados.copy():
                        if Bloqueados == (Linha1, Coluna1):
                            Permitido = False
                            del Posicionados[5]
                            break
                    if Permitido == True:
                        Posicionados.append((Linha1, Coluna1))
                        ConjuntoE[5]["ObjRect"] = ConjuntoL[Linha][Coluna]["ObjRect"]
                        ConjuntoE[6]["ObjRect"] = ConjuntoL[Linha1][Coluna1]["ObjRect"]
                        Permitido = False
                        Sorteando = False
    Tela.blit(ConjuntoE[5]["Imagem"], ConjuntoE[5]["ObjRect"])
    Tela.blit(ConjuntoE[6]["Imagem"], ConjuntoE[6]["ObjRect"])

    #Rebocador3
    if len(Posicionados) == 7:
        Sorteando = True
        while Sorteando:
            Linha = random.randint(0, 7)
            Coluna = random.randint(0, 7)
            for Bloquados in Posicionados:
                Permitido = True
                if Bloquados == (Linha, Coluna):
                    Permitido = False
                    break
            Posicionados.append((Linha, Coluna))
            while (Permitido == True):
                Linha1 = Linha
                Coluna1 = Coluna
                Direção = random.randint(0, 1)
                if Direção == 0:
                    Direção = random.randint(0, 1)
                    if Direção == 0:
                        Coluna1 -= 1
                    else:
                        Coluna1 += 1
                    if Coluna1 > 7 or Coluna1 < 0:
                        del Posicionados[6]
                        break
                else:
                    Direção = random.randint(0, 1)
                    if Direção == 0:
                        Direção = random.randint(0, 1)
                        if Direção == 0:
                            Linha1 -= 1
                        else:
                            Linha1 += 1
                        if Linha1 > 7 or Linha1 < 0:
                            del Posicionados[6]
                            break
                    for Bloqueados in Posicionados.copy():
                        if Bloqueados == (Linha1, Coluna1):
                            Permitido = False
                            del Posicionados[6]
                            break
                    if Permitido == True:
                        Posicionados.append((Linha1, Coluna1))
                        ConjuntoE[7]["ObjRect"] = ConjuntoL[Linha][Coluna]["ObjRect"]
                        ConjuntoE[8]["ObjRect"] = ConjuntoL[Linha1][Coluna1]["ObjRect"]
                        Permitido = False
                        Sorteando = False
    Tela.blit(ConjuntoE[7]["Imagem"], ConjuntoE[7]["ObjRect"])
    Tela.blit(ConjuntoE[8]["Imagem"], ConjuntoE[8]["ObjRect"])

def Cruzadores(Posicionados, ConjuntoE, Tela):
    #Cruzador1
    if len(Posicionados) == 9:
        Sorteando = True
        while Sorteando:
            Linha = random.randint(0, 7)
            Coluna = random.randint(0, 7)
            for Bloquados in Posicionados:
                Permitido = True
                if Bloquados == (Linha, Coluna):
                    Permitido = False
                    break
            Posicionados.append((Linha, Coluna))
            while Permitido:
                Linha1 = Linha
                Coluna1 = Coluna
                Direção = random.randint(0, 1)
                if Direção == 0:
                    Direção = random.randint(0, 1)
                    if Direção == 0:
                        Coluna1 -= 1
                    else:
                        Coluna1 += 1
                    if Coluna1 > 7 or Coluna1 < 0:
                        del Posicionados[8]
                        break
                else:
                    Direção = random.randint(0, 1)
                    if Direção == 0:
                        Direção = random.randint(0, 1)
                        if Direção == 0:
                            Linha1 -= 1
                        else:
                            Linha1 += 1
                        if Linha1 > 7 or Linha1 < 0:
                            del Posicionados[8]
                            break
                    for Bloqueados in Posicionados:
                        if Bloqueados == (Linha1, Coluna1):
                            Permitido = False
                            del Posicionados[8]
                            break
                    Posicionados.append((Linha1, Coluna1))

                ######################################


                    if Permitido == True:
                        if Coluna1 == Coluna:
                            Linha2 = Linha1
                            Direção = random.randint(0, 1)
                            if Direção == 0:
                                Coluna2 = Coluna1 - 2
                            else:
                                Coluna2 = Coluna1 + 2
                            if Coluna2 > 7 or Coluna2 < 0:
                                del Posicionados[9]
                                del Posicionados[8]
                                break
                        else:
                            Coluna2 = Coluna
                            Direção = random.randint(0, 1)
                            if Direção == 0:
                                Linha2 = Linha1 - 2
                            else:
                                Linha2 = Linha1 + 2
                            if Linha2 > 7 or Linha2 < 0:
                                del Posicionados[9]
                                del Posicionados[8]
                                break
                        for Bloqueados in Posicionados.copy():
                            if Bloqueados == (Linha2, Coluna2):
                                Permitido = False
                                del Posicionados[9]
                                del Posicionados[8]
                                break
                        if Permitido == True:
                            Posicionados.append((Linha2, Coluna2))
                            ConjuntoE[9]["ObjRect"] = ConjuntoL[Linha][Coluna]["ObjRect"]
                            ConjuntoE[10]["ObjRect"] = ConjuntoL[Linha1][Coluna1]["ObjRect"]
                            ConjuntoE[11]["ObjRect"] = ConjuntoL[Linha2][Coluna2]["ObjRect"]
                            Permitido = False
                            Sorteando = False

    Tela.blit(ConjuntoE[9]["Imagem"], ConjuntoE[9]["ObjRect"])
    Tela.blit(ConjuntoE[10]["Imagem"], ConjuntoE[10]["ObjRect"])
    Tela.blit(ConjuntoE[11]["Imagem"], ConjuntoE[11]["ObjRect"])

    #Cruzador2
    #Sorteando = False
    #while Sorteando:
        #Linha = random.randint(0, 7)
        #Coluna = random.randint(0, 7)
        #Permitido = True
        #for Bloquados in Ocupados:
            #if Bloquados == (Linha, Coluna):
                #break
            #else:
                #Linha1 = Linha
                #Coluna1 = Coluna
                #Direção = random.randint(0, 1)
                #if Direção == 0:
                    #Direção = random.randint(0, 1)
                    #if Direção == 0:
                        #Coluna1 -= 1
                    #else:
                        #Coluna1 += 1
                    #if Coluna1 > 7 or Coluna1 < 0:
                        #break
                #else:
                    #Direção = random.randint(0, 1)
                    #if Direção == 0:
                        #Direção = random.randint(0, 1)
                        #if Direção == 0:
                            #Linha1 -= 1
                        #else:
                            #Linha1 += 1
                    #if Linha1 > 7 or Linha1 < 0:
                        #break
                #for Bloqueados in Ocupados:
                    #if Bloqueados == (Linha1, Coluna1):
                        #break
                    #else:
                        #if Coluna1 == Coluna:
                            #Direção = random.randint(0, 1)
                            #if Direção == 0:
                                #Coluna2 = Coluna1 - 1
                            #else:
                                #Coluna2 = Coluna1 + 1
                            #if Coluna2 > 7 or Coluna2 < 0:
                                #break
                        #else:
                            #Direção = random.randint(0, 1)
                            #if Direção == 0:
                                #Linha2 = Linha1 - 1
                            #else:
                                #Linha2 = Linha1 + 1
                            #if Linha2 > 7 or Linha2 < 0:
                                #break
                        #Ocupados.append((Linha, Coluna))
                        #ConjuntoE[5]["ObjRect"] = (Posicionar[Linha][Coluna])
                        #Posicionar.remove[Linha][Coluna]
                        #Ocupados.append((Linha, Coluna))
                        #ConjuntoE[6]["ObjRect"] = (Posicionar[Linha1][Coluna1])
                        #Posicionar.remove[Linha][Coluna]
                        #Ocupados.append((Linha, Coluna))
                        #ConjuntoE[7]["ObjRect"] = (Posicionar[Linha1][Coluna1])
                        #Posicionar.remove[Linha][Coluna]
                        #Sorteando = True



def PortaAviões(Posicionar, ConjuntoE,Ocupados):

    Sorteando = True
    while Sorteando:
        Linha = random.randint(0, 7)
        Coluna = random.randint(0, 7)
        for Bloquados in Posicionados:
            Permitido = True
            if Bloquados == (Linha, Coluna):
                Permitido = False
                break
        Posicionados.append((Linha, Coluna))
        while Permitido:
            Linha1 = Linha
            Coluna1 = Coluna
            Direção = random.randint(0, 1)
            if Direção == 0:
                Direção = random.randint(0, 1)
                if Direção == 0:
                    Coluna1 -= 1
                else:
                    Coluna1 += 1
                if Coluna1 > 7 or Coluna1 < 0:
                   break
            else:
                Direção = random.randint(0, 1)
                if Direção == 0:
                    Direção = random.randint(0, 1)
                    if Direção == 0:
                        Linha1 -= 1
                    else:
                        Linha1 += 1
                    if Linha1 > 7 or Linha1 < 0:
                        break
                Linha2 = Linha1d
                Coluna2 = Coluna1



########################
                for Bloqueados in Ocupados:
                    if Bloqueados == (Linha1, Coluna1):
                        break
                    else:
                        if Coluna1 == Coluna:
                            Direção = random.randint(0, 1)
                            if Direção == 0:
                                Coluna2 = Coluna1 - 1
                            else:
                                Coluna2 = Coluna1 + 1
                            if Coluna2 > 7 or Cvoluna2 < 0:
                                break
                        else:
                            Direção = random.randint(0, 1)
                            if Direção == 0:
                                Linha2 = Linha1 - 1
                            else:
                                Linha2 = Linha1 + 1
                            if Linha2 > 7 or Linha2 < 0:
                                break
                    for Bloqueados in Ocupados:
                        if Bloqueados == (Linha2, Coluna2):
                            break
                        if Coluna2 == Coluna1:
                            Coluna3 = Coluna2
                            Direção = random.randint(0, 1)
                            if Direção == 0:
                                Linha3 = Linha2 - 1
                            else:
                                Linha3 = Linha1 + 1
                            if Linha2 > 7 or Linha2 < 0:
                                break
                            else:
                                for Bloqueados in Ocupados:
                                    if Bloqueados == (Linha3, Coluna3):
                                        break
                        else:
                            Linha3 = Linha2
                            Direção = random.randint(0, 1)
                            if Direção == 0:
                                Coluna3 = Coluna2 - 1
                            else:
                                Coluna3 = Coluna2 + 1
                            if Linha3 > 7 or Linha3 < 0:
                                break
                            else:
                                for Bloqueados in Ocupados:
                                    if Bloqueados == (Linha3, Coluna3):
                                        break
                    Ocupados.append((Linha, Coluna))
                    ConjuntoE[8]["ObjRect"] = (Posicionar[Linha][Coluna])
                    Posicionar.remove[Linha][Coluna]
                    Ocupados.append((Linha1, Coluna1))
                    ConjuntoE[9]["ObjRect"] = (Posicionar[Linha1][Coluna1])
                    Posicionar.remove[Linha1][Coluna1]
                    Ocupados.append((Linha2, Coluna2))
                    ConjuntoE[10]["ObjRect"] = (Posicionar[Linha2][Coluna2])
                    Posicionar.remove[Linha2][Coluna2]
                    Ocupados.append((Linha3, Coluna3))
                    ConjuntoE[11]["ObjRect"] = (Posicionar[Linha3][Coluna3])
                    Posicionar.remove[Linha3][Coluna3]
                    Sorteando = True


def Tabuleiro(Fundos, Tela, Janela, Acerto):
    if Janela == "Abertura":
        Tela.blit(Fundos[0], (0, 0))
    elif Janela == "Carregado":
        Tela.blit(Fundos[1], (0, 0))
        Embarcações(Posicionados, ConjuntoE, Tela)
        for Linhas in ConjuntoL:
            for Colunas in Linhas:
                Onda = Colunas
                Tela.blit(Onda['Imagem'], Onda['ObjRect'])
    else:
        Tela.blit(Fundos[2], (0, 0))
        Estilo = pygame.font.get_default_font()
        FonteA = pygame.font.SysFont(Estilo, 30)
        if Acerto == 4:
            ConteúdoA = ("Esquadra derrotada.")
            ConteúdoB = ("Você venceu!")
            TextoA = FonteA.render((ConteúdoA), 1, (0, 0, 0))
            TextoB = FonteA.render((ConteúdoB), 1, (0, 0, 0))
            Tela.blit(TextoA, (120, 20))
            Tela.blit(TextoB, (150, 40))
        else:
            ConteúdoA = ("Você perdeu!")
            ConteúdoB = ("Não  derrotou a esquadra.")
            TextoA = FonteA.render((ConteúdoA), 1, (0, 0, 0))
            TextoB = FonteA.render((ConteúdoB), 1, (0, 0, 0))
            Tela.blit(TextoA, (150, 20))
            Tela.blit(TextoB, (100, 40))

def Principal():
    pygame.init()
    Tela = pygame.display.set_mode((458, 400))
    Relógio = pygame.time.Clock()
    pygame.display.set_caption('Game')
    Imagem()
    Sons()
    pygame.display.set_icon(Ícone)
    Musica = True
    Aberto = True
    Disparos = 5
    Acerto = 0
    Janela = 'Abertura'
    Destruidos = []
    while Aberto:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                Aberto = False
            pygame.display.update()
            if Janela == 'Abertura':
                pygame.time.set_timer(pygame.USEREVENT + 1, 3000)
            if evento.type == pygame.USEREVENT + 1:
                pygame.time.set_timer(pygame.USEREVENT + 1, 0)
                Janela ='Carregado'
            Esquerdo, Giratório ,Direito = pygame.mouse.get_pressed()
            if Esquerdo == True:
                if Janela == 'Carregado':
                    Jogada.play()
                    Atingido = 0
                    for Peças in ConjuntoE:
                        if (pygame.mouse.get_pos())[0] >= (Peças["ObjRect"][0]) and (pygame.mouse.get_pos())[0] <= (Peças["ObjRect"][0]+33):
                            if (pygame.mouse.get_pos())[1] >= (Peças["ObjRect"][1]) and (pygame.mouse.get_pos())[1] <= (Peças["ObjRect"][1]+33):
                                Destruidos.append(Peças)
                                Atingido += 1
                    if Atingido > 0:
                        Acerto += 1
                    else:
                        Disparos -= 1
            if Disparos == 0 or Acerto == 4:
                Janela = "Fim"
            if Direito == True:
                if Musica:
                    pygame.mixer.music.stop()
                    Musica = False
                else:
                    pygame.mixer.music.play()
                    Musica = True
        Tabuleiro(Fundos, Tela, Janela, Acerto)
        if len(Destruidos) != 0:
            for Destruido in Destruidos:
                Tela.blit(Destruido['Imagem'], Destruido['ObjRect'])
        pygame.display.update()
        Relógio.tick(40)
    pygame.quit()

Principal()





















