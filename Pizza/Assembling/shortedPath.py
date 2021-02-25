width = 5
height = 4

grid = [False] * (width * height + 1)
wasHere = [False] * (width * height + 1)
correctPath = [False] * (width * height + 1)

startX = 0
startY = 0
endX = 4
endY = 4

moves = []
def recursiveSolve(x, y):
    if (x == endX and y == endY):
        return True
    if (grid[x*width + y] or wasHere[x * width + y]):
        return False
    # If you are on a wall or already were here
    wasHere[x*width + y] = True
    if (x != 0): # Checks if not on left edge
        if (recursiveSolve(x-1, y)): # Recalls method one to the left
            moves.append('L')
            correctPath[x*width + y] = True # Sets that path value to True
            return True
    if (x != width - 1): # Checks if not on right edge
        if (recursiveSolve(x+1, y)):# Recalls method one to the right
            moves.append('R')
            correctPath[x*width + y] = True
            return True
    if (y != 0):  # Checks if not on top edge
        if (recursiveSolve(x, y-1)): # Recalls method one up
            moves.append('U')
            correctPath[x*width + y] = True
            return True
    if (y != height - 1): # Checks if not on bottom edge
        if (recursiveSolve(x, y+1)): # Recalls method one down
            moves.append('D')
            correctPath[x*width + y] = True
            return True
    return False

recursiveSolve(startX, startY)
print(moves)