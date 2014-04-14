'''
CS 321 heuristic.py written by Tony Tran and Miles Douglas
'''

from puzzle8 import getTile

def num_wrong_tiles(state):
	goalState = "123804765"
	numberWrong = 0
	for i in xrange(len(goalState)):
		currentTile = getTile(state,i)
		if currentTile == 0:
			continue
		if str(currentTile) != goalState[i]:
			numberWrong += 1
	
	return numberWrong

def manhattan_distance(state):
	goalState = "123804765"
	distance = 0
	for i in xrange(len(goalState)):
		currentTile = getTile(state,i)
		if str(currentTile) != goalState[i]:
			currentPosition = (i%3, i/3) 
			goalPosition = (goalState.index(str(currentTile))%3, goalState.index(str(currentTile))/3)
			distance += abs(currentPosition[0] - goalPosition[0]) + abs(currentPosition[1] - goalPosition[1])

	return distance