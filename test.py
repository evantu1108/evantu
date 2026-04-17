
maze = [["+","+",".","+","+"],["+","+",".",".","."],["+",".","+",".","+"],["+",".","+",".","."]]
curX = 0
curY = 2
visited = set()
def findExit(maze, curX, curY, time, visited=set()):
    if (curX, curY) in visited:
        return -1
    visited.add((curX, curY))
    if maze[curX][curY] == "+":
        return -1
    if curX == 0 or curY == 0 or curX == len(maze)-1 or curY == len(maze[0])-1:
        return time
    tries = []
    tries.append(findExit(maze, curX+1, curY, time+1))
    tries.append(findExit(maze, curX-1, curY, time+1))
    tries.append(findExit(maze, curX, curY+1, time+1))
    tries.append(findExit(maze, curX, curY-1, time+1))
    minimum = -1
    for _try in tries:
        if _try != -1:
            minimum = min(_try, minimum) if minimum != -1 else _try
    return minimum
print(findExit(maze, curX, curY, 0))