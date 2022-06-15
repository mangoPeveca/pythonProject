import back_end
import graphics
import pygame
from pygame.locals import *
import sys
import time


class Hand():
    def __init__(self, user):
        self.user = user
        self.cardFaces = []
        self.cardValues = []

    def get_user(self):
        return self.user

    def set_card_values(self, cards):
        self.cardValues = cards

    def add_card_face(self, card):
        self.cardFaces.append(card)

    def add_card_value(self, card):
        self.cardValues.append(card)

    def get_card_values(self):
        return self.cardValues

    def get_card_faces(self):
        return self.cardFaces

    def remove_last_card(self):
        cardFace = self.cardFaces.pop()
        cardValue = self.cardValues.pop()
        return cardFace, cardValue

WINDOWWIDTH = 804
WINDOWHEIGHT = 402

# Start Game
graphics.window(WINDOWWIDTH, WINDOWHEIGHT)
graphics.display_text("*** BLACKJACK  ***", 400, 0)
pygame.display.update()

# game loop - will run into red x clicked
while True:

    # Uses Hand class to make a hand for the player and a hand for the dealer.
    playerHand = Hand("player")
    dealerHand = Hand("dealer")

    # card positions
    playerXpos = 5
    PLAYER_Y_POS = 200
    dealerXpos = 5
    dealer_Y_POS = 25
    PLAYER_TOTAL_Y = 185
    dealer_TOTAL_Y = 13
    # reset window
    graphics.window(WINDOWWIDTH, WINDOWHEIGHT)

    # indicate where each players hand is
    graphics.display_text("Player:", 5, PLAYER_Y_POS - 15)
    graphics.display_text("Dealer:", 5, dealer_Y_POS - 15)
    # picks two cards for each hand
    for card in range(2):
        back_end.deal_card(playerHand)
        playerXpos = back_end.draw(playerXpos, PLAYER_Y_POS, playerHand)

    back_end.deal_card(dealerHand)
    dealerXpos = back_end.draw(dealerXpos, dealer_Y_POS, dealerHand)

    # gets and displays the total of player hand and dealerHand
    dealerTotal = str(back_end.user_total(dealerHand))
    playerTotal = str(back_end.user_total(playerHand))

    graphics.display_text(playerTotal, playerXpos, PLAYER_TOTAL_Y)
    graphics.display_text(dealerTotal, dealerXpos, dealer_TOTAL_Y)
    pygame.display.update()

    # Players turn is first
    turn = "player"
    playerMove = ""

    if int(playerTotal) == 21:
        graphics.display_text("Blackjack! You won.", 200, 200)
        time.sleep(3)
        break

    playerCards = playerHand.get_card_faces()
    firstCard = playerCards[0]
    secondCard = playerCards[1]

    # Player picks move. if h pressed, new card added until either total is over 21 or s is  pressed.
    while playerMove != "stand":
        if turn == playerHand.get_user():
            for event in pygame.event.get():
                if event.type == KEYUP:
                    if event.key == K_h:
                        playerMove = "hit"
                    elif event.key == K_s:
                        playerMove = "stand"

            if playerMove == "hit":
                playerTotal = back_end.user_total(playerHand)
                if playerTotal < 21:
                    playerXpos, playerMove, playerTotal = back_end.player_go(playerHand, playerXpos, PLAYER_Y_POS, PLAYER_TOTAL_Y)
                    if playerTotal >= 21:
                        turn = "dealer"
                else:
                    playerMove = "stand"

            elif playerMove == "stand":
                turn = "dealer"

            if int(playerTotal) > 21:
                graphics.display_text("You busted! You lost.", 200, 200)
                time.sleep(3)
                break

        if turn == dealerHand.get_user():
            # dealer move
            dealerXpos = back_end.dealer_move(dealerHand, dealerXpos, dealer_Y_POS)
            # Displays dealers new total
            dealerTotal = str(back_end.user_total(dealerHand))
            graphics.display_text(dealerTotal, dealerXpos, dealer_TOTAL_Y)
            pygame.display.update()
            time.sleep(3)

    graphics.window(WINDOWWIDTH, WINDOWHEIGHT)
    # last total were strings - int needed for calculations
    playerTotal = back_end.user_total(playerHand)
    dealerTotal = back_end.user_total(dealerHand)

    # checks and displays the results of each hand compared to the dealer

    if playerTotal > 21:
        graphics.display_text("You bust! You lost. :(", 200, 200)

    elif dealerTotal > 21:
        graphics.display_text("Dealer busted! You won! :)", 200, 200)

    elif playerTotal == dealerTotal:
        graphics.display_text("You drew.", 200, 200)

    elif playerTotal > dealerTotal:
        graphics.display_text("You won! :)", 200, 200)

    elif playerTotal < dealerTotal:
        graphics.display_text("You lost. :(", 200, 200)

    pygame.display.update()
    time.sleep(3)

    # exit sequence
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()