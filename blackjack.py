import random
import mysql.connector
import matplotlib.pyplot as plt

cnx = mysql.connector.connect(user='root', password='Ausjus1995', host='127.0.0.1', database='blackjack') 
cursor = cnx.cursor()
add_data_ko = ("Insert into KO " "(P1_wins, P1_losses, P2_wins, P2_losses) " "Values (%s, %s, %s, %s)")
add_data_hilo = ("Insert into hilo " "(P1_wins, P1_losses, P2_wins, P2_lossess) " "Values (%s, %s, %s, %s)")

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

'''
for j in range(1, 10):
    cardCount = 0
    winRate = [[0, 0, False], [0, 0, False]]
    for i in range(1, 1000): #ko
        playGame(cardCount, winRate, 7)
    Win_Loss_Data = (winRate[0][0], winRate[0][1], winRate[1][0], winRate[1][1])
    cursor.execute(add_data_ko, Win_Loss_Data)
    cardCount = 0
    winRate = [[0, 0, False], [0, 0, False]]
    for i in range(1, 1000): #hilo
        playGame(cardCount, winRate, 6)
    Win_Loss_Data = (winRate[0][0], winRate[0][1], winRate[1][0], winRate[1][1])
    cursor.execute(add_data_hilo, Win_Loss_Data)

cnx.commit()
cursor.close()
cnx.close()
'''
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
players = ['P1 Wins', 'P2 Wins', 'P1 Losses', 'P2 Losses']
graphData = []
dbValues = ["P1_wins", "P2_wins", "P1_losses", "P2_losses"]
for val in dbValues:
    cursor.execute("Select " + val + " from KO")
    dbData = cursor.fetchall()
    lengthData = len(dbData)
    sumData = 0
    for x in dbData:
        sumData += x[0]
    aveData = "{:.2f}".format(sumData/lengthData)
    print(aveData)
    graphData.append(aveData)
ax.bar(players,graphData)
#plt.show()

dbValues2 = ["P1_wins", "P2_wins", "P1_losses", "P2_lossess"]
fig2 = plt.figure()
ax2 = fig2.add_axes([0,0,1,1])
graphDataHilo = []
for val in dbValues2:
    cursor.execute("Select " + val + " from hilo")
    dbData = cursor.fetchall()
    lengthData = len(dbData)
    sumData = 0
    for x in dbData:
        sumData += x[0]
    aveData = "{:.2f}".format(sumData/lengthData)
    print(aveData)
    graphDataHilo.append(aveData)
ax2.bar(players,graphDataHilo)
plt.show()
'''
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
langs = ['C', 'C++', 'Java', 'Python', 'PHP']
students = [23,17,35,29,12]
ax.bar(langs,students)
plt.show()
'''
# format graph correctly
# add logic to make players bet smarter, graph results, try to optimize win rate, create way to add more players and more decks of cards, let program tell us when the best time to bet or stay is
