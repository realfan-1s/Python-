# 常见的四种线性数据结构 1.Stack栈 2.Queue队列 3.两端队列Deque 4.列表List
# 这种数据项之间只存在先后顺序


# 1.栈 有次序的数据集合，数据项的加入和移除都在同一段（栈顶），后进先出
# 使用python实现Stack
class Stack:
    def __init__(self):
        self.items = []

    def IsEmpty(self):
        return self.items == []

    def Push(self, item):
        self.items.append(item)

    def Pop(self):
        return self.items.pop()

    def Peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


# Stack测试代码
# s = Stack()
# print(s.IsEmpty())
# s.Push(4)
# s.Push('Dog')
# print(s.Peek())
# s.Push(True)
# print(s.size())
# print(s.IsEmpty())
# s.Push(8.4)
# print(s.Pop())
# print(s.Pop())
# print(s.size())


# 栈的引用——Lisp简单括号匹配
def Bracket(symbolString):
    z = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        if symbolString[index] == '(':
            z.Push(symbolString[index])
        else:
            if z.IsEmpty():
                balanced = False
            else:
                z.Pop()
        index += 1
    if balanced and z.IsEmpty():
        return True
    else:
        return False


# 匹配多种括号
def ParChecker(symbolString):
    z = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in '[{(':
            z.Push(symbol)
        else:
            if z.IsEmpty():
                balanced = False
            else:
                top = z.Pop()
                if not Match(top, symbol):
                    balanced = False
        index += 1
    if balanced and z.IsEmpty():
        return True
    else:
        return False


def Match(open, close):
    opens = '([{'
    closes = ')]}'
    return opens.index[open] == closes.index[close]


# 十进制转化为二进制
# 使用除以N求余数的算法可以快速扩展为转换成N进制
def Conversion(decNumber):
    z = Stack()
    while decNumber > 0:
        rem = decNumber % 2
        z.Push(rem)
        decNumber = decNumber // 2

    binStr = ''
    while not z.IsEmpty():
        binStr += str(z.Pop())
    return binStr


print(Conversion(42))