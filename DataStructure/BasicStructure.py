# 中缀表达式转换为后缀/前缀表达式


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


def InfixToPostFix(infixExpr):
    prec = {}
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1
    opstack = Stack()
    postFixList = []
    tokenList = []
    for i in infixExpr:
        tokenList.append(i)
    # 遇到操作数直接输出，遇到左括号就进栈，遇到右括号就从栈中不断弹出，直到弹出左括号
    for token in tokenList:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in '0123456789' or token in 'abcdefghijklmnopqrstuvwxyz':
            postFixList.append(token)
        elif token == "(":
            opstack.Push(token)
        elif token == ")":
            topToken = opstack.Pop()
            while topToken != '(':
                postFixList.append(topToken)
                topToken = opstack.Pop()
        else:
            while (not opstack.IsEmpty()) and (prec[opstack.Peek()] >=
                                               prec[token]):
                postFixList.append(opstack.Pop())
            opstack.Push(token)

    while not opstack.IsEmpty():
        postFixList.append(opstack.Pop())
    return ' '.join(postFixList)


print(InfixToPostFix("(A+B)*(C+D)"))


def CalcPostFix(num):
    opErandStack = Stack()
    tokenList = []
    for i in num:
        tokenList.append(i)
    for token in tokenList:
        if token in '0123456789':
            opErandStack.Push(token)
        else:
            op2 = opErandStack.Pop()
            op1 = opErandStack.Pop()
            result = DoMath(token, op1, op2)
            opErandStack.Push(result)

    return opErandStack.Pop()


def DoMath(op, str1, str2):
    op1 = float(str1)
    op2 = float(str2)
    if op == '+':
        return op1 + op2
    elif op == '-':
        return op1 - op2
    elif op == '*':
        return op1 * op2
    elif op == '/':
        return op1 / op2


print(CalcPostFix('56*3+'))


def Calculator(infixExpr):
    prec = {}
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1
    opStack = Stack()
    postFixList = []
    tokenList = []
    couldCalc = True
    for i in infixExpr:
        tokenList.append(i)
    for token in tokenList:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in 'abcdefghijklmnopqrstuvwxyz':
            postFixList.append(token)
            couldCalc = False
        elif token in '0123456789':
            postFixList.append(token)
        elif token == '(':
            opStack.Push(token)
        elif token == ')':
            tokenPop = opStack.Pop()
            while tokenPop != '(':
                postFixList.append(tokenPop)
                tokenPop = opStack.Pop()
        else:
            while (not opStack.IsEmpty()) and (prec[opStack.Peek()] >=
                                               prec[token]):
                postFixList.append(opStack.Pop())
            opStack.Push(token)

    while not opStack.IsEmpty():
        postFixList.append(opStack.Pop())

    Answer = ' '.join(postFixList)
    if not couldCalc:
        print("此结果的表达式为: " + Answer)
    else:
        tokenList = Answer.split()
        for token in tokenList:
            if token in '0123456789':
                opStack.Push(token)
            else:
                op2 = opStack.Pop()
                op1 = opStack.Pop()
                result = DoMath(token, op1, op2)
                opStack.Push(result)

        print("计算结果是: " + str(opStack.Pop()))


Calculator("(A+B)*(C+D)")
Calculator("5+3*2")