import random

def dealCards(numberOfCards, deckOfCards, pointer, numOfPlayers):
    count = 0
    while count < numberOfCards:
        for player in range(len(numOfPlayers)):
            numOfPlayers[player] += deckOfCards[pointer]
            pointer += 1
        count += 1
    return pointer

def playGame():
    deckOfCards =  [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 14]
    random.shuffle(deckOfCards)
    numOfPlayers = [0, 0, 0]
    pointer = 0
    pointer = dealCards(2, deckOfCards, pointer, numOfPlayers)
    print("STARTING HAND: ",  numOfPlayers)
    for currentPlayer in range(len(numOfPlayers)):
        playerStayed = False
        while True:
            if numOfPlayers[currentPlayer] <= 16:
                currentPlayerCount = [numOfPlayers[currentPlayer]]
                pointer = dealCards(1, deckOfCards, pointer, currentPlayerCount)
                numOfPlayers[currentPlayer] = currentPlayerCount[0]
            elif numOfPlayers[currentPlayer] <= 21:
                playerStayed = True
                break
            else:
                break
        if playerStayed:
            print("PLAYER " + str(currentPlayer) + " stayed. There hand total is: " + str(numOfPlayers[currentPlayer]))
        else:
            print("PLAYER " + str(currentPlayer) + " busted. There hand total is: " + str(numOfPlayers[currentPlayer]))
    print("FINISHED HAND: ", numOfPlayers)
    for currentPlayer in range(len(numOfPlayers)):
        if currentPlayer == 0:
            continue
        if currentPlayer > 21:
            print("PLAYER " + str(currentPlayer) + " LOST!")
        elif currentPlayer < numOfPlayers[0] and numOfPlayers[0] <= 21:
            print("PLAYER " + str(currentPlayer) + " LOST!")
        elif currentPlayer == numOfPlayers[0] and numOfPlayers[0] <= 21:
            print("PLAYER " + str(currentPlayer) + " TIED!")
        else:
            print("PLAYER " + str(currentPlayer) + " WON!")


playGame()

# Implement KO Strategy, create way to add more players and more decks of cards, let program tell us when the best time to bet or stay is
