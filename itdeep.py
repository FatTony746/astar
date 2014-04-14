'''
CS 321 Assignment 1 Part 2
Written By: Miles Douglas and Tony Tran

		Run 1       Run 2
Total(d-1)	0.14679779	0.175899149
	
		0   0.001228423	0.005221165
		1   0.001249932	0.005314042
		2   0.001645882	0.005540369
		3   0.002657754	0.007298193
		4   0.00501488	0.008403431
		5   0.012862514	0.014458047
		6   0.034813796	0.037892919
		7   0.087324609	0.091770982
	(d)	8   0.24365942	0.20332725245567

This shows that the run time of the last limit is the key factor in determining the overall run time of the program.
This is also why limited DFS is the bomb. 

'''



from puzzle8 import *
import time

goal = state([1,2,3,8,0,4,7,6,5])


class Node:
	
	def __init__(self, state, path):
		self.s = state
		self.p = path

# Function
def itdeep(state):
	# t = time.clock()
	found = False
	startNode = Node(state, [state])
	limit = 0
	while(not found):
		# print time.clock() - t
		# t = time.clock()
		found = limitedDFS(startNode, limit)
		startNode.p = [state]
		limit += 1
	return formatMoves(found)

# Takes list of states and turns them into list of moves
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

# Limited depth first seach method
def limitedDFS(node, limit):
	# Goal check
	if node.s == goal:
		return node.p
	# If at bottom of tree
	elif limit == 0:
		return 0
	else:
		# Recursive loop
		for n in neighbors(blankSquare(node.s)):
			newN = moveBlank(node.s, n)
			newP = []
			node.p.append(newN)
			for item in node.p:
				newP.append(item)
			newNode = Node(newN, newP)
			result = limitedDFS(newNode, limit-1)
			# Child node presented no solution
			if result == 0:
				node.p.pop()
				pass
			# Child node is solution
			else:
				return result
	return 0

	