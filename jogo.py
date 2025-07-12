import pygame 
from pygame.locals import *
import sys
from sys import exit 
from random import randint
from random import choice

# Inicialização do Pygame
pygame.init()

def jogo1():
    # Configurações da tela
    LARGURA = 1140
    ALTURA = 624
    tamanho_da_tela = (LARGURA, ALTURA)
    tela = pygame.display.set_mode(tamanho_da_tela)
    pygame.display.set_caption('Fallen Angels')

    # carregar imgagem de Fundo
    imagem_de_fundo = pygame.image.load('fundoj1.1.jpg')
    imagem_de_fundo = pygame.transform.smoothscale(imagem_de_fundo, tamanho_da_tela)
    fundo_x = 0  # Posição inicial do fundo

    # Carregar música de fundo
    pygame.mixer.music.load("jogo1.mp3")
    pygame.mixer.music.set_volume(0.5)  # Ajuste o volume (0.0 a 1.0)
    pygame.mixer.music.play(-1)  #-1 faz a música repetir indefinidamente

    #cronometro na tela 
    font = pygame.font.Font('Android Assassin.otf', 30)
    texto = font.render('TEMPO:', True, 'white', (0,0,0))
    posicao_texto = texto.get_rect()
    posicao_texto.center = 95, 50
    timer = 0 
    tempo_segundo = 0

    # Personagem
    imagem_do_personagem = pygame.image.load('akira.png')
    imagem_do_personagem = pygame.transform.scale(imagem_do_personagem, (100, 90)) #tamanho do personagem 
    posicao_do_personagem = imagem_do_personagem.get_rect(bottomleft=(100, ALTURA- 155)) #posicao do personagem no eixo x e y 
    gravidade = 1
    velocidade_pulo = -20
    velocidade_y = 0
    no_chao = True

    # Obstáculos
    imagem_do_obstaculo = pygame.image.load('vilao.png')  
    imagem_do_obstaculo = pygame.transform.scale(imagem_do_obstaculo, (100, 100))  #tamanho do personagem vilao 
    obstaculos = []  # Lista para armazenar os obstáculos
    velocidade_obstaculo = 8

    # Função para criar obstáculos
    def criar_obstaculo():
        y = ALTURA - 250  # Posição no chão
        return pygame.Rect(LARGURA, y, 50, 50)  # Retorna um retângulo representando o obstáculo

    #função para exibir a tela de Game Over
    def game_over():
        fonte_game_over = pygame.font.Font('Android Assassin.otf', 60)
        texto_game_over = fonte_game_over.render('GAME OVER', True, 'red', (0, 0, 0))
        tela.blit(texto, posicao_texto)
        posicao_game_over = texto_game_over.get_rect()
        posicao_game_over.center = (500, 350)
        tela.blit(texto_game_over, posicao_game_over)
        pygame.display.update()
        pygame.time.wait(3000)
        return False  # Retorna False para indicar que o jogo deve ser encerrado

    # Configuração do relógio
    relogio = pygame.time.Clock()

    # Loop do jogo
    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                exit()
            if evento.type == KEYDOWN:
                if evento.key == K_SPACE and no_chao:
                    velocidade_y = velocidade_pulo
                    no_chao = False #variável indica se o personagem está no chao (true) ou no ar (false) / se eu quiser que ele pule no ar de novo basta por true

        # Aplica gravidade ao personagem
        velocidade_y += gravidade
        posicao_do_personagem.y += velocidade_y

        # Verifica se o personagem está no chão
        if posicao_do_personagem.bottom >= ALTURA - 155:
            posicao_do_personagem.bottom = ALTURA - 155
            no_chao = True
            velocidade_y = 0

        # Movimentação do fundo (efeito de corrida)
        fundo_x -= velocidade_obstaculo // 2
        if fundo_x <= -LARGURA:
            fundo_x = 0

        # Cronômetro
        if (timer < 60):
            timer += 1
        else:
            tempo_segundo += 1
            texto = font.render('TEMPO:' + str(tempo_segundo), True, 'white', (0, 0, 0))
            timer = 0

        # Adiciona novos obstáculos
        if len(obstaculos) == 0 or obstaculos[-1].x < LARGURA - 700: #verifica se na tela aparece algum obstaculo na largura de 700 / distancia de um obstaculo pra outro
            obstaculos.append(criar_obstaculo())

        # Movimenta os obstáculos
        for obstaculo in obstaculos:
            obstaculo.x -= velocidade_obstaculo #mover o obstaculo pra esquerda (frente) subtraindo a velocidade (velocidade que o obstaculo vai ter)
            if obstaculo.right < 0:  # Remove obstáculos que saíram da tela
                obstaculos.remove(obstaculo)

        # Verifica colisões
        for obstaculo in obstaculos:
            if posicao_do_personagem.colliderect(obstaculo):
                rodando = game_over()
                break

        # Atualização da tela
        tela.blit(imagem_de_fundo, (fundo_x, 0))
        tela.blit(imagem_de_fundo, (fundo_x + LARGURA, 0))  # Desenha o fundo novamente para criar o efeito de movimento
        tela.blit(imagem_do_personagem, posicao_do_personagem)
        tela.blit(texto, posicao_texto)
        # Desenha os obstáculos
        for obstaculo in obstaculos:
            tela.blit(imagem_do_obstaculo, obstaculo)

        pygame.display.update()
        relogio.tick(60)  # Mantém o jogo rodando a 60 FPS


