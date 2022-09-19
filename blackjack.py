import random
cardCount = 0

def dealCards(numberOfCards, deckOfCards, pointer, numOfPlayers, cardCount, strat):
    count = 0
    while count < numberOfCards:
        for player in range(len(numOfPlayers)):
            currentCard = deckOfCards[pointer]
            numOfPlayers[player] += currentCard
            if currentCard <= strat:
                cardCount += 1
            elif currentCard > 9:
                cardCount -= 1
            pointer += 1
        count += 1
    return [pointer, cardCount]

def playGame(cardCount, winRate, strat):
    deckOfCards =  [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 14]
    random.shuffle(deckOfCards)
    numOfPlayers = [0, 0, 0]
    pointer = 0
    blackJackData = dealCards(2, deckOfCards, pointer, numOfPlayers, cardCount, strat)
    pointer = blackJackData[0]
    cardCount = blackJackData[1]
    #print("STARTING HAND: ",  numOfPlayers)
    #print("KO", cardCount)
    for currentPlayer in range(len(numOfPlayers)):
        playerStayed = False
        while True:
            if cardCount >= 2 and numOfPlayers[currentPlayer] <= 11 and currentPlayer != 0:
                winRate[currentPlayer - 1][2] = True
                currentPlayerCount = [numOfPlayers[currentPlayer]]
                blackJackData = dealCards(1, deckOfCards, pointer, currentPlayerCount, cardCount, strat)
                pointer = blackJackData[0]
                cardCount = blackJackData[1]
                #print("KO", cardCount)
                numOfPlayers[currentPlayer] = currentPlayerCount[0]
            elif numOfPlayers[currentPlayer] <= 16:
                currentPlayerCount = [numOfPlayers[currentPlayer]]
                blackJackData = dealCards(1, deckOfCards, pointer, currentPlayerCount, cardCount, strat)
                pointer = blackJackData[0]
                cardCount = blackJackData[1]
                #print("KO", cardCount)
                numOfPlayers[currentPlayer] = currentPlayerCount[0]
            elif numOfPlayers[currentPlayer] <= 21:
                playerStayed = True
                break
            else:
                break
        '''
        if playerStayed:
            print("PLAYER " + str(currentPlayer) + " stayed. Their hand total is: " + str(numOfPlayers[currentPlayer]))
        else:
            print("PLAYER " + str(currentPlayer) + " busted. Their hand total is: " + str(numOfPlayers[currentPlayer]))
        '''
    #print("FINISHED HAND: ", numOfPlayers)
    for currentPlayer in range(len(numOfPlayers)):
        if currentPlayer == 0:
            continue
        if numOfPlayers[currentPlayer] > 21:
            #print("PLAYER " + str(currentPlayer) + " LOST!")
            if winRate[currentPlayer - 1][2]:
                winRate[currentPlayer - 1][1] += 1
        elif numOfPlayers[currentPlayer] < numOfPlayers[0] and numOfPlayers[0] <= 21:
            #print("PLAYER " + str(currentPlayer) + " LOST!")
            if winRate[currentPlayer - 1][2]:
                winRate[currentPlayer - 1][1] += 1
        elif numOfPlayers[currentPlayer] == numOfPlayers[0] and numOfPlayers[0] <= 21:
            #print("PLAYER " + str(currentPlayer) + " TIED!")
            if winRate[currentPlayer - 1][2]:
                winRate[currentPlayer - 1][0] += 1
        else:
            #print("PLAYER " + str(currentPlayer) + " WON!")
            if winRate[currentPlayer - 1][2]:
                winRate[currentPlayer - 1][0] += 1
    winRate[0][2] = False
    winRate[1][2] = False


cardCount = 0
winRate = [[0, 0, False], [0, 0, False]]
for i in range(1, 1000):
    playGame(cardCount, winRate, 7)

print("KO PLAYER 1 had " + str(winRate[0][0]) + " favorable wins compared to " + str(winRate[0][1]) + " losses!")
print("KO PLAYER 2 had " + str(winRate[1][0]) + " favorable wins compared to " + str(winRate[1][1]) + " losses!")

cardCount = 0
winRate = [[0, 0, False], [0, 0, False]]
for i in range(1, 1000):
    playGame(cardCount, winRate, 6)

print("HILO PLAYER 1 had " + str(winRate[0][0]) + " favorable wins compared to " + str(winRate[0][1]) + " losses!")
print("HILO PLAYER 2 had " + str(winRate[1][0]) + " favorable wins compared to " + str(winRate[1][1]) + " losses!")


# add logic to make players bet smarter, graph results, try to optimize win rate, create way to add more players and more decks of cards, let program tell us when the best time to bet or stay is
