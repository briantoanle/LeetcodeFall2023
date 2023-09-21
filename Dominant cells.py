
'''
take in a grid of whichever dimension, return dominant cells

'''

a = [[1,2,7],[4,5,6],[8,8,9]]
b = [[9,1,1],[1,1,9],[9,1,1],[1,1,9]]

def checkDominant(grid,temp,i,j):
    print(temp,i,j, end=" ")
    if j > 0 and i > 0:
        if grid[j - 1][i - 1] >= temp:
            print('hit top left')
            return False
    if j > 0:
        if grid[j - 1][i] >= temp:
            return False
    if  j > 0 and i < len(grid[0])-1:
        if grid[j - 1][i + 1] >= temp:
            return False
    if i > 0:
        if grid[j][i - 1] >= temp:
            print('hit center left')
            return False
    if i < len(grid[0])-1:
        if grid[j][i + 1] >= temp:
            print('hit center right')
            return False
    if i > 0 and j < len(grid):
        if grid[j+1][i-1] >= temp:
            print('hit bottom left')
            return False
    if j < len(grid)-1:
        if grid[j+1][i] >= temp:
            print('hit bottom middle')
            return False
    if i < len(grid[0]) and j < len(grid):
        if grid[j+1][i+1] >= temp:
            print('hit bottom right')
            return False
    print(i,j,"pass")
    return True
def dominantcells(grid):

    counter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            #print(grid[i][j], end = " ")
            temp = grid[i][j]
            if checkDominant(grid,temp,i,j):
                counter += 1
    return counter

print("here", dominantcells(b))
directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
print(type(directions[0]))
'''

cell at x y 
check 
[x-1,y-1][x,y-1][x+1,y-1]
[x-1,y][x+1,y]
[x-1,y+1][x,y+1][x+1,y+1]


check cell surroundings

cell at 0,0
check 0,1 1,0 1,1

cell at 1,1
check 0,0 0,1 1,0 0,2 1,2 2,0 2,1 2,2


'''