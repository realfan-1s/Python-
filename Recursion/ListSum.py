import sys
import turtle
"""
递归算法三要素：
1. 递归算法必须有一个基本的结束条件(最小规模问题直接解决)
2. 递归算法必须能改变状态并向基本的结束条件演进(减小问题规模)
3. 递归算法必须调用自身(解决减小了规模的相同问题)
"""


def ListSum(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + ListSum(numList[1:])


print(ListSum([1, 3, 5, 7]))


# 整数转化为任意进制
def ToStr(num, base):
    """
    将整数转化为任意进制
    1. 基本结束条件：小于要求进制的整数
    2. 拆解整数的过程即向基本结束条件演进的过程
    """
    convertString = '0123456789ABCDEF'
    if num < base:
        return convertString[num]
    else:
        return ToStr(num // base, base) + convertString[num % base]


print(ToStr(1453, 16))
print(sys.getrecursionlimit())
sys.setrecursionlimit(3000)
print(sys.getrecursionlimit())

t = turtle.Turtle()


def DrawSprial(t, linelen):
    """
    绘制螺旋线
    """
    if linelen > 0:
        t.forward(linelen)
        t.right(90)
        DrawSprial(t, linelen - 5)


# 分型:自相似递归图形
def Tree(branch_len, t):
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        Tree(branch_len - 15, t)
        t.left(40)
        Tree(branch_len - 15, t)
        t.right(20)
        t.backward(branch_len)


# t.left(90)
# t.penup()
# t.backward(100)
# t.pendown()
# t.pencolor('green')
# t.pensize(1)
# Tree(80, t)
# t.hideturtle()
# turtle.done()


# 谢尔宾斯基三角形
def GetMid(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)


def DrawTriangle(points, color):
    t.fillcolor(color)
    t.penup()
    t.goto(points['top'])
    t.pendown()
    t.begin_fill()
    t.goto(points['left'])
    t.goto(points['right'])
    t.goto(points['top'])
    t.end_fill()


def Sierpinski(degree, points):
    colorMap = ['red', 'green', 'blue', 'orange', 'yellow', 'violet']
    DrawTriangle(
        points,
        colorMap[degree],
    )
    if degree > 0:
        Sierpinski(
            degree - 1, {
                'left': points['left'],
                'right': GetMid(points['left'], points['right']),
                'top': GetMid(points['left'], points['top'])
            })
        Sierpinski(
            degree - 1, {
                'left': GetMid(points['right'], points['left']),
                'right': points['right'],
                'top': GetMid(points['right'], points['top'])
            })
        Sierpinski(
            degree - 1, {
                'left': GetMid(points['top'], points['left']),
                'right': GetMid(points['top'], points['right']),
                'top': points['top']
            })


points = {'left': (0, 0), 'top': (50, 86.6), 'right': (100, 0)}
Sierpinski(3, points)
turtle.done()
