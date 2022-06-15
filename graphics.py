
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
    img = pygame.image.load('tabletop.png')
    pygame.display.set_icon(img)
    pygame.display.update()


def draw_card(x, y, cardFace):
    # draw white background on card
    CARD_WIDTH = 67
    CARD_HEIGHT = 93.8
    cardRect = pygame.draw.rect(windowSurface, WHITE, (x, y, CARD_WIDTH, CARD_HEIGHT))
    # gets the number/letter and the suit of the card
    rank = cardFace[:1]
    if rank == "1":
        rank = cardFace[:2]
    suit = cardFace[-1:]
    # check for suit so number is the right colour
    if suit == "h" or suit == "d":
        cardNum = basicFont.render(rank, True, RED)
    else:
        cardNum = basicFont.render(rank, True, BLACK)

    #Moves cardNum to corner
    cardNumRect = cardNum.get_rect()
    cardNumRect.left = x + 7.5
    cardNumRect.top = y + 7.5
    windowSurface.blit(cardNum, cardNumRect)

    # dictionary of card type.  Position of spots, down left side, down right side, down middle
    xPos = {"A": [cardRect.centerx],
            "2": [cardRect.centerx, cardRect.centerx],
            "3": [cardRect.centerx, cardRect.centerx, cardRect.centerx],
            "4": [cardRect.left + (CARD_WIDTH/3), cardRect.left + (CARD_WIDTH/3), cardRect.right - (CARD_WIDTH/3), cardRect.right - (CARD_WIDTH/3)],
            "5": [cardRect.left + (CARD_WIDTH/3), cardRect.left + (CARD_WIDTH/3), cardRect.right - (CARD_WIDTH/3), cardRect.right - (CARD_WIDTH/3), cardRect.centerx],
            "6": [cardRect.left + (CARD_WIDTH/3), cardRect.left + (CARD_WIDTH/3), cardRect.left + (CARD_WIDTH/3), cardRect.right - (CARD_WIDTH/3), cardRect.right - (CARD_WIDTH/3), cardRect.right - (CARD_WIDTH/3)],
            "7": [cardRect.left + (CARD_WIDTH/3), cardRect.left + (CARD_WIDTH/3), cardRect.left + (CARD_WIDTH/3), cardRect.right - (CARD_WIDTH/3), cardRect.right - (CARD_WIDTH/3), cardRect.right - (CARD_WIDTH/3), cardRect.centerx],
            "8": [cardRect.left + (CARD_WIDTH/3), cardRect.left + (CARD_WIDTH/3), cardRect.left + (CARD_WIDTH/3), cardRect.right - (CARD_WIDTH/3), cardRect.right - (CARD_WIDTH/3), cardRect.right - (CARD_WIDTH/3), cardRect.centerx, cardRect.centerx],
            "9": [cardRect.left + (CARD_WIDTH/3), cardRect.left + (CARD_WIDTH/3), cardRect.left + (CARD_WIDTH/3), cardRect.left + (CARD_WIDTH/3), cardRect.right - (CARD_WIDTH/3), cardRect.right - (CARD_WIDTH/3), cardRect.right - (CARD_WIDTH/3), cardRect.right - (CARD_WIDTH/3), cardRect.centerx],
            "10": [cardRect.left + (CARD_WIDTH/3), cardRect.left + (CARD_WIDTH/3), cardRect.left + (CARD_WIDTH/3), cardRect.left + (CARD_WIDTH/3), cardRect.right - (CARD_WIDTH/3), cardRect.right - (CARD_WIDTH/3), cardRect.right - (CARD_WIDTH/3), cardRect.right - (CARD_WIDTH/3), cardRect.centerx, cardRect.centerx],
            "J": [cardRect.centerx],
            "Q": [cardRect.centerx],
            "K": [cardRect.centerx]}

    yPos = {"A": [cardRect.centery],
            "2": [cardRect.top + (CARD_HEIGHT/3), cardRect.bottom - (CARD_HEIGHT/3)],
            "3": [cardRect.top + (CARD_HEIGHT/4), cardRect.centery, cardRect.bottom - (CARD_HEIGHT/4)],
            "4": [cardRect.top + (CARD_HEIGHT/3), cardRect.bottom - (CARD_HEIGHT/3), cardRect.top + (CARD_HEIGHT/3), cardRect.bottom - (CARD_HEIGHT/3)],
            "5": [cardRect.top + (CARD_HEIGHT/3), cardRect.bottom - (CARD_HEIGHT/3), cardRect.top + (CARD_HEIGHT/3), cardRect.bottom - (CARD_HEIGHT/3), cardRect.centery],
            "6": [cardRect.top + (CARD_HEIGHT/4), cardRect.centery, cardRect.bottom - (CARD_HEIGHT/4), cardRect.top + (CARD_HEIGHT/4), cardRect.centery, cardRect.bottom - (CARD_HEIGHT/4)],
            "7": [cardRect.top + (CARD_HEIGHT/4), cardRect.centery, cardRect.bottom - (CARD_HEIGHT/4), cardRect.top + (CARD_HEIGHT/4), cardRect.centery, cardRect.bottom - (CARD_HEIGHT/4), cardRect.top + (CARD_HEIGHT/3)],
            "8": [cardRect.top + (CARD_HEIGHT/4), cardRect.centery, cardRect.bottom - (CARD_HEIGHT/4), cardRect.top + (CARD_HEIGHT/4), cardRect.centery, cardRect.bottom - (CARD_HEIGHT/4), cardRect.top + (CARD_HEIGHT/3), cardRect.bottom - (CARD_HEIGHT/3)],
            "9": [cardRect.top + (CARD_HEIGHT/5), cardRect.top + (CARD_HEIGHT*2/5), cardRect.top + (CARD_HEIGHT*3/5), cardRect.bottom - (CARD_HEIGHT/5), cardRect.top + (CARD_HEIGHT/5), cardRect.top + (CARD_HEIGHT*2/5), cardRect.top + (CARD_HEIGHT*3/5), cardRect.bottom - (CARD_HEIGHT/5), cardRect.centery],
            "10": [cardRect.top + (CARD_HEIGHT/5), cardRect.top + (CARD_HEIGHT*2/5), cardRect.top + (CARD_HEIGHT*3/5), cardRect.bottom - (CARD_HEIGHT/5), cardRect.top + (CARD_HEIGHT/5), cardRect.top + (CARD_HEIGHT*2/5), cardRect.top + (CARD_HEIGHT*3/5), cardRect.bottom - (CARD_HEIGHT/5), cardRect.top + (CARD_HEIGHT/3), cardRect.bottom - (CARD_HEIGHT/3)],
            "J": [cardRect.centery],
            "Q": [cardRect.centery],
            "K": [cardRect.centery]}

    # for each value at the key (the number) it draws the correct spot at each position.
    for spot in range(len(xPos[rank])):
        suitImage = pygame.Rect(cardRect.centerx, cardRect.centery, 20, 20)
        suitImage.centerx = xPos[rank][spot]
        suitImage.centery = yPos[rank][spot]

        if suit == "d":
            diamond = pygame.image.load("diamond2.png")
            #fit diamond image to card size
            diamond = pygame.transform.scale(diamond, (20, 20))
            windowSurface.blit(diamond, suitImage)

        if suit == "h":
            heart = pygame.image.load("heart2.png")
            heart = pygame.transform.scale(heart, (15, 15))
            windowSurface.blit(heart, suitImage)

        if suit == "c":
            club = pygame.image.load("clubs.png")
            club = pygame.transform.scale(club, (20, 20))
            windowSurface.blit(club, suitImage)

        if suit == "s":
            spade = pygame.image.load("spade.png")
            spade = pygame.transform.scale(spade, (20, 20))
            windowSurface.blit(spade, suitImage)

    pygame.display.update()

# shows the text passed at the position passed.
def display_text(text, x, y):
    shownText = basicFont.render(text, True, BLACK)
    textRect = shownText.get_rect()
    textRect.left = x
    textRect.top = y
    windowSurface.blit(shownText, textRect)