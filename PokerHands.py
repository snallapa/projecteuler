pokerHands = []
with open('pokerhands.txt') as f:
    for line in f:
    	line = line.split()
    	firstHand = line[0:5]
    	secondHand = line[5:]
    	game = [firstHand, secondHand]
        pokerHands.append(game)

def checkOrder(mylist):
    it = (int(x, 16) for x in mylist)
    first = next(it)
    return all(a == b for a, b in enumerate(it, first + 1))
def duplicates(mylist):
	numberCounts = {}
	for num in mylist:
		count = 0
		for num2 in mylist:
			if num == num2:
				count += 1
		numberCounts[num] = count
	return numberCounts

def getScore(playerHand):
	player1Numbers = []
	player1Suits = []
	player2Numbers = []
	player2Suits = []
	player1Score= 0
	for card in playerHand:
		if card[0] == 'T':
			card[0] = '10'
		elif card[0] == 'J':
			card[0] = '11'
		elif card[0] == 'Q':
			card[0] = '12'
		elif card[0] == 'K':
			card[0] = '13'
		elif card[0] == 'A':
			card[0] = '13'
		player1Numbers.append(int(card[0]))
		player1Suits.append(card[1])
	player1Numbers.sort()
	if len(set(player1Suits)) == 1:
		player1Score = 60
		if checkOrder(player1Numbers):
			player1Score == 90
			if player1Numbers[0] == 10 and player1Numbers[1] == 11 and player1Numbers == 12 and player1Numbers == 13 and player1Numbers == 14:
				player1Score == 100
	if checkOrder(player1Numbers):
		player1Score = 40
	player1Counts = duplicates(player1Numbers)
	numberOfPairs = [0,0,0,0,0]
	for num in player1Numbers:
		if player1Counts[num] == 4:
			player1Score = 80
			break
		if player1Counts[num] == 3:
			numberOfPairs[3] = 1
		if player1Counts[num] == 2:
			numberOfPairs[2] += 1
	if numberOfPairs[3] == 1:
		player1Score = 40
		if numberOfPairs[2] == 1:
			player1Score = 70
	if numberOfPairs[2] == 2:
		player1Score = 30
	if numberOfPairs[2] == 1:
		player1Score = 20

def pokerGame(game):
	player1 = game[0]
	player2 = game[1]




