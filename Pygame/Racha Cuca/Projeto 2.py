import pygame, random


def Sons():

    global Jogada

    Jogada = pygame.mixer.Sound('Movendo.wav')

    pygame.mixer.music.load('Plano de Fundo.mp3')

    pygame.mixer.music.play(-1, 0.0)



def Imagens():

    global Lacuna, Peças, Paredes, Ícone, Posições

    Lacuna = {"ObjRect": pygame.Rect(34, 300, 60, 60), 'Imagem': pygame.image.load('ball.png')}

    Primeira = {"Obj": pygame.Rect(34, 120, 60, 60), 'Imagem': pygame.image.load('1º.png')}

    Segunda = {"Obj": pygame.Rect(94, 120, 60, 60), 'Imagem': pygame.image.load('2º.png')}

    Terceira = {"Obj": pygame.Rect(154, 120, 60, 60), 'Imagem': pygame.image.load('3º.png')}

    Quarta = {"Obj": pygame.Rect(34, 180, 60, 60), 'Imagem': pygame.image.load('4º.png')}

    Quinta = {"Obj": pygame.Rect(94, 180, 60, 60), 'Imagem': pygame.image.load('5º.png')}

    Sexta = {"Obj": pygame.Rect(154, 180, 60, 60), 'Imagem': pygame.image.load('6º.png')}

    Sétima = {"Obj": pygame.Rect(34, 240, 60, 60), 'Imagem': pygame.image.load('7º.png')}

    Oitava = {"Obj": pygame.Rect(94, 240, 60, 60), 'Imagem': pygame.image.load('8º.png')}

    Nona = {"Obj": pygame.Rect(154, 240, 60, 60), 'Imagem': pygame.image.load('9º.png')}

    Carregando = pygame.image.load('Inicio.jpg')

    Fundo = pygame.image.load('Meio.jpg')

    Final = pygame.image.load('Final.png')

    Ícone = pygame.image.load("Ícone.jpg")

    Paredes = [Carregando, Fundo, Final]

    Peças = [Primeira, Segunda, Terceira, Quarta, Quinta, Sexta, Sétima, Oitava, Nona]

    Posições = [(34, 120), (94, 120), (154, 120), (34, 180), (94, 180), (154, 180), (34, 240), (94, 240), (154, 240)]



def Desordenando():

    Lacuna['ObjRect'].x, Lacuna['ObjRect'].y = (34, 300)

    Espaços = Posições.copy()

    Espaços.remove((34, 240))

    Ocupados = ''

    for Peça in Peças:

        if Peça != Peças[6]:

            Preenchido = False

            while Preenchido == False:

                Lugares = random.randint(0, 7)

                if str(Lugares) not in Ocupados:

                    Ocupados += str(Lugares)

                    Peça['Obj'].x, Peça['Obj'].y = Espaços[Lugares][0], Espaços[Lugares][1]

                    Preenchido = True

        else:

            Peça['Obj'].x, Peça['Obj'].y = (34, 240)



def Jogadas(Espaço, Música):

    if Lacuna['ObjRect'].left > 154:

        Lacuna['ObjRect'].x, Lacuna['ObjRect'].y = Espaço

    elif Lacuna['ObjRect'].left < 34:

        Lacuna['ObjRect'].x, Lacuna['ObjRect'].y = Espaço

    elif Lacuna['ObjRect'].top > 300:

        Lacuna['ObjRect'].x, Lacuna['ObjRect'].y = Espaço

    elif Lacuna['ObjRect'].top < 120:

        Lacuna['ObjRect'].x, Lacuna['ObjRect'].y = Espaço

    elif Lacuna['ObjRect'].top == 300 and Lacuna['ObjRect'].left > 34:

        Lacuna['ObjRect'].x, Lacuna['ObjRect'].y = Espaço

    else:

        for Peça in Peças:

            if Lacuna['ObjRect'].colliderect(Peça['Obj']):

                Peça['Obj'].x, Peça['Obj'].y = Espaço

                if Música:

                    Jogada.play()





def Verificando():

    global Corretas

    Corretas = 0

    Espaço = -1

    for Peça in Peças:

        Espaço += 1

        if Peça['Obj'].x == Posições[Espaço][0] and Peça['Obj'].y == Posições[Espaço][1]:

            Corretas += 1



def Principal():

    pygame.init()

    Imagens()

    Sons()

    Desordenando()

    Tela = pygame.display.set_mode((250,420))

    pygame.display.set_caption('Game')

    pygame.display.set_icon(Ícone)

    Relógio = pygame.time.Clock()

    Movimento = 0

    Carregado = 0

    Música = True

    Executando = True

    while Executando:

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:

                Executando = False

            pygame.display.update()

            if Carregado == False:

                pygame.time.set_timer(pygame.USEREVENT + 1, 3000)

            if evento.type == pygame.USEREVENT + 1:

                pygame.time.set_timer(pygame.USEREVENT + 1, 0)

                Carregado = True

            Espaço = Lacuna['ObjRect'].x, Lacuna['ObjRect'].y

            if evento.type == pygame.KEYDOWN:

                 if evento.key == pygame.K_RIGHT:

                    Lacuna['ObjRect'].x += Lacuna['ObjRect'].width

                    Movimento += 1

                 if evento.key == pygame.K_LEFT:

                    Lacuna['ObjRect'].x -= Lacuna['ObjRect'].width

                    Movimento += 1

                 if evento.key == pygame.K_DOWN:

                    Lacuna['ObjRect'].y += Lacuna['ObjRect'].height

                    Movimento += 1

                 if evento.key == pygame.K_UP:

                    Lacuna['ObjRect'].y -= Lacuna['ObjRect'].height

                    Movimento += 1

                 if evento.key == pygame.K_1:

                     Desordenando()

                     Movimento = 0

                     Carregado = True

                 if evento.key == pygame.K_0:

                    if Música:

                        pygame.mixer.music.stop()

                        Música = False

                    else:

                        pygame.mixer.music.play()

                        Música = True

        if Carregado == 0:

            Tela.blit(Paredes[0], (0, 0))

            Carregado = False

        if Carregado == True:

            Tela.blit(Paredes[1], (0, 0))

            for Bloco in Peças:

                Tela.blit(Bloco['Imagem'], Bloco["Obj"])

            Tela.blit(Lacuna['Imagem'], Lacuna['ObjRect'])

        Jogadas(Espaço, Música)

        Verificando()

        if Corretas == 9:

            Carregado = False

            Tela.blit(Paredes[2], (0, 0))

            Estilo = pygame.font.get_default_font()

            FonteA = pygame.font.SysFont(Estilo, 30)

            FonteB = pygame.font.SysFont(Estilo, 20)

            ConteúdoA = ("Você Venceu!")

            ConteúdoB = (f"Quantidade de jogadas:{ Movimento }!")

            TextoA = FonteA.render((ConteúdoA), 1, (255, 255, 255))

            TextoB = FonteB.render((ConteúdoB), 1, (255, 255, 255))

            Tela.blit(TextoA, (60, 320))

            Tela.blit(TextoB, (45, 360))

        pygame.display.update()

        Relógio.tick(40)

    pygame.quit()

Principal()