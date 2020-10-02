# 树：空集或由根节点以及零个或多个子节点构成，每个子节点到根必须有边相连
# 树的结构——层次化，越接近顶部越普遍，越接近底部越独特
# 两个子节点之间相互独立、隔离
# 树的下方每一个叶节点都具有唯一性,可以从根开始到达每一个种的完全路径来唯一标识每一个物种
# 节点(Node):组成树的基本部分 每个节点具有名称，还可以保留额外的数据项
# 边(edge)组成树的另一个基本组成部分，每条边恰好链接两个节点，具有出入方向
# 根节点(root)树中唯一一个没有入边的节点，兄弟节点(sibling)具有同一个父节点的节点


class CreateTree:
    """
    通过python list实现二叉树的数据结构
    使用嵌套列表法实现树，很容易从二叉树扩展到多叉树
    第一个元素为根节点的值；第二个元素是左子树；第三个元素是右子树
    """
    def BinaryTree(root):
        """
        创建仅有根节点的二叉树
        """
        return [root, [], []]

    def InsertLeft(tree, newBranch):
        """
        将新节点插入树中作为直接的左节点
        """
        t = tree.pop(1)
        if len(t) > 1:
            # 将旧的左子树作为新节点的左子树
            tree.insert(1, [newBranch, t, []])
        else:
            tree.insert(1, [newBranch, [], []])
        return tree

    def InsertRight(tree, newBranch):
        """
        将新节点插入树中作为直接的右节点
        """
        t = tree.pop(2)
        if len(t) > 1:
            tree.insert(2, [newBranch, [], t])
        else:
            tree.insert(2, [newBranch, [], []])
        return tree

    def GetRootVal(tree):
        """
        取得根节点
        """
        return tree[0]

    def SetRootVal(tree, newVal):
        """
        设置根节点
        """
        tree[0] = newVal

    def GetLeftChild(tree):
        """
        返回左子树
        """
        return tree[1]

    def GetRightChild(tree):
        """
        返回右子树
        """
        return tree[2]


class MyBinaryTree:
    """
    使用节点链接法实现树
    """
    def __init__(self, rootObj):
        """
        成员key保存根节点数据项
        成员left/rightchild保存左右子树的引用
        """
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def InsertLeft(self, newNode):
        """
        插入左子树
        """
        if self.leftChild is None:
            self.leftChild = MyBinaryTree(newNode)
        else:
            t = MyBinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def InsertRight(self, newNode):
        """
        插入右子树
        """
        if self.rightChild is None:
            self.rightChild = MyBinaryTree(newNode)
        else:
            t = MyBinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def GetLeftChild(self):
        return self.leftChild

    def GetRightChild(self):
        return self.rightChild

    def SetRootVal(self, root):
        self.key = root

    def GetRootVal(self):
        return self.key
