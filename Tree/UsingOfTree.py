from Tree.PrintTree import CreateTree
from DataStructure.Stack import Stack
import operator


def CalcParseTree(fpexp):
    """
    建立表达式解析树
    创建树的关键是对当前节点的跟踪
    因此可以创建一个栈来记录并跟踪父节点
    节点下降时，将下降前的节点入栈
    节点上升时，上升至Pop出的节点即可
    """
    fpList = fpexp.split()
    pStack = Stack()
    pTree = CreateTree.BinaryTree('')
    pStack.Push(pTree)
    currentTree = pTree
    for p in fpList:
        if p == '(':
            # 入栈下降
            CreateTree.InsertLeft(currentTree, '')
            pStack.Push(currentTree)
            currentTree = CreateTree.GetLeftChild(currentTree)
        elif p not in '+-*/)':
            # 出栈上升
            CreateTree.SetRootVal(currentTree, eval(p))
            parent = pStack.Pop()
            currentTree = parent
        elif p in '+-*/':
            # 入栈下降
            CreateTree.SetRootVal(currentTree, p)
            CreateTree.InsertRight(currentTree, '')
            pStack.Push(currentTree)
            currentTree = CreateTree.GetRightChild(currentTree)
        elif p == ')':
            currentTree = pStack.Pop()
        else:
            raise ValueError("Unknown Operator: " + p)

    return pTree


def Evaluate(parseTree):
    """
    使用递归对表达式解析树进行求值
    """
    opers = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }
    # 缩小规模
    leftC = CreateTree.GetLeftChild(parseTree)
    rightC = CreateTree.GetRightChild(parseTree)

    # 递归调用
    if leftC and rightC:
        fn = opers[CreateTree.GetRootVal(parseTree)]
        return fn(Evaluate(leftC), Evaluate(rightC))
    else:
        return CreateTree.GetRootVal(parseTree)


NumTree = CalcParseTree("( ( 1 + 2 ) + ( ( 3 + 4 ) + 5 ) )")
print(Evaluate(NumTree))


# 后序遍历求值
def PostOrderEval(parseTree):
    opers = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }
    leftC = PostOrderEval(CreateTree.GetLeftChild(parseTree))
    rightC = PostOrderEval(CreateTree.GetRightChild(parseTree))

    if leftC and rightC:
        return opers[CreateTree.GetRootVal(parseTree)](leftC, rightC)
    else:
        return CreateTree.GetRootVal(parseTree)


# 2. 树的遍历,对树的所有数据项进行逐个访问
def Preorder(tree):
    """
    1. preorder(前序遍历):先访问二叉树根节点，再前序访问左子树，最后前序访问右子树
    """
    if tree:
        print(CreateTree.GetRootVal(tree))
        Preorder(CreateTree.GetLeftChild(tree))
        Preorder(CreateTree.GetRightChild(tree))


def Inorder(tree):
    """
    2. inorder(中序遍历):先中序访问左子树，再访问根节点，最后中序访问右子树
    """
    if tree:
        Inorder(CreateTree.GetLeftChild(tree))
        print(CreateTree.GetRootVal(tree))
        Inorder(CreateTree.GetRightChild(tree))


def Postorder(tree):
    """
    3. postorder(后序遍历):先递归后序访问左子树，再后序访问右子树，最后访问根节点
    """
    if tree:
        Postorder(CreateTree.GetLeftChild(tree))
        Postorder(CreateTree.GetRightChild(tree))
        print(CreateTree.GetRootVal(tree))


# 3.生成全括号中缀表达式
def PrintExp(tree):
    sval = ''
    if tree:
        if CreateTree.GetLeftChild(tree):
            sval = '(' + PrintExp(CreateTree.GetLeftChild(tree))
            sval += str(CreateTree.GetRootVal(tree))
            sval += PrintExp(CreateTree.GetRightChild(tree)) + ')'
        else:
            sval += PrintExp(CreateTree.GetLeftChild(tree))
            sval += PrintExp(CreateTree.GetRightChild(tree))

    return sval


NumTree = CalcParseTree("( ( 1 + 2 ) + ( ( 3 + 4 ) + 5 ) ) ")
print(PrintExp(NumTree))
