import pygame
import sys,os,time

pygame.init()
largura,altura = 1200,650
display = pygame.display.set_mode((largura,altura))
fundo = pygame.image.load(os.path.join("assets","img","espaco.png")).convert_alpha()
nave = pygame.image.load(os.path.join("assets","img","ship.png")).convert_alpha()
nave = pygame.transform.scale(nave,(40,40))
naveRec =nave.get_rect(center=(500,500))

bg1 = pygame.image.load(os.path.join("assets","img","espaco.png")).convert_alpha()
bgR1 =bg1.get_rect(center=((altura/2,(largura/2))))

font = pygame.font.Font(os.path.join("assets","Font","Sigmar","Sigmar-Regular.ttf"),16)
texto = font.render('Navinha',True, (65,105,225))
recText = texto.get_rect(center=(100,10))

pygame.display.set_caption("Space Kombat")
loop = True
pos_y = 300
relogio = pygame.time.Clock()
while loop:
    start = int(round(time.time()*1000))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.MOUSEMOTION:
            print(event.pos)
            naveRec.center=event.pos
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(f"tiro{event.pos}")

            
    display.fill((0,0,0))
    display.blit(fundo, (0,0))
    display.blit(nave, naveRec)
    display.blit(texto, recText)

    pos_y = 390

    pygame.display.update()
    end = int(round(time.time()*1000))

    relogio.tick(120)
pygame.quit()