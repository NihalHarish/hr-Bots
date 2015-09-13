#
def nextMove(n,r,c,grid):
    princessPos = ()
    for i in range(n):
        for j in range(n):
            if(grid[i][j] == 'p'):
                princessPos = (i,j)
                break
    vDif = princessPos[0] - r
    hDif = princessPos[1] - c
    if(vDif < 0):
        return "UP"
    elif(vDif > 0):
        return "DOWN"
    if(hDif < 0):
        return "LEFT"
    elif(hDif > 0):
        return "RIGHT"
    return ""
n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))

