import pygame
import random

plansza = [[' ' for i in range(10)] for j in range(10)]
pygame.init()
ekran = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Snake")
rozpoczecie = False
zegar = pygame.time.Clock()
ostatnie_posuniecie = 0
def rysuj_linie(rozmiarplanszy, kolor=0x000000):
    for x in range(rozmiarplanszy):
        for y in range(rozmiarplanszy):
            pygame.draw.line(ekran, kolor, (x*50, y*50), (x*50, 500), 3)
            pygame.draw.line(ekran, kolor, (x*50, y*50), (500, y*50), 3)
    pygame.draw.line(ekran, 0x000000, (0, rozmiarplanszy*50), (rozmiarplanszy*50, rozmiarplanszy*50), 10)
    pygame.draw.line(ekran, 0x000000, (rozmiarplanszy*50, 0), (rozmiarplanszy*50, rozmiarplanszy*50), 10)
    pygame.draw.line(ekran, 0x000000, (0, 0), (rozmiarplanszy*50, 0), 10)
    pygame.draw.line(ekran, 0x000000, (0,rozmiarplanszy*50), (0, 0), 10)
global licznik
licznik = 50
punkty = 1
def autoposuniecie():
    global licznik, x,y
    global ostatnie_posuniecie
    licznik -=1
    if licznik == 0:
        licznik = 50
        if ostatnie_posuniecie == "UP":
            y-=1
        
        if ostatnie_posuniecie == "DOWN":
            y+=1
        if ostatnie_posuniecie == "RIGHT":
            x+=1
        if ostatnie_posuniecie == "LEFT":
            x-=1
generowanie = True
x_owoc = 0
y_owoc = 0
def generuj_owoc():
    global generowanie,x,y, punkty,x_owoc, y_owoc
    
    if generowanie:
        x_owoc = random.randint(0,9)
        y_owoc = random.randint(0,9)
        generowanie = False
    if x == x_owoc and y == y_owoc:
        punkty+=1
        generowanie = True
    pygame.draw.circle(ekran, 0xff0000, (x_owoc*50+25, y_owoc*50+25), 20)
        

y = random.randint(0, 9)
x = random.randint(0,9)  
kliknieto_x = False
koniec_gry = False
ustawiono_flage = False
while not kliknieto_x:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            kliknieto_x = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y-=1
                ostatnie_posuniecie="UP"
            if event.key == pygame.K_DOWN:
                y+=1
                ostatnie_posuniecie="DOWN"
            if event.key == pygame.K_LEFT:
                x-=1
                ostatnie_posuniecie="LEFT"
            if event.key == pygame.K_RIGHT:
                x+=1
                ostatnie_posuniecie="RIGHT"
        

    if x < 0:
        kliknieto_x = True
    if y < 0:
        kliknieto_x = True
    if x > 9:
        kliknieto_x = True
    if y > 9:
        kliknieto_x = True


    
    ekran.fill(0xFFFFFF)
   
    for y_pos in range(9):
        for x_pos in range(9):
            if plansza[y_pos][x_pos] == '*':
                pygame.draw.rect(ekran, 0x00ff00,  pygame.Rect(x_pos*50, y_pos*50, 50, 50))
    if punkty == 1:
        
        if ostatnie_posuniecie == "UP":
                plansza[y+1][x] = ' ' 
        elif ostatnie_posuniecie == "DOWN":
                plansza[y-1][x] = ' '
        elif ostatnie_posuniecie == "RIGHT":
                plansza[y][x-1] = ' '
        elif ostatnie_posuniecie == "LEFT":
               plansza[y][x+1] = ' '
        
    plansza[y][x] = '*'

    if punkty >= 2:
        if ostatnie_posuniecie == "UP":
                plansza[y+punkty][x] = '*'
                ostatnie_y = y+punkty+1
                ostatnie_x = x
        elif ostatnie_posuniecie == "DOWN":
                plansza[y-punkty][x] = '*'
                ostatnie_y = y-punkty-1
                ostatnie_x = x
        elif ostatnie_posuniecie == "RIGHT":
                plansza[y][x+punkty] = '*'
                ostatnie_y = y
                ostatnie_x = x+punkty+1
        elif ostatnie_posuniecie == "LEFT":
               plansza[y][x-punkty] = '*'
               ostatnie_y = y
               ostatnie_x = x-punkty-1
        plansza[ostatnie_y][ostatnie_x] = ' ' 

        
    
    rysuj_linie(10, 0xcccccc)
    generuj_owoc()
    
    
    autoposuniecie()
    pygame.display.flip()
    
    zegar.tick(60)
pygame.quit()
