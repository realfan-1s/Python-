import turtle
from turtle import color, setworldcoordinates, tracer, update

count = 0


def MoveDisk(fp, tp):
    print('Move disk from %s to %s\n' % (fp, tp))


def Hanoi(height, fromPole, withPole, toPole):
    global count
    if height >= 1:
        Hanoi(height - 1, fromPole, toPole, withPole)
        MoveDisk(fromPole, toPole)
        Hanoi(height - 1, withPole, fromPole, toPole)
        count += 1
    return count


def FourHanoi(height, fromPole, midPole, withPole, toPole):
    global count
    if height >= 2:
        FourHanoi(height - 2, fromPole, toPole, withPole, midPole)
        MoveDisk(fromPole, toPole)
        MoveDisk(fromPole, toPole)
        FourHanoi(height - 2, midPole, withPole, fromPole, toPole)
        count += 2
    return count


print(FourHanoi(3, 'A', 'B', 'C', 'D'))


class Maze:
    def __init__(self, mazeFileName):
        rowsInMaze = 0
        columnsInMaze = 0
        self.mazeList = []
        mazeFile = open(mazeFileName, 'r')
        for line in mazeFile:
            rowList = []
            col = 0
            for ch in line[:-1]:
                rowList.append(ch)
                if ch == 'S':
                    self.startRow = rowsInMaze
                    self.startCol = col
                col += 1
            rowsInMaze += 1
            self.mazeList.append(rowList)
            columnsInMaze = len(rowList)

        self.rowsInMaze = rowsInMaze
        self.columnsInMaze = columnsInMaze
        self.xTranslate = -columnsInMaze / 2
        self.yTranslate = rowsInMaze / 2
        self.t = turtle.Turtle(shape='turtle')
        setup(width=600, height=800)
        setworldcoordinates(-(columnsInMaze - 1) / 2 - .5,
                            -(rowsInMaze - 1) / 2 - .5,
                            (columnsInMaze - 1) / 2 + .5,
                            (rowsInMaze - 1) / 2 + 0.5)

    def DrawMaze(self):
        for y in range(self.rowsInMaze):
            for x in range(self.columnsInMaze):
                if self.mazeList[y][x] == OBSTACLE:
                    self.DrawCenteredBox(x + self.xTranslate,
                                         -y + self.yTranslate, 'tan')

        self.t.color('black', 'blue')

    def DrawCenteredBox(self, x, y, color):
        tracer(0)
        self.t.up()
        self.t.goto(x - .5, y - .5)
        self.t.color('black', color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
            self.t.end_fill()
            update()
            tracer(1)

    def MoveTurtle(self, x, y):
        """
        乌龟移动
        """
        self.t.up()
        self.t.setheading(
            self.t.towards(x + self.xTranslate, -y + self.yTranslate))
        self.t.goto(x + self.xTranslate, -y + self.yTranslates)

    def DropPoints(self, color):
        """
        在已经走过的路径下设置标记
        """
        self.t.dot(color)

    def UpdatePosition(self, row, col, val=None):
        if val:
            self.mazeList[row][col] = val
        self.MoveTurtle(col, row)

        if val == PART_OF_PATH:
            color = 'green'
        elif val == OBSTACLE:
            color = 'red'
        elif val == TRIED:
            color = 'black'
        elif val == DEAD_END:
            color = 'orange'
        else:
            color = None

        if color:
            self.DropPoints(color)

    def IsExit(self, row, col):
        return (row == 0 or row == (self.rowsInMaze - 1) or col == 0
                or col == (self.columnsInMaze - 1))

    def __getitem__(self, idx):
        return self.mazeList[idx]


# 核心函数！！！
def SearchFrom(maze, row, col):
    # 1. 碰到墙壁，返回失败
    maze.UpdatePosition(row, col)
    if maze[row][col] == OBSTACLE:
        return False

    # 2. 碰到标记点或死胡同，返回失败
    if maze[row][col] == TRIED or maze[row][col] == DEAD_END:
        return False

    # 3. 碰到了出口，返回成功
    if maze.IsExit(row, col):
        maze.UpdatePosition(row, col, PART_OF_PATH)
        return True

    # 对已经经历过的道路进行标记
    maze.UpdatePosition(row, col, TRIED)

    # 向东西南北四个方向继续探索,利用or的短路效应（若第一项返回true则不计算后续项）
    found = SearchFrom(maze, row - 1, col) or SearchFrom(
        maze, row + 1, col) or SearchFrom(maze, row, col - 1) or SearchFrom(
            maze, row, col + 1)

    # 探索成功，标记当前点，探索失败，标记为死胡同
    if found:
        maze.UpdatePosition(row, col, PART_OF_PATH)
    else:
        maze.UpdatePosition(row, col, DEAD_END)

    return found
