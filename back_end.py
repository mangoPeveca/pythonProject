import random
import graphics
import time
import pygame
from pygame.locals import *

#all possible cards in the pack (only uses 1 pack)
deck =  ['2h', '2d','2c', '2s', '3h', '3d', '3s', '3c', '4h', '4d', '4s', '4c', '5h', '5d', '5s', '5c', '6h', '6d', '6s', '6c', '7h', '7d', '7s', '7c', '8h', '8d', '8s', '8c', '9h', '9d', '9s', '9c', '10h', '10d', '10s', '10c', 'Jh', 'Jd', 'Js', 'Jc', 'Qh', 'Qd', 'Qs', 'Qc', 'Kh', 'Kd', 'Ks', 'Kc', 'Ah', 'Ad', 'As', 'Ac', '2h', '2d','2c', '2s', '3h', '3d', '3s', '3c', '4h', '4d', '4s', '4c', '5h', '5d', '5s', '5c', '6h', '6d', '6s', '6c', '7h', '7d', '7s', '7c', '8h', '8d', '8s', '8c', '9h', '9d', '9s', '9c', '10h', '10d', '10s', '10c', 'Jh', 'Jd', 'Js', 'Jc', 'Qh', 'Qd', 'Qs', 'Qc', 'Kh', 'Kd', 'Ks', 'Kc', 'Ah', 'Ad', 'As', 'Ac', '2h', '2d','2c', '2s', '3h', '3d', '3s', '3c', '4h', '4d', '4s', '4c', '5h', '5d', '5s', '5c', '6h', '6d', '6s', '6c', '7h', '7d', '7s', '7c', '8h', '8d', '8s', '8c', '9h', '9d', '9s', '9c', '10h', '10d', '10s', '10c', 'Jh', 'Jd', 'Js', 'Jc', 'Qh', 'Qd', 'Qs', 'Qc', 'Kh', 'Kd', 'Ks', 'Kc', 'Ah', 'Ad', 'As', 'Ac', '2h', '2d','2c', '2s', '3h', '3d', '3s', '3c', '4h', '4d', '4s', '4c', '5h', '5d', '5s', '5c', '6h', '6d', '6s', '6c', '7h', '7d', '7s', '7c', '8h', '8d', '8s', '8c', '9h', '9d', '9s', '9c', '10h', '10d', '10s', '10c', 'Jh', 'Jd', 'Js', 'Jc', 'Qh', 'Qd', 'Qs', 'Qc', 'Kh', 'Kd', 'Ks', 'Kc', 'Ah', 'Ad', 'As', 'Ac']

# Chooses a card from the values and adds to the hand
def deal_card(UserHand):
    newCard = ""
    while newCard == "":
        newCard = random.choice(deck)
        deck.remove(newCard)
    UserHand.add_card_face(newCard)
    if newCard[:1] == "J":
        UserHand.add_card_value(10)
    elif newCard[:1] == "Q":
        UserHand.add_card_value(10)
    elif newCard[:1] == "K":
        UserHand.add_card_value(10)
    elif newCard[:1] == "A":
        UserHand.add_card_value(11)
    elif newCard[:1] == "1":
        UserHand.add_card_value(10)
    else:
        value = int(newCard[:1])
        UserHand.add_card_value(value)

def draw(x, y, userHand):
    # display in window and moves position across
    next = next_card(userHand)
    graphics.draw_card(x, y, next)
    x = x + 72
    return x

# adds each card and returns total
def user_total(UserHand):
    cards = UserHand.get_card_values()
    total = 0
    for n in range(len(cards)):
        total = total + cards[n]

    return total

# algorithm dealer uses - only twists if total less than 17.
def dealer_move(UserHand, x, y):
    total = user_total(UserHand)

    while total < 17:
        deal_card(UserHand)
        x = draw(x, y, UserHand)
        total = user_total(UserHand)
        ace_swap(UserHand, total)
        total = user_total(UserHand)
        graphics.display_text(str(total), x, 13)
        time.sleep(3)

    return x


# checks for ace in pack and swaps value to 1
def ace_swap(UserHand, total):
    cards = UserHand.get_card_values()
    if total > 21:
        if 11 in cards:
            Aindex = cards.index(11)
            cards[Aindex] = 1
            UserHand.set_card_values(cards)

#returs last card in list
def next_card(userHand):
    cardList = userHand.get_card_faces()
    length = len(cardList)
    card = cardList[length-1]

    return card

#player interaction
def player_go(playerHand, playerXpos, PLAYER_Y_POS, PLAYER_TOTAL_Y):
    deal_card(playerHand)
    playerXpos = draw(playerXpos, PLAYER_Y_POS, playerHand)
    playerTotal = user_total(playerHand)
    playerMove = ""

    # Check for ace - change to 1 if bust
    ace_swap(playerHand, playerTotal)

    # Displays new total
    playerTotal = str(user_total(playerHand))
    graphics.display_text(playerTotal, playerXpos, PLAYER_TOTAL_Y)
    pygame.display.update()

    return playerXpos, playerMove, int(playerTotal)