import random

numOfPlayers = [0, 0, 0]

# deal two initial cards to each play

for playerCount in numOfPlayers:
    playerStayed = False
    while True:
        if playerCount <= 16:
            # deal
            break
        elif playerCount <= 21:
            playerStayed = True
            # stay
            break
        else:
            # bust
            break
    if playerStayed:
        # do something
    else:
        # do something else

# compare players count and see who won, then start the next game if have correct number of cards
'''
def dealCards(numberOfCards, deckOfCards, pointer):
    count = 0
    cardsDelt = []
    while count < numberOfCards:
        cardsDelt.append(deckOfCards[pointer])
        pointer += 1
        count += 1
    return cardsDelt, pointer

pointer = 0
deckOfCards =  [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 14]

random.shuffle(deckOfCards)

cards, pointer = dealCards(6, deckOfCards, pointer)

secondHand, pointer = dealCards(6, deckOfCards, pointer)

print("1st Deck", cards, pointer)

print("2nd Deck", secondHand, pointer)
'''
