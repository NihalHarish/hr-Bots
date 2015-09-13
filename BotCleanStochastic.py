#!/usr/bin/python


board = []
def find_dirty_tiles():
    global board
    dirty_tiles = []
    for i in range(5):
        for j in range(5):
            if(board[i][j] == 'd'):
                dirty_tiles.append((i,j))
    return dirty_tiles

def find_closest_tile(tiles, cur_row, cur_col):
    min_dist = 10
    min_tile = 0
    for i in range(len(tiles)):
        row_dist = abs(cur_row-tiles[i][0])
        column_dist = abs(cur_col-tiles[i][1])
        dist   = row_dist+column_dist
        if(dist < min_dist):
            min_dist = dist
            min_tile = i
    t = tiles.pop(min_tile)
    return t

    
# Head ends here
def next_move(posr, posc, board):
    dirty_tiles = find_dirty_tiles()
    closest_tile = find_closest_tile(dirty_tiles, posr, posc)
    rowDif = posr - closest_tile[0]
    colDif = posc - closest_tile[1]
    if(rowDif < 0):
        return "DOWN"
    elif(rowDif > 0):
        return "UP"
    if(colDif < 0):
        return "RIGHT"
    elif(colDif > 0):
        return "LEFT"
    elif(colDif == 0 and rowDif == 0):
        return "CLEAN"
# Tail starts here
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    print(next_move(pos[0], pos[1], board))

