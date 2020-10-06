# AVL树和BST树的实现方式基本相同，不同之处仅在于二叉树的生成与维护过程
# AVL树的实现中要对每个节点参数跟踪"影响因子"参数
# balanceFactor = height(leftSubTree) - height(rightSubTree),若balanceFactor>0称为左重，若balanceFactor<0称为右重
# AVL树最差情形下的性能：即平衡因子为-1或1,此时的时间复杂度为O(logN)
# 叶节点若作为左子节点插入，父节点的平衡因子+1；作为右子节点差额u，父节点的平衡因子-1,这种影响可能会一直传递到根节点或是到某一父节点是其平衡因子为0
from Tree.BinarySearchTree import TreeNode


class AVLTree:
    def Put(self, key, val):
        if self.root:
            self._Put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)

    def _Put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.GetLeftChild():
                self._Put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
                self.UpdateBalance(currentNode.leftChild)
        else:
            if currentNode.GetRightChild():
                self._Put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)
                self.UpdateBalance(currentNode.rightChild)

    def UpdateBalance(self, node):
        if node.balanceFactor > 1 or node.balanceFactor < -1:
            self.Rebalance(node)
            return
        
        if node.parent != None:
            if node.IsLeftChild():
                node.parent.balanceFactor += 1
            elif node.IsRightChild():
                node.parent.balanceFactor -= 1
            
            if node.parent.balanceFactor != 0:
                self.UpdateBalance(node.parent)

    def Rebalance(self, node):
        """
        实现手段：将不平衡的子树进行旋转；若子树左重，则右旋，右重，则左旋
        同时更新相关父节点的引用，更新旋转后的受影响的节点的影响因子
        以右重为例，若新节点B原来有左节点，则要将左节点设置为A节点的右子节点
        以左重为例探讨更复杂的情况，将左重节点右旋之后，但是新节点原来已有右节点，于是原来的右子节点改变为旧根节点的左子节点
        """
        if node.balanceFactor < 0:
            #  右子节点左重，先右旋
            if node.rightChild.balanceFactor > 0:
                self.RotateRight(node.rightChild)
                self.RotateLeft(node)
            else:
                self.RotateLeft(node)
        elif node.balanceFactor > 0:
            # 左子节点右重，先左旋
            if node.leftChild.balanceFactor < 0:
                self.RotateLeft(node.leftChild)
                self.RotateRight(node)
            else:
                self.RotateRight(node)

    def RotateLeft(self, rotRoot):
        newRoot = rotRoot.rightChild
        # 将新的根节点的右子节点指向旧根节点的左子节点
        rotRoot.rightChild = newRoot.leftChild
        if newRoot.leftChild != None:
            newRoot.leftChild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        # 判断旧的根节点是否是整个二叉树的根
        if rotRoot.IsRoot():
            self.root = newRoot
        else:
            if rotRoot.IsLeftChild():
                rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot
            
        newRoot.leftChild = rotRoot
        rotRoot.parent = newRoot
        newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(rotRoot.balanceFactor, 0)
        rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(newRoot.balanceFactor, 0)
        
    def RotateRight(self, rotRoot):
        newRoot = rotRoot.leftChild
        rotRoot.rightChild = newRoot.rightChild
        if newRoot.rightChild != None:
            newRoot.rightChild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.IsRoot():
            self.root = newRoot
        else:
            if rotRoot.IsLeftChild():
                rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot
        newRoot.rightChild = rotRoot
        rotRoot.parent = newRoot
        newRoot.balanceFactor = newRoot.balanceFactor + 1 - max(rotRoot.balanceFactor, 0)
        rotRoot.balanceFactor = rotRoot.balanceFactor - 1 + min(rotRoot.balanceFactor, 0)




        
