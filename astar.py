from puzzle8 import *
from heuristic import *
from itdeep import *
import Queue
import heapq
import time

goal = state([1,2,3,8,0,4,7,6,5])

class Node:

	def __init__(self, s, p, gC, h):
		self.state = s
		self.path = p
		self.gCost = gC
		self.fCost = h + gC

	def __cmp__(self, other):
		return self.fCost - other.fCost

def formatMoves(path):
	formattedPath = []
	for i in xrange(len(path)-1):
		state1 = path[i]
		state2 = path[i+1]
		for j in xrange(9):
			tile1 = getTile(state1,j)
			tile2 = getTile(state2,j)
			if tile1 != tile2:
				if tile1 == 0:
					diff1 = j
				else:
					diff2 = j
		pathTuple = (diff1, diff2)
		formattedPath.append(pathTuple)
	return formattedPath

def astar(start, heuristic):

	startNode = Node(start, [start], 0, heuristic(start))

	visited = []
	frontier = Queue.PriorityQueue()
	frontier.put(startNode)

	while(frontier):
		curNode = frontier.get()
		if(curNode.state == goal):
			return formatMoves(curNode.path)

		else:
			visited.append(curNode.state)
			for n in neighbors(blankSquare(curNode.state)):
				newState = moveBlank(curNode.state, n)
				if newState not in visited:					
					newG = curNode.gCost + 1
					newPath = []
					for s in curNode.path:
						newPath.append(s)
					newPath.append(newState)
					newNode = Node(newState, newPath, newG, heuristic(newState))
					frontier.put(newNode)

def test():

	randomStates = []
	for i in xrange(5):
		randomStates.append(randomState())

	for s in randomStates:
		startTime = time.clock()
		print "-"*80
		print "Starting itdeep..."
		itdeep(s)
		print "Completed in....", time.clock() - startTime, "..."
		print "-"*80
		print "Starting astar num_wrong_tiles..."
		astar(s, num_wrong_tiles)
		print "Completed in....", time.clock() - startTime, "..."
		print "-"*80
		print "Starting astar manhattan_distance..."
		astar(s, manhattan_distance)
		print "Completed in....", time.clock() - startTime, "..."
		print "-"*80
		print "***"*20
		print "***"*20
		print "***"*20


if __name__ == "__main__":
	test()