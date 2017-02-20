def cullent_location(a):
    for pile in p:
        try:
            return p.index(pile), pile.index(a)
        except:
            pass


def ismovable(a, x): #p[x]
    if cullent_location(a)[1] == 0 and (len(p[x]) == 0 or a < p[x][0]):
        return True
    else:
        return False


def move(a, x):
    tmp = p[cullent_location(a)[0]].pop(0)
    p[x].insert(0, tmp)


def tower(a, x):
    if ismovable(a, x):
        move(a, x)
        count.append('')
        print(len(count), p)
        if a == 1:
            pass
        else:
            tower(a-1, x)
    else:
        y = 3 - (x + cullent_location(a)[0])
        tower(a-1, y)
        tower(a, x)


print('Please input n:')
n = int(input())
p = [[d+1 for d in range(n)], [], []]
count = []
print(0, p)
tower(n, 2)