def jogo2():
    #tela
    tamanho_tela=(1000,700)
    tela= pygame.display.set_mode((tamanho_tela))
    pygame.display.set_caption('Fallen Angels') 

    #fundo de tela
    fundo=pygame.image.load('pista2.jpg')
    fundo=pygame.transform.smoothscale(fundo,(1000,700))
    pista_y1 = 0  # Posição y da primeira imagem da pista
    pista_y2 = -700  # Posição y da segunda imagem da pista (logo acima da primeira)
    velocidade_pista = 5  # Velocidade de movimento da pista


    #Cronometro na tela 

    font= pygame.font.Font('Android Assassin.otf',30)
    texto= font.render('TEMPO:',True,'white',(0,0,0))
    posicao_texto=texto.get_rect()
    posicao_texto.center=95,50
    timer=0 
    tempo_segundo=0

    # Carregar música de fundo
    pygame.mixer.music.load("jogo1.mp3")
    pygame.mixer.music.set_volume(0.5)  # Ajuste o volume (0.0 a 1.0)
    pygame.mixer.music.play(-1)  #-1 faz a música repetir indefinidamente


    #as faixas da pista (esquerda e direita)

    faixa_esquerda = (400, 445)  # intervalo de x para a faixa esquerda
    faixa_direita = (445, 600)   # intervalo de x para a faixa direita

    # funçao que vai gerar posições aleatórias dentro das faixas
    def gerar_posicao_aleatoaria():
        faixa = choice([faixa_esquerda, faixa_direita])  # Escolhe aleatoriamente entre esquerda e direita 
        return randint(faixa[0], faixa[1])  # retorna uma posição x aleatória dentro da faixa escolhida


    #moto na pista e a posicao da moto inicialmente 
    posicao_x=500
    posicao_y=620
    velocidade=10
    moto_surface=pygame.image.load('moto.png')
    moto_surface=pygame.transform.scale(moto_surface,(50,100)) #tamanho da moto na tela
    moto_rect = pygame.Rect(posicao_x, posicao_y, 20, 30) #ajustando o retângulo da moto

    #carro1 na pista - carro verde
    
    velocidade_carro1= -5
    posicao_y_carro1=-10
    posicao_x_carro1=gerar_posicao_aleatoaria()
    carro1_surface=pygame.image.load('carro verde.png')
    carro1_surface=pygame.transform.scale(carro1_surface,(90,80))


    #carro2 na pista - policia

    velocidade_carro2= -5 
    posicao_y_carro2= -15
    posicao_x_carro2= gerar_posicao_aleatoaria()
    carro2_surface=pygame.image.load('carro policia.png')
    carro2_surface=pygame.transform.scale(carro2_surface,(75,90))


    #carro3 na pista - ambulancia

    velocidade_carro3= -5 
    posicao_y_carro3= -120
    posicao_x_carro3= gerar_posicao_aleatoaria()
    carro3_surface=pygame.image.load('carro ambulancia.png')
    carro3_surface=pygame.transform.scale(carro3_surface,(60,80))


    #carro4 na pista - taxi

    velocidade_carro4= -5 
    posicao_y_carro4= -250
    posicao_x_carro4=gerar_posicao_aleatoaria()
    carro4_surface=pygame.image.load('carro taxi.png')
    carro4_surface=pygame.transform.scale(carro4_surface,(60,80))


    #carro5 na pista - vermelho 
    velocidade_carro5= -5 
    posicao_y_carro5= -300
    posicao_x_carro5= gerar_posicao_aleatoaria()
    carro5_surface=pygame.image.load('carro 5.png')
    carro5_surface=pygame.transform.scale(carro5_surface,(58,85))


    #carro6 na pista -laranja 
    velocidade_carro6= -5 
    posicao_y_carro6= -400
    posicao_x_carro6= gerar_posicao_aleatoaria()
    carro6_surface=pygame.image.load('carro 6.png')
    carro6_surface=pygame.transform.scale(carro6_surface,(56,90))



    #função para exibir a tela de Game Over
    def game_over():
        fonte_game_over = pygame.font.Font('Android Assassin.otf', 60)
        texto_game_over = fonte_game_over.render('GAME OVER', True, 'red', (0, 0, 0))
        posicao_game_over = texto_game_over.get_rect()
        posicao_game_over.center = (500, 350)
        tela.blit(texto_game_over, posicao_game_over)
        pygame.display.update()
        pygame.time.wait(3000)

    #velocidade
    relogio= pygame.time.Clock()

    #loop principal do jogo
    while True:
        #condição para fechar o jogo 
        for event in pygame.event.get():
            if event.type == QUIT: 
                pygame.quit() 
                exit()

        #movimento da moto pra direita e esquerda, pra cima e pra baixo
        comando=pygame.key.get_pressed() 
        if comando[pygame.K_RIGHT] and posicao_x<=640: #comando para moto ir pra direita e delimitar o espaço que ela vai ficar
            posicao_x+=velocidade
        if comando[pygame.K_LEFT] and posicao_x>=325: #comando para moto ir pra esqueda e delimitar o espaço que ela vai ficar
            posicao_x-=velocidade 
        
        #cronometro
        if (timer<20):
            timer+=1
        else:
            tempo_segundo+=1
            texto= font.render('TEMPO:'+str(tempo_segundo),True,'white',(0,0,0))
            timer=0

        # Movimento da pista 
        pista_y1 += velocidade_pista
        pista_y2 += velocidade_pista

        # Reposiciona as imagens da pista quando saem da tela
        if pista_y1 >= 700:
            pista_y1 = -700
        if pista_y2 >= 700:
            pista_y2 = -700

        #movimento do carro1 
        posicao_y_carro1 -= velocidade_carro1
        if (posicao_y_carro1>=700):
            posicao_y_carro1= randint(-800,-700) #randint determina a posiçao aleatoria que o carro vai 
            posicao_x_carro1=gerar_posicao_aleatoaria()
            velocidade_carro1-=3

        #movimento do carro2 
        posicao_y_carro2 -= velocidade_carro2
        if (posicao_y_carro2>=700):
            posicao_y_carro2= randint(-810,-700)
            posicao_x_carro2=gerar_posicao_aleatoaria()
            velocidade_carro2-=3

        #movimento do carro3 
        posicao_y_carro3 -= velocidade_carro3
        if (posicao_y_carro3>=700):
            posicao_y_carro3= randint(-815,-700)
            posicao_x_carro3=gerar_posicao_aleatoaria()
            velocidade_carro3-=3

        #movimento do carro4 
        posicao_y_carro4 -= velocidade_carro4
        if (posicao_y_carro4>=700):
            posicao_y_carro4= randint(-820,-700)
            posicao_x_carro4=gerar_posicao_aleatoaria()
            velocidade_carro4-=3
        #movimento do carro5 
        posicao_y_carro5 -= velocidade_carro5
        if (posicao_y_carro5>=700):
            posicao_y_carro5= randint(-800,-700)
            posicao_x_carro5=gerar_posicao_aleatoaria()
            velocidade_carro5-=3
        #movimento do carro6 
        posicao_y_carro6 -= velocidade_carro6
        if (posicao_y_carro6>=700):
            posicao_y_carro6= randint(-800,-700)
            posicao_x_carro6=gerar_posicao_aleatoaria()
            velocidade_carro6-=3

        #detecta colisão 
        carro1_rect = pygame.Rect(posicao_x_carro1, posicao_y_carro1, 50,60)
        if moto_rect.colliderect(carro1_rect):
            game_over()
            break
        carro2_rect = pygame.Rect(posicao_x_carro2, posicao_y_carro2, 50,60)
        if moto_rect.colliderect(carro2_rect):
            game_over()
            break
        carro3_rect = pygame.Rect(posicao_x_carro3, posicao_y_carro3, 50,60)
        if moto_rect.colliderect(carro3_rect):
            game_over()
            break
        carro4_rect = pygame.Rect(posicao_x_carro4, posicao_y_carro4, 50,60)
        if moto_rect.colliderect(carro4_rect):
            game_over()
            break
        carro5_rect = pygame.Rect(posicao_x_carro5, posicao_y_carro5, 50,60)
        if moto_rect.colliderect(carro5_rect):
            game_over()
            break
        carro6_rect = pygame.Rect(posicao_x_carro6, posicao_y_carro6, 50,60)
        if moto_rect.colliderect(carro6_rect):
            game_over()
            break

        # Desenha os elementos na tela
        tela.blit(fundo, (0, pista_y1))  # Desenha a primeira imagem da pista verde
        tela.blit(fundo, (0, pista_y2))  # Desenha a segunda imagem da pista verde
        tela.blit(moto_surface, moto_rect)
        tela.blit(carro1_surface,(carro1_rect))
        tela.blit(carro2_surface,(carro2_rect))
        tela.blit(carro3_surface,(carro3_rect))
        tela.blit(carro4_surface,(carro4_rect))
        tela.blit(carro5_surface,(carro5_rect))
        tela.blit(carro6_surface,(carro6_rect))
        tela.blit(texto,posicao_texto)
        moto_rect.topleft = (posicao_x, posicao_y)
        moto_rect.bottomleft = (posicao_x, posicao_y)
        relogio.tick(15) #velocidade que a moto vai se mover na tela, quanto maior mais rapido
        pygame.display.update() #atualizar o jogo sempre que algo acontecer


