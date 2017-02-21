import sys


def current_location(disc):
    for pile in piles:
        try:
            return piles.index(pile), pile.index(disc)
        except:
            pass


def ismovable(disc, destination): #piles[destination]
    if current_location(disc)[1] == 0 and (len(piles[destination]) == 0 or disc < piles[destination][0]):
        return True
    else:
        return False


def move(disc, destination):
    tmp = piles[current_location(disc)[0]].pop(0)
    piles[destination].insert(0, tmp)


def tower(disc, destination):
    global count
    if ismovable(disc, destination):
        move(disc, destination)
        count += 1
        print(count, piles)
        if disc == 1:
            pass
        else:
            tower(disc-1, destination)
    else:
        new_destination = 3 - (destination + current_location(disc)[0])
        tower(disc-1, new_destination)
        tower(disc, destination)


print('Please input n:')
try:
    n = int(input())
except:
    print('invalid input')
    sys.exit()

piles = [[i+1 for i in range(n)], [], []]
count = 0
print(0, piles)
tower(n, 2)
