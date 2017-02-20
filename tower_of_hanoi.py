import sys

def cullent_location(disc):
    for pile in piles:
        try:
            return piles.index(pile), pile.index(disc)
        except:
            pass


def ismovable(disc, destination): #piles[destination]
    if cullent_location(disc)[1] == 0 and (len(piles[destination]) == 0 or disc < piles[destination][0]):
        return True
    else:
        return False


def move(disc, destination):
    tmp = piles[cullent_location(disc)[0]].pop(0)
    piles[destination].insert(0, tmp)


def tower(disc, destination):
    if ismovable(disc, destination):
        move(disc, destination)
        count.append('')
        print(len(count), piles)
        if disc == 1:
            pass
        else:
            tower(disc-1, destination)
    else:
        new_destination = 3 - (destination + cullent_location(disc)[0])
        tower(disc-1, new_destination)
        tower(disc, destination)


print('Please input n:')
try:
    n = int(input())
except:
    print('invalid input')
    sys.exit()

piles = [[i+1 for i in range(n)], [], []]
count = []
print(0, piles)
tower(n, 2)