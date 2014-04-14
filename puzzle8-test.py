from heuristic import *
from itdeep import *
from astar import *
from puzzle8 import *
import random

s = state([1,2,3,7,8,4,0,6,5])
# itdeep = None
# astar = None

if num_wrong_tiles(s) != 2:
    print "Error: Wrong number of tiles"
else:
    print "."

if manhattan_distance(s) != 4:
    print "Error: Manhattan Distance calculated incorrectly"
else:
    print "."

if itdeep(s) != [(6,3), (3,4)]:
    print "Error: Iterative Deepening calculating wrong answer"
else:
    print "."

if astar(s, num_wrong_tiles) != [(6,3), (3,4)]:
    print "Error: Astar incorrect with num_wrong_tiles heur."
else:
    print "."

if astar(s, manhattan_distance) != [(6,3), (3,4)]:
    print "Error: Astar incorrect with manhattan_distance heur."
else:
    print "."


s = state([1,2,3,7,5,8,0,6,4])

if num_wrong_tiles(s) != 4:
    print "Error: Wrong number of tiles"
else:
    print "."

if manhattan_distance(s) != 8:
    print "Error: Manhattan Distance calculated incorrectly"
else:
    print "."

if itdeep(s) != [(6, 7), (7, 4), (4, 5), (5, 8), (8, 7), (7, 6), (6, 3), (3, 4)]:
    print "Error: Iterative Deepening calculating wrong answer"
else:
    print "."

if astar(s, num_wrong_tiles) != [(6, 7), (7, 4), (4, 5), (5, 8), (8, 7), (7, 6), (6, 3), (3, 4)]:
    print "Error: Astar incorrect with num_wrong_tiles heur."
else:
    print "."

if astar(s, manhattan_distance) != [(6, 7), (7, 4), (4, 5), (5, 8), (8, 7), (7, 6), (6, 3), (3, 4)]:
    print "Error: Astar incorrect with manhattan_distance heur."
else:
    print "."