# Configurações da tela
LARGURA, ALTURA = 1104, 624
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Menu Inicial")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CINZA = (100, 100, 100)
VERMELHO = (255, 0, 0)

# Fonte customizada
fonte = pygame.font.Font('Android Assassin.otf', 50)

# Carregar imagem de fundo
imagem_fundo = pygame.image.load("menu.jpg")
imagem_fundo = pygame.transform.scale(imagem_fundo, (LARGURA, ALTURA))

# Carregar música de fundo
pygame.mixer.music.load("audiomenu.mp3")
pygame.mixer.music.set_volume(0.5)  # Ajuste o volume (0.0 a 1.0)
pygame.mixer.music.play(-1)  #-1 faz a música repetir indefinidamente

# Função para desenhar o texto
def desenhar_texto(texto, fonte, cor, superficie, x, y):
    objeto_texto = fonte.render(texto, True, cor)
    retangulo_texto = objeto_texto.get_rect(center=(x, y))
    superficie.blit(objeto_texto, retangulo_texto)

# Loop do menu
def menu_principal():
    while True:
        tela.blit(imagem_fundo, (0, 0))
        desenhar_texto("driving", fonte, VERMELHO, tela, LARGURA // 2, ALTURA // 4)
        
        # Definição dos botões
        botao_jogo1 = pygame.Rect(LARGURA // 3, ALTURA // 2, LARGURA // 3, 50)
        botao_jogo2 = pygame.Rect(LARGURA // 3, ALTURA // 2 + 70, LARGURA // 3, 50)
        
        pygame.draw.rect(tela, CINZA, botao_jogo1)
        pygame.draw.rect(tela, CINZA, botao_jogo2)
        
        desenhar_texto("Jogo 1", fonte, PRETO, tela, LARGURA // 2, ALTURA // 2 + 25)
        desenhar_texto("Jogo 2", fonte, PRETO, tela, LARGURA // 2, ALTURA // 2 + 95)
        
        # Captura de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_jogo1.collidepoint(evento.pos): #verifica se o clique do mouse (evento.pos) foi dentro do retângulo do botão 
                    loop_jogo1()
                if botao_jogo2.collidepoint(evento.pos):
                    loop_jogo2()
        
        pygame.display.flip()

# Função do Jogo 1
def loop_jogo1():
    tela.blit(imagem_fundo, (0, 0))
    desenhar_texto("Jogo 1 em Andamento...", fonte, BRANCO, tela, LARGURA // 2, ALTURA // 2)
    pygame.display.flip()
    pygame.time.wait(2000)  # Exibe a mensagem por 2 segundos
    jogo1()  # Inicia o jogo1

# Função do Jogo 2
def loop_jogo2():
    tela.blit(imagem_fundo, (0, 0))
    desenhar_texto("Jogo 2 em Andamento...", fonte, BRANCO, tela, LARGURA // 2, ALTURA // 2)
    pygame.display.flip()
    pygame.time.wait(2000)  # Exibe a mensagem por 2 segundos
    jogo2()

# Iniciar o menu
menu_principal()