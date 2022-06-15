import random

playerTurn = True
dealerTurn = True
playerBust = False
dealerBust = False
dealer = []
player = []
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']

#dealing the cards
def dealing(Cards_num):
    cardsDrawn = 0
    for x in range(Cards_num):
        cardsDrawn = (deck.pop(0))

    return cardsDrawn

#func calculating the total
def total(dealer, times, total):
    br = 0
    ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in range(times):
        for x, e in enumerate(ranks):
            if dealer[i] == 'A' and total > 10:
                total += 1
                br += 1
                break
            elif dealer[i] == 'A' and total <= 10:
                total += 11
                br += 1
                break
            elif dealer[i] == 'J' or dealer[i] == 'Q' or dealer[i] == 'K':
                total += 10
                break
            elif dealer[i] == e:
                total += e
                br += 1
                break
    return total

#player hit or stand function
def hit_or_stand(player):
    turn = 3
    global playerChoice
    global playerBust
    while playerTurn == True:
        if playerChoice == 1:
            playerCard = dealing(1)
            player.append(playerCard)
            playerTotal = total(player, turn, 0)
            turn += 1
            print("You drew: ", playerCard)
            print("Your new total is: ", playerTotal)
            if playerTotal > 21:
                print("You busted! Dealer wins")
                playerBust = True
                break
            playerChoice = int(input("For hit press 1, for stand press 2: "))
        else:
            break
    if playerTotal <= 21:
        print("Your new total is: ", playerTotal)
    return playerTotal

#calculating dealer's total
def dealerHit(dealer, dealerTotal):
    global dealerBust
    turn = 3
    while dealerTotal < 17:
        dealerCard = dealing(1)
        dealer.append(dealerCard)
        dealerTotal = total(dealer, turn, 0)
        turn += 1
        print("Dealer drew: ", dealerCard)
        print("Dealar's total is: ", dealerTotal)
    if dealerTotal > 21:
        print("You win! The dealer busted!")
        dealerBust = True
    return dealerTotal


#shuffleling the deck
for i in range(10):
    random.shuffle(deck)
print(deck)

#dealing hands
for i in range(2):
    dealers = dealing(1)
    dealer.append(dealers)
    playerCard = dealing(1)
    player.append(playerCard)

print(dealer)
print(player)

dealerTotal = total(dealer, 2, 0) #caclucating dealer total
playerTotal = total(player, 2, 0) #caclucating player total

print("Dealer has", dealerTotal)
print("You have: ", playerTotal)

#checking win
def checkWin(playerTotal, dealerTotal, turn):
    if turn == 2:
        if playerTotal == 21 and dealerTotal == 21:
            print("Draw")
        elif playerTotal == 21:
            print("Blackjack! You win!")
        elif dealerTotal == 21:
            print("Blackjack! Delaer wins!")
    elif playerTotal > dealerTotal:
        print("You win!")
    elif playerTotal < dealerTotal:
        print("Dealer wins!")
    else:
        print("Draw!")

checkWin(playerTotal, dealerTotal, 2)

playerChoice = int(input("For hit press 1, for stand press 2: "))
while playerChoice > 2 or playerChoice < 1:
    playerChoice = int(input("For hit press 1, for stand press 2: "))

while playerChoice != 2:
    if playerBust == True:
        break
    playerTotal = hit_or_stand(player)

if playerBust == False:
    dealerTotal = dealerHit(dealer, dealerTotal)
    if dealerBust == False:
        checkWin(playerTotal, dealerTotal, 3)