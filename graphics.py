import pygame
import sys
from pygame.locals import *
# set up pygame
pygame.init()

#Set up colours (RGB)
BG = (68, 85, 90)
WHITE = (255, 225, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# set up font
basicFont = pygame.font.SysFont(None, 20)

# set up window
def window(WINDOWWIDTH, WINDOWHEIGHT):
    global windowSurface
    windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
    pygame.display.set_caption("Blackjack")
    windowSurface.fill(BG)
    img = pygame.image.load('AS.png')
    pygame.display.set_icon(img)
    pygame.display.update()


def draw_card(x, y, cardFace):
    # draw white background on card
    CARD_WIDTH = 67
    CARD_HEIGHT = 93.8

    if cardFace == "2d":
        img = pygame.image.load("2D.png")
        img = pygame.transform.scale(img, (CARD_WIDTH, CARD_HEIGHT))
        windowSurface.blit(img, (x, y))

    if cardFace == "2h":
        img = pygame.image.load("2H.png")
        img = pygame.transform.scale(img, (CARD_WIDTH, CARD_HEIGHT))
        windowSurface.blit(img, (x, y))

    if cardFace == "2c":
        img = pygame.image.load("2C.png")
        img = pygame.transform.scale(img, (CARD_WIDTH, CARD_HEIGHT))
        windowSurface.blit(img, (x, y))

    if cardFace == "2s":
        img = pygame.image.load("2S.png")
        img = pygame.transform.scale(img, (CARD_WIDTH, CARD_HEIGHT))
        windowSurface.blit(img, (x, y))
    
    if cardFace == "3d":
        img = pygame.image.load("3D.png")
        img = pygame.transform.scale(img, (CARD_WIDTH, CARD_HEIGHT))
        windowSurface.blit(img, (x, y))

    if cardFace == "3h":
        img = pygame.image.load("3H.png")
        img = pygame.transform.scale(img, (CARD_WIDTH, CARD_HEIGHT))
        windowSurface.blit(img, (x, y))

    if cardFace == "3c":
        img = pygame.image.load("3C.png")
        img = pygame.transform.scale(img, (CARD_WIDTH, CARD_HEIGHT))
        windowSurface.blit(img, (x, y))

    if cardFace == "3s":
        img = pygame.image.load("3S.png")
        img = pygame.transform.scale(img, (CARD_WIDTH, CARD_HEIGHT))
        windowSurface.blit(img, (x, y))
    if cardFace == "4d":
        img = pygame.image.load("4D.png")
        img = pygame.transform.scale(img, (CARD_WIDTH, CARD_HEIGHT))
        windowSurface.blit(img, (x, y))

    if cardFace == "4h":
        img = pygame.image.load("4H.png")
        img = pygame.transform.scale(img, (CARD_WIDTH, CARD_HEIGHT))
        windowSurface.blit(img, (x, y))

    if cardFace == "4c":
        img = pygame.image.load("4C.png")
        img = pygame.transform.scale(img, (CARD_WIDTH, CARD_HEIGHT))
        windowSurface.blit(img, (x, y))

    if cardFace == "4s":
        img = pygame.image.load("4S.png")
        img = pygame.transform.scale(img, (CARD_WIDTH, CARD_HEIGHT))
        windowSurface.blit(img, (x, y))
        
    if cardFace == "5d":
        img = pygame.image.load("5D.png")
        img = pygame.transform.scale(img, (CARD_WIDTH, CARD_HEIGHT))
        windowSurface.blit(img, (x, y))

    if cardFace == "5h":
        img = pygame.image.load("5H.png")
        img = pygame.transform.scale(img, (CARD_WIDTH, CARD_HEIGHT))
        windowSurface.blit(img, (x, y))

    if cardFace == "5c":
        img = pygame.image.load("5C.png")
        img = pygame.transform.scale(img, (CARD_WIDTH, CARD_HEIGHT))
        windowSurface.blit(img, (x, y))

    if cardFace == "5s":
        img = pygame.image.load("5S.png")
        img = pygame.transform.scale(img, (CARD_WIDTH, CARD_HEIGHT))
        windowSurface.blit(img, (x, y))
        
    if cardFace == "6d":
        img = pygame.image.load("6D.png")
        img = pygame.transform.scale(img, (CARD_WIDTH, CARD_HEIGHT))
        windowSurface.blit(img, (x, y))

    if cardFace == "6h":
        img = pygame.image.load("6H.png")
        img = pygame.transform.scale(img, (CARD_WIDTH, CARD_HEIGHT))
        windowSurface.blit(img, (x, y))

    if cardFace == "6c":
        img = pygame.image.load("6C.png")
        img = pygame.transform.scale(img, (CARD_WIDTH, CARD_HEIGHT))
        windowSurface.blit(img, (x, y))

    if cardFace == "6s":
        img = pygame.image.load("6S.png")
        img = pygame.transform.scale(img, (CARD_WIDTH, CARD_HEIGHT))
        windowSurface.blit(img, (x, y))
        
    if cardFace == "7d":
        img = pygame.image.load("7D.png")
        img = pygame.transform.scale(img, (CARD_WIDTH, CARD_HEIGHT))
        windowSurface.blit(img, (x, y))

    if cardFace == "7h":
        img = pygame.image.load("7H.png")
        img = pygame.transform.scale(img, (CARD_WIDTH, CARD_HEIGHT))
        windowSurface.blit(img, (x, y))

    if cardFace == "7c":
        img = pygame.image.load("7C.png")
        img = pygame.transform.scale(img, (CARD_WIDTH, CARD_HEIGHT))
        windowSurface.blit(img, (x, y))

    if cardFace == "7s":
        img = pygame.image.load("7S.png")
        img = pygame.transform.scale(img, (CARD_WIDTH, CARD_HEIGHT))
        windowSurface.blit(img, (x, y))
        
    if cardFace == "8d":
        img = pygame.image.load("8D.png")
        img = pygame.transform.scale(img, (CARD_WIDTH, CARD_HEIGHT))
        windowSurface.blit(img, (x, y))

    if cardFace == "8h":
        img = pygame.image.load("8H.png")
        img = pygame.transform.scale(img, (CARD_WIDTH, CARD_HEIGHT))
        windowSurface.blit(img, (x, y))

    if cardFace == "8c":
        img = pygame.image.load("8C.png")
        img = pygame.transform.scale(img, (CARD_WIDTH, CARD_HEIGHT))
        windowSurface.blit(img, (x, y))

    if cardFace == "8s":
        img = pygame.image.load("8S.png")
        img = pygame.transform.scale(img, (CARD_WIDTH, CARD_HEIGHT))
        windowSurface.blit(img, (x, y))
        
    if cardFace == "9d":
        img = pygame.image.load("9D.png")
        img = pygame.transform.scale(img, (CARD_WIDTH, CARD_HEIGHT))
        windowSurface.blit(img, (x, y))

    if cardFace == "9h":
        img = pygame.image.load("9H.png")
        img = pygame.transform.scale(img, (CARD_WIDTH, CARD_HEIGHT))
        windowSurface.blit(img, (x, y))

    if cardFace == "9c":
        img = pygame.image.load("9C.png")
        img = pygame.transform.scale(img, (CARD_WIDTH, CARD_HEIGHT))
        windowSurface.blit(img, (x, y))

    if cardFace == "9s":
        img = pygame.image.load("9S.png")
        img = pygame.transform.scale(img, (CARD_WIDTH, CARD_HEIGHT))
        windowSurface.blit(img, (x, y))
        
    if cardFace == "10d":
        img = pygame.image.load("10D.png")
        img = pygame.transform.scale(img, (CARD_WIDTH, CARD_HEIGHT))
        windowSurface.blit(img, (x, y))

    if cardFace == "10h":
        img = pygame.image.load("10H.png")
        img = pygame.transform.scale(img, (CARD_WIDTH, CARD_HEIGHT))
        windowSurface.blit(img, (x, y))

    if cardFace == "10c":
        img = pygame.image.load("10C.png")
        img = pygame.transform.scale(img, (CARD_WIDTH, CARD_HEIGHT))
        windowSurface.blit(img, (x, y))

    if cardFace == "10s":
        img = pygame.image.load("10S.png")
        img = pygame.transform.scale(img, (CARD_WIDTH, CARD_HEIGHT))
        windowSurface.blit(img, (x, y))
        
    if cardFace == "Jd":
        img = pygame.image.load("JD.png")
        img = pygame.transform.scale(img, (CARD_WIDTH, CARD_HEIGHT))
        windowSurface.blit(img, (x, y))

    if cardFace == "Jh":
        img = pygame.image.load("JH.png")
        img = pygame.transform.scale(img, (CARD_WIDTH, CARD_HEIGHT))
        windowSurface.blit(img, (x, y))

    if cardFace == "Jc":
        img = pygame.image.load("JC.png")
        img = pygame.transform.scale(img, (CARD_WIDTH, CARD_HEIGHT))
        windowSurface.blit(img, (x, y))

    if cardFace == "Js":
        img = pygame.image.load("JS.png")
        img = pygame.transform.scale(img, (CARD_WIDTH, CARD_HEIGHT))
        windowSurface.blit(img, (x, y))
        
    if cardFace == "Qd":
        img = pygame.image.load("QD.png")
        img = pygame.transform.scale(img, (CARD_WIDTH, CARD_HEIGHT))
        windowSurface.blit(img, (x, y))

    if cardFace == "Qh":
        img = pygame.image.load("QH.png")
        img = pygame.transform.scale(img, (CARD_WIDTH, CARD_HEIGHT))
        windowSurface.blit(img, (x, y))

    if cardFace == "Qc":
        img = pygame.image.load("QC.png")
        img = pygame.transform.scale(img, (CARD_WIDTH, CARD_HEIGHT))
        windowSurface.blit(img, (x, y))

    if cardFace == "Qs":
        img = pygame.image.load("QS.png")
        img = pygame.transform.scale(img, (CARD_WIDTH, CARD_HEIGHT))
        windowSurface.blit(img, (x, y))
        
    if cardFace == "Kd":
        img = pygame.image.load("KD.png")
        img = pygame.transform.scale(img, (CARD_WIDTH, CARD_HEIGHT))
        windowSurface.blit(img, (x, y))

    if cardFace == "Kh":
        img = pygame.image.load("KH.png")
        img = pygame.transform.scale(img, (CARD_WIDTH, CARD_HEIGHT))
        windowSurface.blit(img, (x, y))

    if cardFace == "Kc":
        img = pygame.image.load("KC.png")
        img = pygame.transform.scale(img, (CARD_WIDTH, CARD_HEIGHT))
        windowSurface.blit(img, (x, y))

    if cardFace == "Ks":
        img = pygame.image.load("KS.png")
        img = pygame.transform.scale(img, (CARD_WIDTH, CARD_HEIGHT))
        windowSurface.blit(img, (x, y))
        
    if cardFace == "Ad":
        img = pygame.image.load("AD.png")
        img = pygame.transform.scale(img, (CARD_WIDTH, CARD_HEIGHT))
        windowSurface.blit(img, (x, y))

    if cardFace == "Ah":
        img = pygame.image.load("AH.png")
        img = pygame.transform.scale(img, (CARD_WIDTH, CARD_HEIGHT))
        windowSurface.blit(img, (x, y))

    if cardFace == "Ac":
        img = pygame.image.load("AC.png")
        img = pygame.transform.scale(img, (CARD_WIDTH, CARD_HEIGHT))
        windowSurface.blit(img, (x, y))

    if cardFace == "As":
        img = pygame.image.load("AS.png")
        img = pygame.transform.scale(img, (CARD_WIDTH, CARD_HEIGHT))
        windowSurface.blit(img, (x, y))
        

    pygame.display.update()

# shows the text passed at the position passed.
def display_text(text, x, y):
    shownText = basicFont.render(text, True, BLACK)
    textRect = shownText.get_rect()
    textRect.left = x
    textRect.top = y
    windowSurface.blit(shownText, textRect)
