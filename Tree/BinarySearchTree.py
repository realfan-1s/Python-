# BST下，比父节点小的key都出现在左子树，比父节点大的key都出现在右子树
# 数据插入顺序不同，生成的BST也不同


class BinartSearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        # 使BST可进行迭代
        return self.root.__iter__()

    def Put(self, key, val):
        """
        插入key构造BST
        首先看BST是否为空，若一个节点都没有，那么key节点成为根节点root
        否则调用递归函数_put来放置key
        最差性能是O(log2N)
        若key顺序是按从小到大排列，此时put方法的性能是O(N)
        """
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size += 1

    def _put(self, key, val, currentNode):
        # currentNode即当前二叉查找树子树的根
        """
        若key比currentNode小，则_put到左子树，若无左子树，key便成为左子节点
        若key比currentNode大，则_put到右子树，若无右子树，key便成为右子节点
        """
        if key < currentNode.key:
            if currentNode.GetLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
        else:
            if currentNode.GetRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)

    def __setitem__(self, key, value):
        """
        实现对BST的索引赋值
        """
        self.Put(key, value)

    def Get(self, key):
        """
        在树中找到key所在节点取到payload
        """
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _Get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            self._Get(key, currentNode.leftChild)
        elif key > currentNode.key:
            self._Get(key, currentNode.rightChild)

    def __getitem__(self, key):
        return self.Get(key)

    def __contains__(self, key):
        """
        实现归属判断运算符in
        """
        if self._Get(key, self.root):
            return True
        else:
            return False

    def Delete(self, key):
        if self.size > 1:
            nodeToRemove = self._Get(key, self.root)
            if nodeToRemove:
                self.size -= 1
                self.Remove(nodeToRemove)
            else:
                raise KeyError("This Node does not exist")
        elif self.size == 1 and self.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError("This Node does not exist")

    def __delitem__(self, key):
        self.Delete(key)

    def Remove(currentNode):
        """
        从BST中remove一个节点，仍旧要保持BST的性质，分成以下三种情形:
        1. 该节点中没有子节点
        2. 该节点下只有一个子节点
        3， 该节点下有两个子节点
        当被删除节点上有两个子节点时，可以找被删除节点右子树中最小的作为后继
        """
        if currentNode.IsLeaf():
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        elif currentNode.HasBothChildren():
            succ = currentNode.FindSuccessor()
            succ.SpiceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload
        else:
            if currentNode.GetLeftChild():
                if currentNode.IsLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.IsRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:
                    currentNode.ReplaceNodeData(
                        currentNode.leftChild.key,
                        currentNode.leftChild.payload,
                        currentNode.leftChild.leftChild,
                        currentNode.leftChild.right)
            else:
                if currentNode.IsRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                elif currentNode.IsLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                else:
                    currentNode.ReplaceNodeData(
                        currentNode.rightChild.key,
                        currentNode.rightChild.payload,
                        currentNode.rightChild.leftChild,
                        currentNode.rightChild.rightChild)


class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def GetLeftChild(self):
        return self.leftChild

    def GetRightChild(self):
        return self.rightChild

    def IsLeftChild(self):
        return self.parent and self.leftChild == self.parent

    def IsRightChild(self):
        return self.parent and self.rightChild == self.parent

    def IsRoot(self):
        return not self.parent

    def IsLeaf(self):
        return not (self.leftChild or self.rightChild)

    def HasAnyChildren(self):
        return self.leftChild or self.rightChild

    def HasBothChildren(self):
        return self.leftChild and self.rightChild

    def ReplaceNodeData(self, key, value, lc, rc):
        # 替换根节点
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.GetLeftChild():
            self.leftChild.parent = self
        if self.GetRightChild():
            self.rightChild.parent = self

    def __iter__(self):
        # 进行中序遍历
        if self:
            if self.GetLeftChild():
                for elem in self.leftChild:
                    yield elem
            yield self.key
            if self.GetRightChild():
                for elem in self.rightChild:
                    yield elem

    def FindSuccessor(self):
        """
        寻找后继项
        """
        succ = None
        if self.GetRightChild():
            succ = self.rightChild.FindMin()
        else:
            if self.parent:
                if self.IsLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.FindSuccessor()
                    self.parent.rightChild = self
        return succ

    def FindMin(self):
        current = self
        while current.GetLeftChild():
            current = current.leftChild
        return current

    def SpliceOut(self):
        if self.IsLeaf():
            if self.IsLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.HasAnyChildren():
            if self.GetLeftChild():
                if self.IsLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.IsLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent
