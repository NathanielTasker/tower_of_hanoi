'''
This program solves Tower of Hanoi puzzle
in minimum number of moves.
The puzzle starts with the disks in a neat stack
in ascending order of size on one rod,
the smallest at the top, thus making a conical shape.
The objective of the puzzle is to move the entire stack
to another rod, obeying the following simple rules:
1. Only one disk can be moved at a time.
2. Each move consists of taking the upper disk
  from one of the stacks and placing it on top of another stack
  i.e. a disk can only be moved if it is the uppermost disk on a stack.
3. No disk may be placed on top of a smaller disk.
'''

import sys


def location(disc):
    "returns current location of disc in format like(pile index, disc index)"
    for pile in piles:
        if disc in pile:
            return piles.index(pile), pile.index(disc)


def is_movable(disc, destination):
    """
    returns True/False by whether or not disc is movable to destination
    (destination must be index number of piles)
    """
    is_disc_at_the_top = location(disc)[1] == 0
    dest_pile_is_acceptable = len(piles[destination]) == 0 or disc < piles[destination][0]
    return is_disc_at_the_top and dest_pile_is_acceptable


def move(disc, destination):
    "moves disc to destination(destination must be index number of piles)"
    tmp = piles[location(disc)[0]].pop(0)
    piles[destination].insert(0, tmp)


def stack(max_disc, destination):
    "make disks of 1 to max_disc stacked in ascending order of size on one rod at destination"
    global count
    if is_movable(max_disc, destination):
        move(max_disc, destination)
        count += 1
        print(count, piles)
        if max_disc == 1:
            pass
        else:
            stack(max_disc-1, destination)
    else:
        new_destination = 3 - (destination + location(max_disc)[0])
        stack(max_disc-1, new_destination)
        stack(max_disc, destination)


print('Please input n:')
try:
    n = int(input())
except TypeError as err:
    print('Invalid input')
    sys.exit()

piles = [[i+1 for i in range(n)], [], []]
count = 0
print(0, piles)
stack(n, 2)
