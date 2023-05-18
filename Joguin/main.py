import pygame
from pygame.locals import *
import sys 
from random import randint
from collections import Counter 
import os 

pygame.init()
largura, altura = 720, 560
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("TESTE")
fundo = pygame.image.load(os.path.join("grama.png")).convert_alpha()

#pygame.mixer_music.set_volume(0.1)
#musica_fundo = pygame.mixer_music.load("fundo.mp3")
#pygame.mixer_music.play(-1  )

x_cobra=largura/2
y_cobra=altura/2
x_maca=randint(40, 600) 
y_maca=randint(50, 430)
velocidade = 10
x_controle = 0
y_controle = 0
lista_cobra = []
comprimento = 1


fonte =pygame.font.SysFont("arial", 40, True, False)

relogio= pygame.time.Clock()
Pontos = 0
morreu = False


def aumenta_cobra(lista_cobra):
       for XeY in lista_cobra:
                pygame.draw.rect(tela, (178,58,238), (XeY[0], XeY[1], 20, 20))

def reiniciar_jogo():
     global Pontos, comprimento,x_cobra, y_cobra,lista_cabeca, lista_cobra, x_maca, y_maca, morreu
     Pontos = 0
     comprimento = 1 
     x_cobra = largura//2
     y_cobra = altura//2
     lista_cobra = []
     lista_cabeca = []
     x_maca=randint(40, 600) 
     y_maca=randint(50, 430)
     morreu = False
                 
while True:
    relogio.tick(15)
    tela.blit(fundo, (0,0))
    #tela.fill((0,0,0))
    msg = f"Pontos: {Pontos}"
    texto = fonte.render(msg, True, (255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()
             exit()
        if event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[K_a]:
                if x_controle == velocidade:
                      pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if pygame.key.get_pressed()[K_d]:
                if x_controle == -velocidade:
                      pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if pygame.key.get_pressed()[K_w]:
                if y_controle == velocidade:
                     pass
                else:
                    x_controle = 0
                    y_controle = -velocidade
            if pygame.key.get_pressed()[K_s]:
                if y_controle == -velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle = velocidade

    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle           
   
    if pygame.key.get_pressed()[K_SPACE]:
                x_cobra = largura//2
                y_cobra = altura//2
    cobra = pygame.draw.rect(tela, (0,255,0),(x_cobra,y_cobra,20,20))
    maca = pygame.draw.rect(tela, (255,0,0),(x_maca,y_maca,20,20))

    if cobra.colliderect(maca):
           x_maca=randint(40, 600)
           y_maca=randint(50, 430)
           Pontos+=1
           comprimento = Pontos+comprimento
           

    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    lista_cobra.append(lista_cabeca)

    '''if lista_cobra.count.items(lista_cabeca)>1:
        morreu = True
        while morreu: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if pygame.key.get_pressed()[K_r]:
                        reiniciar_jogo()'''
                       

    if len(lista_cobra)>comprimento:
        del lista_cobra[0]

    aumenta_cobra(lista_cobra)







    tela.blit(texto, (450,40))

    pygame.display.update()

