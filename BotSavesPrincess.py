#!/usr/bin/python
def displayPathtoPrincess(n,grid):
    marioPos = ()
    princessPos = ()
    for i in range(n):
        for j in range(n):
            if(grid[i][j] == 'm'):
                marioPos = (i,j)
            if(grid[i][j] == 'p'):
                princessPos = (i,j)
    moves = []
    print(princessPos)
    print(marioPos)
    hDis = marioPos[1] - princessPos[1]
    vDis = marioPos[0] - princessPos[0]
    #print(hDis)
    #print(vDis)
    if(hDis < 0):
        moves.extend(['RIGHT']*abs(hDis))
    elif(hDis > 0):
        moves.extend(['LEFT']*hDis)
    if(vDis < 0):
        moves.extend(['DOWN']*abs(vDis))
    elif(vDis > 0):
        moves.extend(['UP']*vDis)
    for m in moves:
        print(m)
#print all the moves here
m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)

